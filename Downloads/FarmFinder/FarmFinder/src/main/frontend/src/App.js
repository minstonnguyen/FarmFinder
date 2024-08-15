import logo from "./logo.svg";
import "./App.css";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./components/Home";
import MenuBar from "./components/MenuBar";
import GenerateGroceryList from "./components/GenerateGroceryList";
import ExploreFarms from "./components/ExploreFarms";
import Layout from "./Layout";
function App() {
  return (
    <div className="App">
      <div className="logo-container">
        <div className="brand-logo">
          <img src="/logo.png" width={50} height={80} alt="logo" />
        </div>
      </div>
      <header className="App-header">
        <p>FarmFinder</p>
      </header>
      <MenuBar />
    </div>
  );
}

export default App;
