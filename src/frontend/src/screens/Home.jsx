import React from "react";
import { Link } from "react-router-dom";
import basketball from "../assets/pixel bball.png";
import soccerball from "../assets/pixel sball.png";
import football from "../assets/pixel fball.png";

const Home = () => {
  return (
    <div className="min-h-screen w-screen bg-gradient-to-r from-blue-300 to-green-300 flex flex-col">
      <h1 className="p-8 font-tourney text-black tracking-wide">Knowball</h1>

      {/* Centers icons while allowing responsiveness */}
      <div className="flex flex-grow justify-center items-center">
        <div className="flex flex-col md:flex-row space-y-8 md:space-y-0 md:space-x-16">
          <Link to="/nba">
            <img
              src={basketball}
              alt="Pixel basketball icon"
              className="w-32 h-32 cursor-pointer"
            />
          </Link>
          <Link to="/epl">
            <img
              src={soccerball}
              alt="Pixel soccer icon"
              className="w-32 h-32 cursor-pointer"
            />
          </Link>
          <Link to="/nfl">
            <img
              src={football}
              alt="Pixel football icon"
              className="w-32 h-32 cursor-pointer"
            />
          </Link>
        </div>
      </div>
    </div>
  );
};

export default Home;
