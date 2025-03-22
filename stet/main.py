import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from tensorflow import keras
from tensorflow.keras import layers
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import norm


def compute_obscurity_scores(csv_file, output_file=None):
    """
    Compute obscurity scores for NFL players using deep learning.

    This function:
    1. Loads NFL player data
    2. Processes and normalizes relevant features
    3. Creates a custom deep learning model
    4. Computes obscurity scores (100 = most obscure, 0 = least obscure)
    5. Returns dataframe with added obscurity scores

    Args:
        csv_file (str): Path to CSV file with NFL player data
        output_file (str, optional): Path to save results. If None, doesn't save.

    Returns:
        pandas.DataFrame: Player data with computed obscurity scores
    """
    # 1. Load and prepare the data
    df = pd.read_csv(csv_file)

    # Clean the data
    df = df.fillna(0)

    # 2. Feature extraction & engineering

    # A. Basic visibility features
    # Pageviews - direct measure of visibility (inverse relation to obscurity)
    if 'Pageviews' in df.columns:
        df['pageviews_factor'] = df['Pageviews']
    else:
        # If no pageviews data, estimate from games played and awards
        df['pageviews_factor'] = df['G'] * 5000

    # B. Accomplishment features
    # Combine awards
    df['awards_count'] = df['MVP'] + df['OPOY'] + df['DPOY'] + \
        df['OROY'] + df['DROY'] + df['AP1'] + df['SB']

    # C. Position-specific performance metrics
    # For QBs
    df['qb_career_value'] = 0
    qb_mask = df['Pos'] == 'QB'
    if qb_mask.any():
        df.loc[qb_mask, 'qb_career_value'] = (
            df.loc[qb_mask, 'PaYds'] * 0.1 +
            df.loc[qb_mask, 'PaTD'] * 5 +
            df.loc[qb_mask, 'QBWin'] * 10 +
            df.loc[qb_mask, 'GWD'] * 15
        )

    # For RBs
    df['rb_career_value'] = 0
    rb_mask = df['Pos'] == 'RB'
    if rb_mask.any():
        df.loc[rb_mask, 'rb_career_value'] = (
            df.loc[rb_mask, 'RuYds'] * 0.2 +
            df.loc[rb_mask, 'RuTD'] * 10 +
            df.loc[rb_mask, 'RecYds'] * 0.15
        )

    # For WRs/TEs
    df['wr_te_career_value'] = 0
    wr_te_mask = (df['Pos'] == 'WR') | (df['Pos'] == 'TE')
    if wr_te_mask.any():
        df.loc[wr_te_mask, 'wr_te_career_value'] = (
            df.loc[wr_te_mask, 'RecYds'] * 0.2 +
            df.loc[wr_te_mask, 'RecTD'] * 10 +
            df.loc[wr_te_mask, 'Rec'] * 0.5
        )

    # For defensive players
    df['def_career_value'] = 0
    def_mask = df['Pos'].isin(['DE', 'DT', 'LB', 'CB', 'S'])
    if def_mask.any():
        df.loc[def_mask, 'def_career_value'] = (
            df.loc[def_mask, 'Solo'] * 1 +
            df.loc[def_mask, 'Ast'] * 0.5 +
            df.loc[def_mask, 'TFL'] * 3 +
            df.loc[def_mask, 'IntD'] * 15 +
            df.loc[def_mask, 'FF'] * 10
        )

    # Combine all position values into a single career value metric
    career_value_cols = ['qb_career_value', 'rb_career_value',
                         'wr_te_career_value', 'def_career_value']
    df['career_value'] = df[career_value_cols].max(axis=1)

    # D. Career longevity and volume
    df['games_factor'] = df['G'] / df['G'].max() if df['G'].max() > 0 else 0
    df['fantasy_factor'] = df['FantPts'] / \
        df['FantPts'].max() if df['FantPts'].max() > 0 else 0

    # 3. Calculate the base obscurity score using key metrics

    # A. Extract normalized key metrics (higher = less obscure)
    # Reverse the logic: higher values in these metrics = lower obscurity
    metrics = pd.DataFrame()

    # Normalize each metric to 0-1 range
    if df['pageviews_factor'].max() > 0:
        metrics['pageviews'] = df['pageviews_factor'] / \
            df['pageviews_factor'].max()
    else:
        metrics['pageviews'] = 0

    # Normalizing assuming 10 awards is maximum
    metrics['awards'] = df['awards_count'] / 10
    metrics['career_value'] = df['career_value'] / \
        df['career_value'].max() if df['career_value'].max() > 0 else 0
    metrics['games'] = df['games_factor']
    metrics['fantasy'] = df['fantasy_factor']

    # B. Calculate the visibility score (inverse of obscurity)
    # Weight the metrics based on importance
    weights = {
        'pageviews': 0.6,
        'awards': 0.3,
        'career_value': 0.2,
        'games': 0.05,
        'fantasy': 0.05
    }

    visibility_score = (
        metrics['pageviews'] * weights['pageviews'] +
        metrics['awards'] * weights['awards'] +
        metrics['career_value'] * weights['career_value'] +
        metrics['games'] * weights['games'] +
        metrics['fantasy'] * weights['fantasy']
    )

    # C. Convert visibility to obscurity (100 = most obscure, 0 = least obscure)
    df['obscurity_score_basic'] = 100 * (1 - visibility_score)

    # 4. Deep Learning Enhancement
    # Use a neural network to capture more complex relationships

    # A. Prepare features for deep learning
    feature_cols = [
        'pageviews_factor', 'awards_count', 'career_value',
        'G', 'GS', 'FantPts'
    ]

    categorical_cols = ['Pos']

    # Create position-specific performance columns for better feature representation
    for pos in df['Pos'].unique():
        # Skip if position is missing/nan
        if pd.isna(pos):
            continue

        pos_mask = df['Pos'] == pos
        if pos_mask.sum() > 0:
            # For each position, add relevant stat columns
            if pos == 'QB':
                df[f'{pos}_PaYds_per_G'] = df['PaYds'] / \
                    df['G'].where(df['G'] > 0, 1)
                df[f'{pos}_PaTD_per_G'] = df['PaTD'] / \
                    df['G'].where(df['G'] > 0, 1)
                feature_cols.extend(
                    [f'{pos}_PaYds_per_G', f'{pos}_PaTD_per_G'])
            elif pos == 'RB':
                df[f'{pos}_RuYds_per_G'] = df['RuYds'] / \
                    df['G'].where(df['G'] > 0, 1)
                df[f'{pos}_RuTD_per_G'] = df['RuTD'] / \
                    df['G'].where(df['G'] > 0, 1)
                feature_cols.extend(
                    [f'{pos}_RuYds_per_G', f'{pos}_RuTD_per_G'])
            elif pos in ['WR', 'TE']:
                df[f'{pos}_RecYds_per_G'] = df['RecYds'] / \
                    df['G'].where(df['G'] > 0, 1)
                df[f'{pos}_RecTD_per_G'] = df['RecTD'] / \
                    df['G'].where(df['G'] > 0, 1)
                feature_cols.extend(
                    [f'{pos}_RecYds_per_G', f'{pos}_RecTD_per_G'])

    # Fill any NaNs created during the calculation
    df = df.fillna(0)

    # Select features and preprocess
    X = df[feature_cols + categorical_cols]

    # Create preprocessing pipeline with sparse output for categorical features
    numerical_transformer = StandardScaler()

    # Use sparse output for OneHotEncoder to save memory
    categorical_transformer = OneHotEncoder(
        handle_unknown='ignore', sparse_output=False)

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numerical_transformer, feature_cols),
            ('cat', categorical_transformer, categorical_cols)
        ],
        sparse_threshold=0  # Force dense output from the transformer
    )

    # Fit and transform the data
    X_processed = preprocessor.fit_transform(X)

    # B. Build and train the model
    # We'll use the basic obscurity score as a starting point
    # and refine it with the neural network
    initial_obscurity = df['obscurity_score_basic'].values

    # Define the model with memory optimization
    model = keras.Sequential([
        layers.InputLayer(input_shape=(X_processed.shape[1],)),
        layers.Dense(32, activation='relu', use_bias=True),
        layers.BatchNormalization(),
        layers.Dropout(0.3),
        layers.Dense(16, activation='relu', use_bias=True),
        layers.Dense(1, activation='sigmoid')  # Output between 0 and 1
    ])

    # Use a memory-efficient optimizer
    optimizer = keras.optimizers.Adam(learning_rate=0.001)

    model.compile(
        optimizer=optimizer,
        loss='mse',
        metrics=['mae']
    )

    # Train the model to learn from the initial obscurity scores
    # This helps capture complex non-linear relationships

    # Set up callbacks to handle warnings
    callbacks = [
        keras.callbacks.EarlyStopping(
            monitor='loss',
            patience=5,
            restore_best_weights=True
        )
    ]

    # Suppress TensorFlow warnings during training
    import os
    import tensorflow as tf
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # Suppress TF warnings

    # Train with memory-optimized settings
    model.fit(
        X_processed,
        initial_obscurity / 100,  # Scale to 0-1 for training
        epochs=30,  # Reduced epochs
        batch_size=8,  # Increased batch size for better memory efficiency
        callbacks=callbacks,
        verbose=1
    )

    # Make predictions and convert back to 0-100 scale
    refined_obscurity = model.predict(X_processed).flatten() * 100

    # Combine initial and refined scores (giving more weight to refined)
    df['obscurity_score'] = 0.3 * \
        df['obscurity_score_basic'] + 0.7 * refined_obscurity

    # 5. Apply business rules and adjustments

    # A. Award winners should have lower obscurity
    # Super Bowl winners, MVPs, etc. are well-known
    award_winners = df['awards_count'] > 0
    if award_winners.any():
        df.loc[award_winners, 'obscurity_score'] *= 0.8  # Reduce obscurity by 20%

    # B. Long careers lead to more visibility
    long_careers = df['G'] > 100
    if long_careers.any():
        df.loc[long_careers, 'obscurity_score'] *= 0.9  # Reduce obscurity by 10%

    # C. Recent Rookie of the Year winners get more attention
    rookies = (df['OROY'] > 0) | (df['DROY'] > 0)
    if rookies.any():
        df.loc[rookies, 'obscurity_score'] *= 0.85  # Reduce obscurity by 15%

    # D. Clean up final scores
    # Ensure scores are within 0-100 range
    df['obscurity_score'] = df['obscurity_score'].clip(0, 100)

    # E. Transform the distribution to be more normal
    # First, calculate mean and standard deviation of current scores
    mean_score = df['obscurity_score'].mean()
    std_score = df['obscurity_score'].std()

    # If standard deviation is too small, set a minimum value
    std_score = max(std_score, 10)

    # Apply transformation to create more of a normal distribution
    # This uses a logistic function to spread out the values
    from scipy import stats

    # Convert to z-scores first
    z_scores = (df['obscurity_score'] - mean_score) / std_score

    # Apply sigmoid transformation to spread values more evenly
    transformed_scores = 1 / (1 + np.exp(-z_scores))

    # Scale back to 0-100 range with better spread
    # Adjust these parameters to control the shape of the distribution
    min_target = 5    # Minimum obscurity score
    max_target = 95   # Maximum obscurity score
    range_target = max_target - min_target

    df['obscurity_score_normalized'] = min_target + \
        range_target * transformed_scores

    # Apply a second transformation to improve normality
    # Use percentile rank method to create a more uniform distribution first
    percentile_ranks = df['obscurity_score_normalized'].rank(pct=True)

    # Then transform to normal distribution using inverse normal CDF
    from scipy.stats import norm
    df['obscurity_score'] = norm.ppf(percentile_ranks) * 15 + 50

    # Clip values to ensure they stay in 0-100 range
    df['obscurity_score'] = df['obscurity_score'].clip(0, 100)

    # Round to 2 decimal places
    df['obscurity_score'] = df['obscurity_score'].round(2)

    # 6. Create a scaled version (0-100 scale to 0-50 scale)
    df['obscurity_score_scaled'] = (df['obscurity_score'] * 0.5).round(2)

    # 7. Save the results if output file provided
    if output_file:
        # Select relevant columns for output
        output_df = df.copy()

        # Drop intermediate calculation columns
        cols_to_drop = [
            'pageviews_factor', 'awards_count', 'qb_career_value',
            'rb_career_value', 'wr_te_career_value', 'def_career_value',
            'career_value', 'games_factor', 'fantasy_factor',
            'obscurity_score_basic'
        ]

        # Also drop position-specific columns we created
        pos_cols = [col for col in output_df.columns if any(
            f'{pos}_' in col for pos in df['Pos'].unique())]
        cols_to_drop.extend(pos_cols)

        # Drop columns that exist
        cols_to_drop = [
            col for col in cols_to_drop if col in output_df.columns]
        output_df = output_df.drop(columns=cols_to_drop)

        # Save to CSV
        output_df.to_csv(output_file, index=False)

    # 8. Return the dataframe with obscurity scores
    return df


