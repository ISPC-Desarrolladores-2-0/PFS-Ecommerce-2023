const Products = 
[
    {
        id:1,
        name: 'Marvel legacy',
        price: '120.000',
        description: 'Marvel legacy',
        image: '/front/images/marvel1.webp'
    },
    {
        id:2,
        name: 'Fantastic Four',
        price: '150.000',
        description: 'Fantastic Four',
        image:  '/front/images/fantasticFour.jpg'
    },
    {
        id:3,
        name: 'Superman',
        price: '200.000',
        description: 'Batman',
        image:  '/front/images/superman.jpg'
    },
]

const root = document.querySelector('#card_section-root');
const cart = []

const loadEvents = () =>
{
    const buttons = document.querySelectorAll('.button')
    for (const button of buttons) 
    {
        button.addEventListener('click', ()=> {
            const selectedProduct = Products.find(product => product.id === Number(button.id))
            if(selectedProduct){
                alert(`Se agregó al carrito el producto: ${selectedProduct.name}`)
                cart.push(selectedProduct)
            }
        })    
    }
}

const createProducts = () =>
{
    Products.forEach(product => {
        const card = document.createElement('div')
        card.innerHTML = `
            <img src='${product.image}'  alt='${product.description}'>           
            <h3>$${product.price}</h3>
            <h4>${product.description}</h4>
            <button id='${product.id}' class='button'>Agregar al carrito</button>
            </div>
        `
        root.appendChild(card)
    });
    loadEvents()
}

createProducts()