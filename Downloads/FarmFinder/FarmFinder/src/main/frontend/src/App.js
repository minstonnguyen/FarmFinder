import logo from "./assets/logo.png";
import "./App.css";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./components/Home";
import MenuBar from "./components/MenuBar";
import GenerateGroceryList from "./components/GenerateGroceryList";
import ExploreFarms from "./components/ExploreFarms";
import GroceryList from "./components/GenerateGroceryList";
import Layout from "./Layout";
function App() {
  return (
    <Router>
      <div className="App">
        <header className="App-header">
          <div className="logo-container">
            <div className="brand-logo">
              <img src={logo}width={125} height={200} alt="logo" />
            </div>
            <p className = "brand-name">FarmFinder</p>
          </div>
          
        </header>
        <MenuBar />
        <Routes>
          <Route path="/ExploreFarms" element={<ExploreFarms />} />
          <Route path="/GenerateGroceryList" element={<GroceryList />} />
          <Route path="/" element={<Home />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
