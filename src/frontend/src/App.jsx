import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./screens/Home";
import NBA from "./screens/NBA";
import EPL from "./screens/EPL";
import NFL from "./screens/NFL";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/nba" element={<NBA />} />
        <Route path="/epl" element={<EPL />} />
        <Route path="/nfl" element={<NFL />} />
      </Routes>
    </Router>
  );
};

export default App;