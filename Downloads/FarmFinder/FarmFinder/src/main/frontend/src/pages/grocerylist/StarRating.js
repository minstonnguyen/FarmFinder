import React, { useState } from "react";
import { FaStar } from "react-icons/fa";

const StarRating = ({ selectedStarRating, setSelectedStarRating }) => {
  //   const [rating, setRating] = useState(null);

  const [hover, setHover] = useState(null);

  return (
    <div>
      {[...Array(5)].map((star, i) => {
        const ratingValue = i + 1;

        return (
          <label>
            <input
              type="radio"
              name="rating"
              value={ratingValue}
              //   onClick={() => setRating(ratingValue)}
              onClick={() => setSelectedStarRating(ratingValue)}
            />
            <FaStar
              className="star"
              color={
                ratingValue <= (hover || selectedStarRating)
                  ? "#ffc107"
                  : "e4e5e9"
              }
              size={25}
              onMouseEnter={() => setHover(ratingValue)}
              onMouseLeave={() => setHover(null)}
            />
          </label>
        );
      })}
    </div>
  );
};

export default StarRating;
