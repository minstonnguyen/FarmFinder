import logo from "./logo.svg";
import "./App.css";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./components/Home";
import MenuBar from "./components/MenuBar";
import GenerateGroceryList from "./components/GenerateGroceryList";
import ExploreFarms from "./components/ExploreFarms";
import GroceryList from "./pages/grocerylist/GroceryList";
import Layout from "./Layout";
function App() {
  return (
    <Router>
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
