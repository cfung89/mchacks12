import React from "react";

const LevelBar = ({ xp }) => {
    const currentLevel = Math.floor(xp**(2/3)*0.3);
    const xpMin = Math.floor(((currentLevel)/0.3)**(3/2));
    const xpMax = Math.floor(((currentLevel+1)/0.3)**(3/2));
    const percentageDone = 100*(xp-xpMin)/(xpMax-xpMin);
    const template = `w-[${percentageDone}%] h-full bg-green-500`
    return (
        <div>
            {xp} XP <br />
            <div className="w-24 h-8 bg-black">
                <div className="w-full h-full bg-white">
                    <div className={template}></div>
                </div>
            </div>
            Level = {currentLevel} <br />
            XP needed to reach level {currentLevel+1} = {xpMax} <br />
            XP minimum for level {currentLevel} = {xpMin}
        </div>
    );
}

export default LevelBar;