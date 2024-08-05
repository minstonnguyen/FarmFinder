import React, { useRef, useState } from 'react';

function GenerateGroceryList() {
  const windowWidth = useRef(window.innerWidth);
  const windowHeight = useRef(window.innerHeight);
  
  const [groceryItems, setGroceryItems] = useState([
    {
      name: 'Poultry',
      id: 1, 
      checked: false,
      expanded: false,
      subOptions: [
            {name: 'Chicken', id: 1.1, checked: false},
            {name: 'Duck', id: 1.2, checked: false}, 
            {name: 'Turkey', id: 1.3, checked: false}]
    },
    {
      name: 'Beef',
      id: 2,
      checked: false,
      expanded: false,
      subOptions: [
        {name: 'Retail', id: 2.1, checked: false},
        {name: 'Ground', id: 2.2, checked: false}, 
        {name: 'Whole', id: 2.3, checked: false},
        {name: 'Half', id: 2.4, checked: false},
        {name: 'Quarter', id: 2.5, checked: false}]

    }

  ]);
  
  const handleCheckChange = (itemId, subItemId = null) =>
  {
    setGroceryItems((prevItems) =>
        prevItems.map((item) => {
          if (item.id === itemId) {
            if (subItemId) {
              // Update sub-option checked state
              return {
                ...item,
                subOptions: item.subOptions.map((sub) =>
                  sub.id === subItemId ? { ...sub, checked: !sub.checked } : sub
                )
              };
            } else {
              // Update main item checked state
              return { ...item, checked: !item.checked };
            }
          }
          return item;
        })
      );
  }
  const handleExpandClick = (itemId) => {
    setGroceryItems((prevItems) =>
      prevItems.map((item) =>
        item.id === itemId ? { ...item, expanded: !item.expanded } : item
      )
    );
  };

  
  return(
    <div> 
        <p>Hi this is a test</p>
        <h2>Shopping List
        <ul>
        {groceryItems.map((item) => (
          <li key={item.id}>
            <label>
              <input
                type="checkbox"
                checked={item.checked}
                onChange={() => handleCheckChange(item.id)}
              />
              {item.name}
            </label>
            {item.subOptions && (
              <>
                <button onClick={() => handleExpandClick(item.id)}>
                  {item.expanded ? 'Collapse' : 'Expand'}
                </button>
                {item.expanded && (
                  <ul>
                    {item.subOptions.map((sub) => (
                      <li key={sub.id}>
                        <label>
                          <input
                            type="checkbox"
                            checked={sub.checked}
                            onChange={() => handleCheckChange(item.id, sub.id)}
                          />
                          {sub.name}
                        </label>
                      </li>
                    ))}
                  </ul>
                )}
              </>
            )}
          </li>
        ))}
      </ul>
        </h2>
    </div>
  );
}

export default GenerateGroceryList;
