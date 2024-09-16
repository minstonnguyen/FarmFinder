import { useState } from "react";
import StarRating from "./StarRating";
import "./ProductPopup.css"; // Import CSS for styling

const ProductPopup = ({ product, onSave, onClose }) => {
  const [selectedStarRating, setSelectedStarRating] = useState(0);
  const [selectedType, setSelectedType] = useState(product.name);
  const [selectedOrganic, setSelectedOrganic] = useState("Yes");

  const handleSave = () => {
    const selectedCriteria = {
      stars: selectedStarRating,
      type: selectedType,
      organic: selectedOrganic,
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
      <StarRating
        selectedStarRating={selectedStarRating}
        setSelectedStarRating={setSelectedStarRating}
      />
      {product.types && product.types.length ? (
        <div className="criteria-section">
          <label>Type: </label>
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
          <label>Organic: </label>
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

      <button onClick={handleSave}>Add To Grocery List</button>
    </div>
  );
};

export default ProductPopup;
