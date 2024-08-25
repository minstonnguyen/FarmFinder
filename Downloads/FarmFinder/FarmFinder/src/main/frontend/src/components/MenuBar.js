import React from 'react';
import { Link } from 'react-router-dom'
const MenuBar = () => {
  return (
    <nav className="menu-bar">
      <ul>
      <li><Link to="/ExploreFarms">Explore Farms</Link></li>
        <li><Link to="/GenerateGroceryList">Premium Organic Grocery List Generator</Link></li>
        <li><Link to="#resources">Resources</Link></li>
        <li><Link to="#about">About</Link></li>
        <li><Link to="#contact">Contact Us</Link></li>
        <li><Link to="#login">Login</Link></li>
        
      </ul>
    </nav>
  );
};

export default MenuBar;
