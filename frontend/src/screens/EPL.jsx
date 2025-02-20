import React, { useState } from 'react';
import TitleCard from '../components/TitleCard';
import QuestionEPL from '../components/QuestionEPL';
import InputsEPL from '../components/InputsEPL';
import AnswersEPL from '../components/AnswersEPL';

const EPL = () => {
  // State to hold the list of answers
  const [answers, setAnswers] = useState([]);

  return (
    <div className='min-h-screen w-screen bg-gradient-to-r from-blue-300 to-green-300'>
      <div className='max-w-400 flex flex-col'>
        <TitleCard />
        <QuestionEPL />

        {/* Columnar alignment for input and answer boxes. */}
        <div className='flex'>
          <div className='w-1/2'>
            {/* Pass setAnswers to InputsEPL to handle updates */}
            <InputsEPL setAnswers={setAnswers} />
          </div>
          <div className='w-1/2'>
            {/* Pass answers to AnswersEPL to display them */}
            <AnswersEPL answers={answers} />
          </div>
        </div>
      </div>
    </div>
  );
}

export default EPL;
