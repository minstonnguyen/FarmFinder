import React from "react";
import products from "./products";
import ProductGrid from "./ProductGrid";
import "./GroceryList.css";

export const GroceryList = () => {
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
          {/* <Popup trigger={buttonPopup} setTrigger={setButtonPopup}>
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
          </Popup> */}
        </div>
        {/* <div className="products"> */}
        <ProductGrid products={products} />
        {/* {PRODUCTS.map((product) => (
            <Product
              trigger={buttonPopup}
              setTrigger={setButtonPopup}
              data={product}
            />
          ))} */}
        {/* </div> */}
      </div>
    </div>
  );
};

export default GroceryList;
