import React from "react";

const AnswersList = () => {
  return (
    <div className="p-8 flex">
      <div className="w-full border-4 border-black rounded-lg p-4">
        <ul className="space-y-2 font-pixel text-black">
          <li>
            <div className="p-4">Total</div>
          </li>
          {[1, 2, 3, 4, 5].map((num) => (
            <li key={num}>
              <div className="border-2 border-dashed rounded-lg p-4">{num}</div>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default AnswersList;
