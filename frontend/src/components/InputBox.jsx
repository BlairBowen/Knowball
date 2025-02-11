import React, { useState } from "react";

const InputBox = () => {
    // Initialize state and its setter. State, in this case, only monitors the
    // contents of the input field.
    const [input, setInput] = useState(""); // Initial state is empty!

    const players = [
        "Player 1", "Player 2", "Player 3", "Player 4", "Player 5", "Player 6",
        "Player 7", "Player 8", "Player 9", "Player 10", "Player 11",
        "Player 12", "Player 13", "Player 14", "Player 15", "Player 16",
        "Player 17", "Player 18", "Player 19", "Player 20", "Player 21"
    ];

    // Filter the list of players based on the current state of the input. The
    // use of <includes()> supports a match on any substring.
    const filteredPlayers = players.filter((player) =>
        player.toLowerCase().includes(input.toLowerCase())
    );

    // Handle the event in which a user clicks on a player from the list of
    // players.
    const handleClickOnPlayer = (player) => {
        setInput(player);
    };
    
    return (
        <div className="p-8 pb-0 flex flex-col">
            <input
                type="text"
                placeholder="ANSWER"
                className="w-full p-4 bg-gray-100 border-4 border-black rounded-lg font-pixel text-black"
                value={input}
                onChange={(e) => setInput(e.target.value)}
            />

            {/* Show dropdown only if there are matching players */}
            {input !== "" && filteredPlayers.length > 0 && (
                <div className="mt-2 p-4 bg-gray-100 border-4 border-black rounded-lg">
                    <ul className="max-h-80 space-y-2 font-pixel text-black overflow-auto">
                        {filteredPlayers.map((player) => (
                            <li
                                className="hover:bg-gray-200 cursor-pointer"
                                key={player}
                                onClick={() => handleClickOnPlayer(player)}
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