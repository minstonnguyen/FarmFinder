import logo from "./assets/logo.png";
import "./App.css";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { Link } from 'react-router-dom'
import Home from "./components/Home";
import MenuBar from "./components/MenuBar";
import GenerateGroceryList from "./components/GenerateGroceryList";
import ExploreFarms from "./components/ExploreFarms";
import GroceryList from "./components/GenerateGroceryList";
import Resources from "./components/Resources";
import ContactUs from "./components/ContactUs";
import About from "./components/About";
import Login from "./components/Login";

import Layout from "./Layout";
function App() {
  return (
    <Router>
      <div className="App">
        <header className="App-header">
          <div className="logo-container">
            <div className="brand-logo">
              <img src={logo} width={125} height={200} alt="logo" />
            </div>
            <p className="brand-name">
              <Link to="/" className="brand-name-link">FarmFinder</Link>
            </p>


          </div>

        </header>
        <MenuBar />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/ExploreFarms" element={<ExploreFarms />} />
          <Route path="/GenerateGroceryList" element={<GroceryList />} />
          <Route path="/Resources" element={<Resources />} />
          <Route path="/About" element={<About />} />
          <Route path="/ContactUs" element={<ContactUs />} />
          <Route path="/Login" element={<Login />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
