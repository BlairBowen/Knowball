import React, { useState, useEffect } from "react";

const InputsEPL = ({ players, correctAnswers, setAnswers, answers }) => {
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
          // Access player name as player[0], which is the name in the tuple.
          player[0].toLowerCase().includes(input.toLowerCase())
        )
      );
    } else {
      setDropdown([]); // If input is empty, clear the dropdown list
    }
  }, [input, players]); // Dependencies on <input> and <players> ensures that
                        // <dropdown> is updated on every relevant change

  // Execute the submit behavior on the event in which the enter key is pressed.
  const submit = (e) => {
    // Block the default form submission behavior, in which the page is reloaded.
    e.preventDefault();

    // Submit by saving <input> as an answer, but only when it's valid. The
    // validity check is that there are players in <dropdown>.
    if (dropdown.length > 0) {
      // Save the submission to a local variable for ease of use.
      const selectedPlayer = dropdown[0];

      // Check if the submission is a duplicate before continuing.
      if (answers.some(answer => answer.player === selectedPlayer[0])) {
        return;
      }

      // Define a correctness property for the submission.
      const isCorrect = correctAnswers.includes(selectedPlayer[0]);

      // Add the submission to the list of answers with its player name,
      // obscurity score, and correctness property.
      setAnswers((prevAnswers) => [
        ...prevAnswers,
        { player: selectedPlayer[0], score: selectedPlayer[1], isCorrect }
      ]);

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
                key={player[0]} // Use player name as the key
                onClick={() => {
                  // Clicking is a separate means of submitting an answer. So,
                  // we must redefine previous event handling behavior. 
                  const selectedPlayer = player;
                  if (answers.some(answer => answer.player === selectedPlayer[0])) {
                    return;
                  }
                  const isCorrect = correctAnswers.includes(selectedPlayer[0]);
                  setAnswers((prevAnswers) => [
                    ...prevAnswers,
                    { player: selectedPlayer[0], score: selectedPlayer[1], isCorrect }
                  ]);
                  setInput("");
                }}
              >
                {player[0]} {/* Display player name */}
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default InputsEPL;
