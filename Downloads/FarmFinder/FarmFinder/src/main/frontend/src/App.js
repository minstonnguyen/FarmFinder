import logo from './logo.svg';
import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './components/Home'
import GenerateGroceryList from './components/GenerateGroceryList'
import ExploreFarms from './components/ExploreFarms'
import Layout from './Layout';

function App() {
  return (
    <Router>
      <Routes>
        <Route path = "/" element = {<Layout />}>
          <Route index element={<Home />} />
          <Route path="/about" element={<GenerateGroceryList />} />
          <Route path="/contact" element={<ExploreFarms />} />
        </Route>
      </Routes>
    </Router>
  );
}

export default App;
