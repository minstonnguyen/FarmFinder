import React, { useState, useEffect, useRef } from "react";
import FinalGroceryList from "./FinalGroceryList";
import ProductPopup from "./ProductPopup"; // Import the popup component

const ProductGrid = ({ products }) => {
  const [selectedProduct, setSelectedProduct] = useState(null);
  const productRefs = useRef({});
  const [groceryList, setGroceryList] = useState([]);

  const handleAddToGroceryList = (productSelection) => {
    setGroceryList((prevList) => [...prevList, productSelection]);
  };

  const handleRemoveFromGroceryList = (index) => {
    setGroceryList((prevList) => prevList.filter((_, i) => i !== index));
  };

  // OLD IMPLEMENTATION WITH LOCALSTATES
  //
  // const [productCriteria, setProductCriteria] = useState({});
  //
  //useEffect(() => {
  //   const savedCriteria = JSON.parse(localStorage.getItem("productCriteria"));
  //   if (savedCriteria) {
  //     setProductCriteria(savedCriteria);
  //   }
  // }, []);

  // useEffect(() => {
  //   localStorage.setItem("productCriteria", JSON.stringify(productCriteria));
  // }, [productCriteria]);

  const handleProductClick = (product, index) => {
    setSelectedProduct({ product, index });
  };

  // const handleSaveCriteria = (productId, criteria) => {
  //   setProductCriteria((prevCriteria) => ({
  //     ...prevCriteria,
  //     [productId]: criteria,
  //   }));
  // };

  const handleClosePopup = () => {
    setSelectedProduct(null);
  };

  return (
    <div className="product-grid">
      {products.map((product, index) => (
        <div
          key={product.id}
          className="product-item"
          ref={(el) => (productRefs.current[index] = el)}
          onClick={() => handleProductClick(product, index)}
        >
          <img src={product.img} />
          <div className="productName">
            <p>
              <b>{product.name}</b>
            </p>
          </div>
        </div>
      ))}

      {selectedProduct && (
        <ProductPopup
          product={selectedProduct.product}
          productIndex={selectedProduct.index}
          productRefs={productRefs}
          onAddToGroceryList={handleAddToGroceryList}
          // onSave={handleSaveCriteria}
          onClose={handleClosePopup}
        />
      )}

      <FinalGroceryList
        groceryList={groceryList}
        onRemoveFromGroceryList={handleRemoveFromGroceryList}
      />
    </div>
  );
};

export default ProductGrid;
