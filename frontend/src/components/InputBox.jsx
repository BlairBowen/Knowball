import React, { useState } from "react";

const InputBox = ({ setAnswers }) => {
  const [input, setInput] = useState("");

  const players = [
    "Player 1", "Player 2", "Player 3", "Player 4", "Player 5", "Player 6",
    "Player 7", "Player 8", "Player 9", "Player 10", "Player 11",
    "Player 12", "Player 13", "Player 14", "Player 15", "Player 16",
    "Player 17", "Player 18", "Player 19", "Player 20", "Player 21"
  ];

  // Filter the list of players based on the current state of the input.
  const filteredPlayers = players.filter((player) =>
    player.toLowerCase().includes(input.toLowerCase())
  );

  // Handle submit (when enter key is pressed or button is clicked)
  const handleSubmit = (e) => {
    e.preventDefault();
    if (filteredPlayers.length > 0) {
      setAnswers((prevAnswers) => [...prevAnswers, filteredPlayers[0]]);
      setInput(""); // Clear the input after submitting
    }
  };

  return (
    <div className="p-8 pb-0 flex flex-col">
      <input
        type="text"
        placeholder="ANSWER"
        className="w-full p-4 bg-gray-100 border-4 border-black rounded-lg font-pixel text-black"
        value={input}
        onChange={(e) => setInput(e.target.value)}
        onKeyDown={(e) => e.key === "Enter" && handleSubmit(e)} // Submit on Enter key press
      />

      {/* Show dropdown only if there are matching players */}
      {input !== "" && filteredPlayers.length > 0 && (
        <div className="mt-2 p-4 bg-gray-100 border-4 border-black rounded-lg">
          <ul className="max-h-80 space-y-2 font-pixel text-black overflow-auto">
            {filteredPlayers.map((player) => (
              <li
                className="hover:bg-gray-200 cursor-pointer"
                key={player}
                onClick={() => {
                  setAnswers((prevAnswers) => [
                    ...prevAnswers,
                    player,
                  ]);
                  setInput(""); // Clear input after selection
                }}
              >
                {player}
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default InputBox;
