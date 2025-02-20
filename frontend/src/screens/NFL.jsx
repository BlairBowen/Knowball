import React, { useState } from 'react';
import TitleCard from '../components/TitleCard';
import QuestionNFL from '../components/QuestionNFL';
import InputsNFL from '../components/InputsNFL';
import AnswersNFL from '../components/AnswersNFL';

const NFL = () => {
  // State to hold the list of answers
  const [answers, setAnswers] = useState([]);

  return (
    <div className='min-h-screen w-screen bg-gradient-to-r from-blue-300 to-green-300'>
      <div className='max-w-400 flex flex-col'>
        <TitleCard />
        <QuestionNFL />

        {/* Columnar alignment for input and answer boxes. */}
        <div className='flex'>
          <div className='w-1/2'>
            {/* Pass setAnswers to InputsNFL to handle updates */}
            <InputsNFL setAnswers={setAnswers} />
          </div>
          <div className='w-1/2'>
            {/* Pass answers to AnswersNFL to display them */}
            <AnswersNFL answers={answers} />
          </div>
        </div>
      </div>
    </div>
  );
}

export default NFL;
