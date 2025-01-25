import React from "react";
import { useState } from "react";

const IconContainer = ({ children }) => {
  const [clicked, setClicked] = useState(false);

  return (
    <div
      className="flex content-center duration-250 hover:cursor-pointer hover:invert"
      onClick={() => setClicked(true)}
    >
      {children}
    </div>
  );
};

export default IconContainer;
