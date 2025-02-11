import React from "react";

const InputBox = () => {
  return (
    <div className="p-8 pb-0 flex flex-col">
        <input
            type="text"
            placeholder="ANSWER"
            className="w-full p-4 bg-gray-100 border-4 border-black rounded-lg font-pixel text-black"
        />

        {/* In the future, this dropdown component will be dynamically rendered! */}
        <div className="mt-2 p-4 bg-gray-100 border-4 border-black rounded-lg">
            <ul className="max-h-80 space-y-2 font-pixel text-black overflow-auto">
                {["Player 1", "Player 2", "Player 3", "Player 4", "Player 5", "Player 6", "Player 7", "Player 8", "Player 9", "Player 10", "Player 11", "Player 12", "Player 13", "Player 14", "Player 15", "Player 16", "Player 17", "Player 18", "Player 19", "Player 20"].map((athlete) => (
                    <li key={athlete} className="hover:bg-gray-200 cursor-pointer">
                        {athlete}
                    </li>
                ))}
            </ul>
        </div>
    </div>
  );
};

export default InputBox;
