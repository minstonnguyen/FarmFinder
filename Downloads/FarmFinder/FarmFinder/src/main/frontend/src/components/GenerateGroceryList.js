import React from "react";
import products from "../pages/grocerylist/products";
import ProductGrid from "../pages/grocerylist/ProductGrid";
import "../pages/grocerylist/grocerylist.css";

export const GenerateGroceryList = () => {
  return (
    <div className="shop">
      <div className="shopTitle">
        <h1> Grocery List Generator</h1>
      </div>
      {/* <div className="instructions">
        Select the product you want to buy, choose the desired criteria from the
        popup window, and add it to your grocery list. Once you've added all
        your products to your grocery list, click finalize to generate a list of
        all available farms for the products on your grocery list.
      </div> */}
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

export default GenerateGroceryList;
