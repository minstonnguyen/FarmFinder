import React from "react";
import "./popup.css";

export const Popup = (props) => {
  return props.trigger ? (
    <div className="popup">
      <div className="popup-inner">
        <button className="closeButton" onClick={() => props.setTrigger(false)}>
          close
        </button>

        {props.children}
      </div>
    </div>
  ) : (
    ""
  );
};

export default Popup;
