import React from "react";

const AnswersList = ({ answers }) => {
  // Number of answer slots
  const totalSlots = 5;

  return (
    <div className="p-8 flex">
      <div className="w-full border-4 border-black rounded-lg p-4">
        <ul className="space-y-2 font-pixel text-black">
          <li>
            <div className="p-4">Total</div>
          </li>
          {/* Render answer slots */}
          {[...Array(totalSlots)].map((_, index) => (
            <li key={index}>
              <div className="border-2 border-dashed rounded-lg p-4">
                {/* Render the answer or a blank space if the slot is not filled */}
                {answers[index] || "___"}
              </div>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default AnswersList;
