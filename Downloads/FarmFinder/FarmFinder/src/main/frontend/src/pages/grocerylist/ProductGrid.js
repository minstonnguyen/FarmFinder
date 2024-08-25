import React, { useState, useEffect } from "react";
import ProductPopup from "./ProductPopup"; // Import the popup component

const ProductGrid = ({ products }) => {
  const [selectedProduct, setSelectedProduct] = useState(null);
  const [productCriteria, setProductCriteria] = useState({});

  useEffect(() => {
    const savedCriteria = JSON.parse(localStorage.getItem("productCriteria"));
    if (savedCriteria) {
      setProductCriteria(savedCriteria);
    }
  }, []);

  useEffect(() => {
    localStorage.setItem("productCriteria", JSON.stringify(productCriteria));
  }, [productCriteria]);

  const handleProductClick = (product) => {
    setSelectedProduct(product);
  };

  const handleSaveCriteria = (productId, criteria) => {
    setProductCriteria((prevCriteria) => ({
      ...prevCriteria,
      [productId]: criteria,
    }));
  };

  const handleClosePopup = () => {
    setSelectedProduct(null);
  };

  return (
    <div className="product-grid">
      {products.map((product) => (
        <div
          key={product.id}
          className="product-item"
          onClick={() => handleProductClick(product)}
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
          product={selectedProduct}
          onSave={handleSaveCriteria}
          onClose={handleClosePopup}
        />
      )}

      <div className="finalGroceryList">
        <h1> Grocery List </h1>
        <pre>{JSON.stringify(productCriteria, null, 2)}</pre>
      </div>
    </div>
  );
};

export default ProductGrid;
