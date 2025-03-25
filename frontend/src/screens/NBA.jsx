import React, { useState, useEffect } from 'react'; // Added useEffect import
import TitleCard from '../components/TitleCard';
import QuestionNBA from '../components/QuestionNBA';
import InputsNBA from '../components/InputsNBA';
import AnswersNBA from '../components/AnswersNBA';

const NBA = () => {
  // Define state variables and setters for all data to be fetched from the
  // database.
  const [players, setPlayers] = useState([]);
  const [question, setQuestion] = useState("");
  const [correctAnswers, setCorrectAnswers] = useState([]);
  const [maxScore, setMaxScore] = useState(0);
  
  // These don't come from the database!
  const [score, setScore] = useState(0);
  const [answers, setAnswers] = useState([]);
  const [gameOver, setGameOver] = useState(false);

  // Use an Azure Function to fetch all active players from the database.
  useEffect(() => {
    const fetchPlayers = async () => {
      try {
        const response = await fetch(import.meta.env.VITE_AZURE_NBA_PLAYERS_URL);
        const data = await response.json();
        setPlayers(data);
      } catch (error) {
        console.error("Error fetching player data:", error);
      }
    };
    
    fetchPlayers();
  }, []); // The empty list argument tells the effect to run only once

  // Use an Azure Function to fetch trivia (a question and its answers) from the database.
  useEffect(() => {
    const fetchTrivia = async () => {
      try {
        const response = await fetch(import.meta.env.VITE_AZURE_NBA_QUESTION_URL);
        const data = await response.json();
        setQuestion(data.question); // Save the question
        setCorrectAnswers(data.answers); // Save the answer set
        setMaxScore(data.max); // Save the max possible score
      } catch (error) {
        console.error("Error fetching trivia:", error);
      }
    };
    
    fetchTrivia();
  }, []);

  // Compute a user's score from only their correct answers. This hook will run
  // every time <answers> is updated.
  useEffect(() => {
    // Define variable <newScore>, which is the summation on <answers> when
    // filtered by correctness.
    const newScore = answers
      .filter((answer) => answer.isCorrect)
      .reduce((acc, answer) => acc + answer.score, 0);

    setScore(newScore); // Update the state variable with the summation

    // The game ends when users submit five answers.
    if (answers.length === 5) {
      setGameOver(true);
    }
  }, [answers]); // Trigger whenever answers are updated

  // This function restarts the game by refreshing the page.
  const playAgain = () => {
    window.location.reload();
  };

  // Render the screen while passing the fetched data down to the components
  // within it.
  return (
    <div className='min-h-screen w-screen bg-gradient-to-r from-blue-300 to-green-300'>
      <div className='max-w-400 flex flex-col'>
        <TitleCard />
        <QuestionNBA question={question}/>

        {/* Columnar alignment for input and answer boxes. */}
        <div className='flex'>
          <div className='w-1/2'>
            {/* Pass setAnswers to InputsNBA to handle updates */}
            <InputsNBA
              players={players}
              correctAnswers={correctAnswers}
              setAnswers={setAnswers}
              answers={answers}
            />
          </div>
          <div className='w-1/2'>
            {/* Pass answers to AnswersNBA to display them */}
            <AnswersNBA
              answers={answers}
              score={score}
              maxScore={maxScore}
            />
          </div>
        </div>

        {gameOver && (
          <div className="fixed inset-0 flex items-center justify-center z-50">
              <div className="bg-gray-100 border-4 border-black rounded-lg p-4 w-200 text-black font-pixel !shadow-2xl shadow-orange-400">
                  <h2 className="text-center text-2xl mb-4">Your Score: {score}</h2>
                  <div className="flex justify-between gap-4">
                      <button
                        onClick={() => window.location.href = '/'}
                        className="flex-1 !bg-blue-300 hover:!bg-blue-400 !border-2 !border-black"
                      >
                        Main Menu
                      </button>
                      <button
                        onClick={playAgain}
                        className="flex-1 !bg-green-300 hover:!bg-green-400 !border-2 !border-black"
                      >
                        Play Again
                      </button>
                  </div>
              </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default NBA;