# Example usage
if __name__ == "__main__":
    # Path to your NFL player data
    input_file = "nfl_locked.csv"

    # Path to save results
    output_file = "nfl_players_with_obscurity.csv"

    # Compute obscurity scores
    result_df = compute_obscurity_scores(input_file, output_file)

    # Display results
    print("Top 5 Most Obscure Players:")
    most_obscure = result_df.sort_values(
        'obscurity_score', ascending=False).head(5)
    print(most_obscure[['Player', 'Pos', 'Team', 'G',
          'obscurity_score', 'obscurity_score_scaled']])

    print("\nTop 5 Least Obscure Players:")
    least_obscure = result_df.sort_values('obscurity_score').head(5)
    print(least_obscure[['Player', 'Pos', 'Team', 'G',
          'obscurity_score', 'obscurity_score_scaled']])

    print("\n mid  Obscure Players:")
    mid_obscure = result_df.sort_values('obscurity_score')
    mid_obscure = mid_obscure[800:850]
    print(mid_obscure[['Player', 'Pos', 'Team', 'G',
          'obscurity_score', 'obscurity_score_scaled']])

    print(result_df[800:900])

    # Plot distribution of obscurity scores
    plt.figure(figsize=(12, 6))

    # Create histogram with more granular bins
    n, bins, patches = plt.hist(result_df['obscurity_score'], bins=30,
                                color='skyblue', edgecolor='black', alpha=0.7)

    # Add a normal curve overlay
    mu = result_df['obscurity_score'].mean()
    sigma = result_df['obscurity_score'].std()
    x = np.linspace(0, 100, 100)
    y = ((1 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(-0.5 *
         ((x - mu) / sigma) ** 2)) * len(result_df) * (bins[1] - bins[0])
    plt.plot(x, y, 'r--', linewidth=2)

    plt.title('Distribution of NFL Player Obscurity Scores', fontsize=16)
    plt.xlabel('Obscurity Score (100 = Most Obscure)', fontsize=12)
    plt.ylabel('Number of Players', fontsize=12)
    plt.grid(alpha=0.3)

    # Add descriptive stats as text
    stats_text = f"Mean: {mu:.2f}\nStd Dev: {sigma:.2f}\nMedian: {result_df['obscurity_score'].median():.2f}"
    plt.text(0.75, 0.8, stats_text, transform=plt.gca().transAxes,
             bbox=dict(facecolor='white', alpha=0.8))

    plt.tight_layout()
    plt.savefig('obscurity_distribution.png')
