import React, { useState, useEffect } from "react";
import axios from "axios";
import ReactDOM from "react-dom";

import Header from "./Layout/Header";
import Body from "./Body/Body";

const App = () => {
  const [ProjectID, setProjectID] = useState(0);

  function handleChange(projectid) {
    setProjectID(projectid);
  }

  return (
    <React.Fragment>
      <Header onChange={handleChange} />
      <Body ProjectID={ProjectID} key={ProjectID} />
    </React.Fragment>
  );
};

ReactDOM.render(<App />, document.getElementById("app"));
