import { useState, useEffect } from "react";
import StarRating from "./StarRating";
import "./ProductPopup.css"; // Import CSS for styling

const ProductPopup = ({
  product,
  productIndex,
  productRefs,
  // onSave,
  onAddToGroceryList,
  onClose,
}) => {
  const productElement = productRefs.current[productIndex];
  const [popupPosition, setPopupPosition] = useState({ top: 100, left: 100 });

  const [selectedStarRating, setSelectedStarRating] = useState(0);
  const [selectedType, setSelectedType] = useState(product.name);
  const [selectedOrganic, setSelectedOrganic] = useState("Yes");

  const handleAddToGroceryList = () => {
    const selectedCriteria = {
      productId: product.id,
      productName: product.name,
      selectedStarRating,
      selectedType,
      selectedOrganic,
    };
    onAddToGroceryList(selectedCriteria);
    onClose();
  };

  useEffect(() => {
    if (productElement) {
      const rect = productElement.getBoundingClientRect();
      const leftPosition = rect.left;
      const topPosition = rect.top + window.scrollY;
      setPopupPosition({
        top: topPosition,
        left: leftPosition > 0 ? leftPosition : 10, // Prevent going off-screen
      });
      console.log(topPosition);
    }
  }, [productElement]);

  // const handleSave = () => {
  //   const selectedCriteria = {
  //     stars: selectedStarRating,
  //     type: selectedType,
  //     organic: selectedOrganic,
  //   };
  //   onSave(product.id, selectedCriteria);
  //   onClose();
  // };

  return (
    <div
      className="product-popup"
      style={{
        position: "absolute",
        top: `${popupPosition.top}px`,
        left: `${popupPosition.left}px`,
        zIndex: 100,
        backgroundColor: "#fff",
        border: "1px solid #ccc",
      }}
    >
      <div className="product-popup-interior">
        <button className="close-btn" onClick={onClose}>
          &times;
        </button>
        <h2 style={{ marginTop: "30px", fontFamily: "FairfieldDisplay" }}>
          {product.name}
        </h2>
        {/* <p>Minimum Star Rating: </p> */}
        <StarRating
          selectedStarRating={selectedStarRating}
          setSelectedStarRating={setSelectedStarRating}
        />
        {product.types && product.types.length ? (
          <div className="criteria-section">
            <select
              value={selectedType}
              onChange={(e) => setSelectedType(e.target.value)}
            >
              <option value="">Select Type</option>
              {product.types.map((type) => (
                <option key={type} value={type}>
                  {type}
                </option>
              ))}
            </select>
          </div>
        ) : (
          ""
        )}
        {product.organic && product.organic.length ? (
          <div className="criteria-section">
            <select
              value={selectedType}
              onChange={(e) => setSelectedOrganic(e.target.value)}
            >
              <option value="">Yes</option>
              {product.organic.map((organic) => (
                <option key={organic} value={organic}>
                  {organic}
                </option>
              ))}
            </select>
          </div>
        ) : (
          ""
        )}
      </div>
      <button
        className="addToListButton"
        style={{ marginTop: "20px" }}
        onClick={handleAddToGroceryList}
        // onClick={handleSave}
      >
        Add To Grocery List
      </button>
    </div>
  );
};

export default ProductPopup;
