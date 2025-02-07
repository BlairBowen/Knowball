import React from "react";
import basketball from "../assets/pixel bball.png";
import soccerball from "../assets/pixel sball.png";
import football from "../assets/pixel fball.png";

const TitleCard = () => {
  return (
    <div className="p-8 pb-0 flex justify-between items-center">
      <h1 className="font-tourney text-black tracking-wide">
        Knowball
      </h1>
      <div className="flex space-x-2">
        {[basketball, soccerball, football].map((img, index) => (
          <img
            key={index}
            src={img}
            alt="Pixel sport icon"
            className="w-16 h-16 cursor-pointer"
          />
        ))}
      </div>
    </div>
  );
};

export default TitleCard;
