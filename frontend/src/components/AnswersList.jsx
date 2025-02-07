import React from "react";

const TitleCard = () => {
  return (
    <div className="p-8 pb-0 flex justify-left">
        <div className="w-full border-4 border-black rounded-lg p-2 md:p-4">
            <ul className="font-pixel">
                <li className="pb-2">
                    <div className="p-1 md:p-2">Total</div>
                </li>
                <li className="pb-2">
                    <div className="border-2 border-dashed rounded-lg p-1 md:p-2">1</div>
                </li>
                <li className="pb-2">
                    <div className="border-2 border-dashed rounded-lg p-1 md:p-2">2</div>
                </li>
                <li className="pb-2">
                    <div className="border-2 border-dashed rounded-lg p-1 md:p-2">3</div>
                </li>
                <li className="pb-2">
                    <div className="border-2 border-dashed rounded-lg p-1 md:p-2">4</div>
                </li>
                <li className="pb-2">
                    <div className="border-2 border-dashed rounded-lg p-1 md:p-2">5</div>
                </li>
            </ul>
        </div>
    </div>
  );
};

export default TitleCard;
