import React from "react";

const LevelBar = ({ xp }) => {
    const currentLevel = Math.floor(xp**(2/3)*0.3);
    const xpMin = Math.floor(((currentLevel)/0.3)**(3/2));
    const xpMax = Math.floor(((currentLevel+1)/0.3)**(3/2));
    const percentageDone = Math.floor(100*(xp-xpMin)/(xpMax-xpMin));

    return (
        <div>
            {xp} XP <br />
            <div className="flex">
            Level {currentLevel} 
            <div className="w-40 h-8 bg-black p-1 mx-3">
                <div className="w-full h-full bg-white">
                    <div className="h-full bg-green-500" style={{ width: `${percentageDone}%` }}></div>
                </div>
            </div> 
            Level {currentLevel+1} <br />
            </div>
            
        </div>
    );
}

export default LevelBar;