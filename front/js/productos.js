const Products = [
  {
    id: 1,
    name: "Marvel legacy",
    price: "120.000",
    description: "Marvel legacy",
    image: "images/marvel-ironMan.jpg",
    detailPath: "./detail_product_pages/Detalle_Comic_Ironman.html",
  },
  {
    id: 2,
    name: "Fantastic Four",
    price: "150.000",
    description: "Fantastic Four",
    image: "images/marvel-avengers.jpg",
    detailPath: "./detail_product_pages/Detalle_Comic_Avengers.html",
  },
  {
    id: 3,
    name: "Capitan America",
    price: "200.000",
    description: "Capitan America",
    image: "images/marvel-capitanAmerica.jpg",
    detailPath:
      "./detail_product_pages/Detalle_Comic_Capitan_America.html",
  },
  {
    id: 4,
    name: "Deadpool",
    price: "300.000",
    description: "Deadpool",
    image: "images/marvel-deadpool.jpg",
    detailPath: "detail_product_pages/Detalle_Comic_Dead_Pool.html",
  },
  {
    id: 5,
    name: "Spiderman",
    price: "400.000",
    description: "Spiderman",
    image: "images/marvel-spiderman.jpg",
    detailPath:
      "./detail_product_pages/Detalle_Comic_Spiderman.html",
  },
  {
    id: 6,
    name: "Black Widow",
    price: "300.000",
    description: "Black Widow",
    image: "images/marvel-blackwidow.jpg",
    detailPath:
      "detail_product_pages/Detalle_Comic_Black_Widow.html",
  },
  {
    id: 7,
    name: "X-Men",
    price: "700.000",
    description: "X-Men",
    image: "images/marvel-xmen.jpg",
    detailPath: "detail_product_pages/Detalle_Comic_X-Men.html",
  },
  {
    id: 8,
    name: "Daredevil",
    price: "600.000",
    description: "Daredevil",
    image: "images/marvel-daredevil.jpg",
    detailPath: "detail_product_pages/Detalle_Comic_DD.html",
  },
  {
    id: 9,
    name: "The amazing Spiderman",
    price: "400.000",
    description: "The amazing Spiderman",
    image: "images/marvel-spiderman-amazing.jpg",
    detailPath:
      "detail_product_pages/Detalle_Comic_Stan_Lee_meets_Spiderman.html",
  },
];

const root = document.querySelector("#card_section-root");
const cart = [];

const loadEvents = () => {
  const buttons = document.querySelectorAll(".button");
  for (const button of buttons) {
    button.addEventListener("click", () => {
      const selectedProduct = Products.find(
        (product) => product.id === Number(button.id)
      );
      if (selectedProduct) {
        // Obtener la ruta de detalle del producto seleccionado
        const detailPath = selectedProduct.detailPath;

        // Redirigir al usuario a la página de detalle
        window.location.href = detailPath;
      }
    });
  }
};





const createProducts = () => {
  Products.forEach((product) => {
    const card = document.createElement("div");
    card.innerHTML = `
            <img src='${product.image}'  alt='${product.description}'> 
            <div class="card-content">   
                <h3>$${product.price}</h3>
                <h4>${product.description}</h4>
                <button id='${product.id}' class='button'>Ver Mas</button>
            </div>
        `;
    root.appendChild(card);
  });
  loadEvents();
};

createProducts();
