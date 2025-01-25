import React from "react";
import IconContainer from "./IconContainer";

const Task = ({ taskName, xp, content, tag }) => {
  return (
    <div className="task bg-pastel-blue px-8 py-6 rounded-xl">
      <div className="taskHeader flex justify-between content-center mb-3">
        <h2 className="taskName text-2xl font-semibold">{taskName}</h2>
        <h2 className="taskXp text-2xl">{xp} XP</h2>
      </div>
      <p className="taskContent text-lg">{content}</p>
      <div className="taskFooter flex justify-between content-center mt-3 text-lg">
        <p className="taskTag">#{tag}</p>
        <div className="taskBtns flex gap-3">
          <IconContainer>
            <img src="/trashcan.svg" alt="Delete task" />
          </IconContainer>
          <IconContainer>
            <img src="/checkbox.svg" alt="Mark task as complete" />
          </IconContainer>
        </div>
      </div>
    </div>
  );
};

export default Task;
