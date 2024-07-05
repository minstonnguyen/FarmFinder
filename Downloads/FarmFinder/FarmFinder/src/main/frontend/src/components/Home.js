import {React, useRef }from 'react';
import yourImage from '../assets/jasper-garratt-dxJr_1W535E-unsplash.jpg';
function Home()
{
    const windowWidth = useRef(window.innerWidth);
    const windowHeight = useRef(window.innerHeight);
    return(

        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', height: '100vh' }}>
            <nav class = "navbar background">
                <ul class = "nav-list">
                <img src={yourImage} width = {windowWidth} height = {800}alt/>

                </ul>
            </nav>
        </div>
    );
}

export default Home;