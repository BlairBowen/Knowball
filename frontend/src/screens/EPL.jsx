import React, { useState, useEffect } from 'react'; // Added useEffect import
import TitleCard from '../components/TitleCard';
import QuestionEPL from '../components/QuestionEPL';
import InputsEPL from '../components/InputsEPL';
import AnswersEPL from '../components/AnswersEPL';

const EPL = () => {
  // Define state variables and setters for all data to be fetched from the
  // database.
  const [players, setPlayers] = useState([]);
  const [question, setQuestion] = useState("");
  const [correctAnswers, setCorrectAnswers] = useState([]);
  
  // These don't come from the database!
  const [score, setScore] = useState(0);
  const [answers, setAnswers] = useState([]);

  // Use an Azure Function to fetch all active players from the database.
  useEffect(() => {
    const fetchPlayers = async () => {
      try {
        const response = await fetch(import.meta.env.VITE_AZURE_EPL_PLAYERS_URL);
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
        const response = await fetch(import.meta.env.VITE_AZURE_EPL_QUESTION_URL);
        const data = await response.json();
        setQuestion(data.question); // Save the question
        setCorrectAnswers(data.answers); // Save the answer set
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
  }, [answers]); // Trigger whenever answers are updated

  // Render the screen while passing the fetched data down to the components
  // within it.
  return (
    <div className='min-h-screen w-screen bg-gradient-to-r from-blue-300 to-green-300'>
      <div className='max-w-400 flex flex-col'>
        <TitleCard />
        <QuestionEPL question={question}/>

        {/* Columnar alignment for input and answer boxes. */}
        <div className='flex'>
          <div className='w-1/2'>
            {/* Pass setAnswers to InputsEPL to handle updates */}
            <InputsEPL
              players={players}
              correctAnswers={correctAnswers}
              setAnswers={setAnswers}
              answers={answers}
            />
          </div>
          <div className='w-1/2'>
            {/* Pass answers to AnswersEPL to display them */}
            <AnswersEPL answers={answers} score={score} />
          </div>
        </div>
      </div>
    </div>
  );
}

export default EPL;
