import React from 'react';
import TitleCard from './components/TitleCard';
import QuestionBox from './components/QuestionBox';
import InputBox from './components/InputBox';
import AnswersList from './components/AnswersList';

function App() {
  return (
    <div className="min-h-screen flex-col items-center justify-center bg-gradient-to-r from-blue-300 to-green-300">
      <TitleCard />
      <QuestionBox />

      {/* Columnar alignment for input and answer boxes. */}
      <div className="flex w-full">
        <div className="w-1/2">
          <InputBox />
        </div>
        <div className="w-1/2">
          <AnswersList />
        </div>
      </div>
    </div>
  );
}

export default App;
