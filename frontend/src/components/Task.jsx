import React from "react";
import { BsCheckCircleFill } from "react-icons/bs";

const Task = ({ taskName, xp, content, tag }) => {
  return (
    <div className="task bg-pastel-blue px-8 py-6 rounded-md">
      <h2 className="taskName text-xl font-semibold">{taskName}</h2>
      <h3 className="taskXp">{xp} XP</h3>
      <p className="taskContent">{content}</p>
      <div className="taskFooter flex justify-between">
        <p className="taskTag">#{tag}</p>
        <div className="taskCheckbox">
          <BsCheckCircleFill />
        </div>
      </div>
    </div>
  );
};

export default Task;
