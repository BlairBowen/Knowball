import React from "react";

const QuestionEPL = ({ question }) => {
  return (
    <div className="p-8 pb-0 flex justify-center">
      <div className="w-full bg-gray-100 border-4 border-black rounded-lg p-4">
        <p className="font-pixel text-black">
          QUESTION: {question || "Loading..."}
        </p>
      </div>
    </div>
  );
};

export default QuestionEPL;
