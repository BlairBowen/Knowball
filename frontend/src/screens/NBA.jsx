import React, { useState } from 'react';
import TitleCard from '../components/TitleCard';
import QuestionNBA from '../components/QuestionNBA';
import InputsNBA from '../components/InputsNBA';
import AnswersNBA from '../components/AnswersNBA';

const NBA = () => {
  // State to hold the list of answers
  const [answers, setAnswers] = useState([]);

  return (
    <div className='min-h-screen w-screen bg-gradient-to-r from-blue-300 to-green-300'>
      <div className='max-w-400 flex flex-col'>
        <TitleCard />
        <QuestionNBA />

        {/* Columnar alignment for input and answer boxes. */}
        <div className='flex'>
          <div className='w-1/2'>
            {/* Pass setAnswers to InputsNBA to handle updates */}
            <InputsNBA setAnswers={setAnswers} />
          </div>
          <div className='w-1/2'>
            {/* Pass answers to AnswersNBA to display them */}
            <AnswersNBA answers={answers} />
          </div>
        </div>
      </div>
    </div>
  );
}

export default NBA;
