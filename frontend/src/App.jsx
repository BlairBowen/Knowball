import React from 'react';
import TitleCard from './components/TitleCard';
import Question from './components/Question';

function App() {
  return (
    <div className="min-h-screen flex-col items-center justify-center bg-gradient-to-r from-blue-300 to-green-300">
      <TitleCard />
      <Question />
    </div>
  );
}

export default App;
