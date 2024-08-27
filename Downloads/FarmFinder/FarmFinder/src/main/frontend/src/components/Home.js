import {React, useRef }from 'react';
import yourImage from '../assets/jasper-garratt-dxJr_1W535E-unsplash.jpg';
import { BrowserRouter as Router, Routes, Route, Switch } from 'react-router-dom';

function Home()
{
    const windowWidth = useRef(window.innerWidth);
    const windowHeight = useRef(window.innerHeight);
    return(

        <div className="home-container">
            <div className="image-container">
                <img 
                    src={yourImage} 
                    width={windowWidth.current} 
                    height={800} 
                    alt="Your Image" 
                    style={{ width: '100%', height: 'auto', objectFit: 'cover' }} 
                />
            </div>
        </div>
    );
}

export default Home;