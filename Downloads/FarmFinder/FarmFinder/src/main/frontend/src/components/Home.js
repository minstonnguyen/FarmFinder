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
                    className='home-image'
                    
                />
            </div>
        </div>
    );
}

export default Home;