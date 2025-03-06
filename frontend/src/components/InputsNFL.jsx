import React, { useState, useEffect } from "react";

const InputsNFL = ({ players, correctAnswers, setAnswers }) => {
  // Define all state variables, which come bundled with associated setters.
  const [input, setInput] = useState(""); // Initialize to empty string
  const [dropdown, setDropdown] = useState([]); // Initialize to empty list

  // Filter the list of players saved to the players prop based on the contents of state variable <input>. 
  useEffect(() => {
    // Only produce a filtered list when <input> isn't empty.
    if (input) {
      // Use the setter on state variable <dropdown> in order to change it.
      setDropdown(
        players.filter((player) =>
          // This is essentially saying, "if the input exists anywhere in the
          // name of a given player - include that player."
          player.toLowerCase().includes(input.toLowerCase())
        )
      );
    } else {
      setDropdown([]); // If input is empty, clear the dropdown list
    }
  }, [input, players]); // Dependencies on <input> and <players> ensures that
                        // <dropdown> is updated on every relevant change

  // Execute the submit behavior on the event in which the enter key is
  // pressed.
  const submit = (e) => {
    // Block the default form submission behavior, in which the page is
    // reloaded.
    e.preventDefault();

    // Submit by saving <input> as an answer, but only when it's valid. The
    // validity check is that there are players in <dropdown>.
    if (dropdown.length > 0) {
      setAnswers((prevAnswers) => [...prevAnswers, dropdown[0]]);
      setInput(""); // Clear the input field after submission
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
        onKeyDown={(e) => e.key === "Enter" && submit(e)} // Submit on Enter key press
      />

      {input !== "" && dropdown.length > 0 && (
        <div className="mt-2 p-4 bg-gray-100 border-4 border-black rounded-lg">
          <ul className="max-h-80 space-y-2 font-pixel text-black overflow-auto">
            {dropdown.map((player) => (
              <li
                className="hover:bg-gray-200 cursor-pointer"
                key={player}
                onClick={() => {
                  setAnswers((prevAnswers) => [...prevAnswers, player]);
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

export default InputsNFL;
