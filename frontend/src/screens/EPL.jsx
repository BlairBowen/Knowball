import React, { useState } from 'react';
import TitleCard from '../components/TitleCard';
import QuestionBox from '../components/QuestionBox';
import InputBox from '../components/InputBox';
import AnswersList from '../components/AnswersList';

const EPL = () => {
  // State to hold the list of answers
  const [answers, setAnswers] = useState([]);

  return (
    <div className='min-h-screen w-screen bg-gradient-to-r from-blue-300 to-green-300'>
      <div className='max-w-400 flex flex-col'>
        <TitleCard />
        <QuestionBox />

        {/* Columnar alignment for input and answer boxes. */}
        <div className='flex'>
          <div className='w-1/2'>
            {/* Pass setAnswers to InputBox to handle updates */}
            <InputBox setAnswers={setAnswers} />
          </div>
          <div className='w-1/2'>
            {/* Pass answers to AnswersList to display them */}
            <AnswersList answers={answers} />
          </div>
        </div>
      </div>
    </div>
  );
}

export default EPL;
