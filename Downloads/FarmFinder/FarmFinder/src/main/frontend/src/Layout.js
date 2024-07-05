// Layout.js
import React from 'react';
import { Outlet } from 'react-router-dom';

function Layout() {
  return (
    <div>
      <header>
        <h1>FarmFinder</h1>
        <nav>
          <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/GenerateGroceryList">GenerateGroceryList</a></li>
            <li><a href="/ExploreFarms">ExploreFarms</a></li>
          </ul>
        </nav>
      </header>
      <main>
        <Outlet />
      </main>
    </div>
  );
}

export default Layout;
