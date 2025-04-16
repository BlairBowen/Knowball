import React from "react";

const AnswersEPL = ({ answers, score, maxScore }) => {
  // Number of answer slots
  const totalSlots = 5;

  return (
    <div className="p-8 flex">
      <div className="w-full border-4 border-black rounded-lg p-4">
        <ul className="space-y-2 font-pixel text-black">
          <li>
            <div className="p-4">
              Score: {Math.round(score)}<br />
              Maximum: {Math.round(maxScore)}
            </div>
          </li>
          {/* Render answer slots */}
          {[...Array(totalSlots)].map((_, index) => {
            const answer = answers[index];

            return (
              <li key={index}>
                <div
                  className={`border-2 border-dashed rounded-lg p-4 ${
                    answer
                      ? answer.isCorrect
                        ? "" // Correct answers remain black
                        : "text-red-500" // Incorrect answers in red
                      : ""
                  }`}
                >
                  {/* Render the answer or a blank space if the slot is not filled */}
                  {answer
                    ? answer.isCorrect
                      ? `${answer.player} +${Math.round(answer.score)}` // Round score
                      : answer.player
                    : "___"}
                </div>
              </li>
            );
          })}
        </ul>
      </div>
    </div>
  );
};

export default AnswersEPL;
