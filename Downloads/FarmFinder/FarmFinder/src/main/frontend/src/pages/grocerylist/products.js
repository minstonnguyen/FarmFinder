import egg from "./product-images/egg.png";
import milk from "./product-images/milk.png";
import butter from "./product-images/butter.png";
import cheese from "./product-images/cheese.jpg";
import cream from "./product-images/cream.png";
import icecream from "./product-images/icecream.png";
import chocolate from "./product-images/chocolate.png";
import beef from "./product-images/beef.png";
import petfood from "./product-images/petfood.png";
import poultry from "./product-images/poultry.png";
import yogurt from "./product-images/yogurt.png";
import plantbasedbeverages from "./product-images/plantbasedbev.png";
import snackbar from "./product-images/snackbar.png";
import cottagecheese from "./product-images/cottagecheese.png";
import cereal from "./product-images/cereal.png";
import tofu from "./product-images/tofu.png";
import soy from "./product-images/soy.png";

const products = [
  {
    id: 1,
    name: "Eggs",
    img: egg,
  },
  {
    id: 2,
    name: "Milk",
    img: milk,
    types: [
      "Chocolate milk",
      "Raw milk",
      "Condensed milk",
      "A2 milk",
      "Evaporated milk",
      "Goat milk",
      "Lactose free milk",
      "Kefir",
      "Infant formula",
      "Vat pasteurized milk",
      "Buttermilk",
      "Biodynamic Milk",
    ],
  },
  {
    id: 3,
    name: "Butter",
    img: butter,
    types: ["Ghee"],
  },
  {
    id: 4,
    name: "Cheese",
    img: cheese,
    types: ["Paneer", "Cream cheese", "Goat cheese", "Raw cheese"],
  },
  {
    id: 5,
    name: "Cream",
    img: cream,
    types: ["Sour cream", "Whipped Cream"],
  },
  {
    id: 6,
    name: "Ice Cream",
    img: icecream,
  },
  {
    id: 7,
    name: "Chocolate",
    img: chocolate,
  },
  {
    id: 8,
    name: "Beef",
    img: beef,
    types: [
      "Elk",
      "Buffalo",
      "Venison",
      "Bison",
      "Retail Cuts",
      "Bulk",
      "Ground",
      "Sausages",
      "Hot Dogs",
      "Veal",
      "Live",
      "Jerky",
      "Organs",
      "Beef bacon",
      "Wholesale",
      "Half",
      "Quarter",
      "Eigths",
      "Custom",
      "Bones",
    ],
  },
  {
    id: 9,
    name: "Pet Food",
    img: petfood,
    types: ["Poultry", "Beef"],
  },
  {
    id: 10,
    name: "Poultry",
    img: poultry,
    types: [
      "Chicken",
      "Turkey",
      "Duck",
      "Ostrich",
      "Kosher",
      "Soy free",
      "Sausage",
      "Canned chicken",
      "Processed meat",
    ],
  },
  {
    id: 11,
    name: "Yogurt",
    img: yogurt,
    types: ["Frozen Yogurt", "Greek Yogurt", "Soy Yogurt", "Skyr"],
  },
  {
    id: 12,
    name: "Plant Based Beverages",
    img: plantbasedbeverages,
    types: [
      "Soy",
      "Almond",
      "Oat",
      "Pistachio/Almond",
      "Cashew",
      "Banana",
      "Coconut",
      "Rice",
      "Hazelnut",
      "Blend",
      "Hemp",
      "Quinoa",
      "Flax",
      "Macadamia",
      "Pea",
    ],
    organic: ["No"],
  },
  {
    id: 13,
    name: "Snack Bar",
    img: snackbar,
    organic: ["No", "Made with organic ingredients"],
  },
  {
    id: 14,
    name: "Cottage Cheese",
    img: cottagecheese,
    organic: ["No"],
  },
  {
    id: 15,
    name: "Cereal",
    img: cereal,
  },
  {
    id: 16,
    name: "Tofu",
    img: tofu,
    types: [
      "Tofu Ravioli",
      "Tofu Veggie Patties",
      "Tofu Hot Dogs",
      "Tofurky",
      "Tofu Spreads",
      "Tofu Salad (No Egg)",
    ],
  },
  {
    id: 17,
    name: "Other Soy Products",
    img: soy,
    types: [
      "Soymilk",
      "Soybeans",
      "Soybean oil",
      "Soy Sauce",
      "Ponzu",
      "Edamame",
      "Tempeh",
      "Tempeh Superburgers",
      "Natto",
      "Miso",
      "Soy Beverages",
      "Soy Dairy products",
      "Sandwiches",
      "Noodles",
      "Burgers",
      "Meatless Sausage",
      "Mushroom Pate",
    ],
  },
];

export default products;
