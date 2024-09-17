import React from "react";

const FinalGroceryList = ({ groceryList, onRemoveFromGroceryList }) => {
  return (
    <div className="finalGroceryList">
      <div className="insideFGL">
        <div className="FGLTitle"> Grocery List </div>
        <div className="listOfGroceries">
          {groceryList.length > 0 ? (
            <ul>
              {groceryList.map((item, index) => (
                <li key={index} className="grocery-list-item">
                  <div className="grocery-details">
                    <p>
                      <strong>{item.productName}</strong> -
                      {item.selectedType && ` Type: ${item.selectedType},`}
                      {item.selectedStarRating &&
                        ` Rating: ${item.selectedStarRating} stars,`}
                      {item.selectedOrganic && ` Organic`}
                    </p>
                  </div>
                  <button
                    className="removeButton"
                    onClick={() => onRemoveFromGroceryList(index)}
                  >
                    &times;
                  </button>
                </li>
              ))}
            </ul>
          ) : (
            <p>Your grocery list is empty.</p>
          )}
        </div>
        <button className="finalizeButton">Finalize Grocery List</button>
      </div>
    </div>
  );
};

export default FinalGroceryList;
