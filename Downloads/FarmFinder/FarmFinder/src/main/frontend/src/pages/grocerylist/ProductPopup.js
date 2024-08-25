import { useState } from "react";
import StarRating from "./StarRating";
import "./ProductPopup.css"; // Import CSS for styling

const ProductPopup = ({ product, onSave, onClose }) => {
  const [selectedStarRating, setSelectedStarRating] = useState(0);
  const [selectedType, setSelectedType] = useState(product.name);

  const handleSave = () => {
    const selectedCriteria = {
      stars: selectedStarRating,
      type: selectedType,
    };
    onSave(product.id, selectedCriteria);
    onClose();
  };

  return (
    <div className={`product-popup ${product ? "open" : ""}`}>
      <button className="close-btn" onClick={onClose}>
        &times;
      </button>
      <h2>{product.name}</h2>
      <p>Minimum Star Rating: </p>
      {/* <StarRating
        selectedStarRating={selectedStarRating}
        setSelectedStarRating={setSelectedStarRating}
      /> */}
      {product.name == "Milk" ? (
        <div className="criteria-section">
          <label>Type:</label>
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

      <button onClick={handleSave}>Add To Grocery List</button>
    </div>
  );
};

export default ProductPopup;
