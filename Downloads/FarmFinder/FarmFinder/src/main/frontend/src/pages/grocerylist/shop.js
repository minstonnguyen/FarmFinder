import React from "react";
import { PRODUCTS } from "./products";
import { Product } from "./product";
import { Popup } from "./popup";
import "./shop.css";
import { useState } from "react";

export const Shop = () => {
  const [buttonPopup, setButtonPopup] = useState(false);
  return (
    <div className="shop">
      <div className="shopTitle">
        <h1> Grocery List Generator</h1>
      </div>
      <div className="filterBox">
        <div className="filter">
          <div className="filterContent">Dairy</div>
        </div>
        <div className="filter">
          <div className="filterContent">Beef</div>
        </div>
        <div className="filter">
          <div className="filterContent">Soy</div>
        </div>
      </div>
      <div className="shopPage">
        <div className="leftpanel">
          <Popup trigger={buttonPopup} setTrigger={setButtonPopup}>
            <h1> Select Criteria </h1>
            <div>
              <input type="checkbox" />
              Criteria 1
            </div>
            <div>
              <input type="checkbox" />
              Criteria 2
            </div>
            <div>
              <input type="checkbox" />
              Criteria 3
            </div>
          </Popup>
        </div>
        <div onClick={() => setButtonPopup(true)} className="products">
          {PRODUCTS.map((product) => (
            <Product data={product} />
          ))}
        </div>
        <div className="groceryList">
          <h1> Grocery List </h1>
        </div>
      </div>
    </div>
  );
};