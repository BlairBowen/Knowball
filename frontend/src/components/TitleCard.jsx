import React from "react";
import { Link } from "react-router-dom";
import basketball from "../assets/pixel bball.png";
import soccerball from "../assets/pixel sball.png";
import football from "../assets/pixel fball.png";

const TitleCard = () => {
  return (
    <div className="p-8 pb-0 flex justify-between items-center h-20">
      {/* Left-Aligned Title */}
      <h1 className="font-tourney text-black tracking-wide">
        Knowball
      </h1>

      {/* Right-Aligned Navigation Icons */}
      <div className="flex space-x-4">
        <Link to="/nba">
          <img
            src={basketball}
            alt="Pixel basketball icon"
            className="w-16 h-16 cursor-pointer"
          />
        </Link>
        <Link to="/epl">
          <img
            src={soccerball}
            alt="Pixel soccer icon"
            className="w-16 h-16 cursor-pointer"
          />
        </Link>
        <Link to="/nfl">
          <img
            src={football}
            alt="Pixel football icon"
            className="w-16 h-16 cursor-pointer"
          />
        </Link>
      </div>
    </div>
  );
};

export default TitleCard;
