const Products = 
[
    {
        id:1,
        name: 'Marvel legacy',
        price: '120.000',
        description: 'Marvel legacy',
        image: '/front/images/marvel-ironMan.jpg'
    },
    {
        id:2,
        name: 'Fantastic Four',
        price: '150.000',
        description: 'Fantastic Four',
        image:  '/front/images/marvel-avengers.jpg'
    },
    {
        id:3,
        name: 'Superman',
        price: '200.000',
        description: 'Batman',
        image:  '/front/images/marvel-capitanAmerica.jpg'
    },
    {
        id:4,
        name: 'Deadpool',
        price: '300.000',
        description: 'Deadpool',
        image:  '/front/images/marvel-deadpool.jpg'
    },
    {
        id:6,
        name: 'Spiderman',
        price: '400.000',
        description: 'Spiderman',
        image:  '/front/images/marvel-spiderman.jpg'
    },
    {
        id:6,
        name: 'Black Widow',
        price: '300.000',
        description: 'Black Widow',
        image:  '/front/images/marvel-blackwidow.jpg'
    },
    {
        id:7,
        name: 'X-Men',
        price: '700.000',
        description: 'X-Men',
        image:  '/front/images/marvel-xmen.jpg'
    },
    {
        id:8,
        name: 'Daredevil',
        price: '600.000',
        description: 'Daredevil',
        image:  '/front/images/marvel-daredevil.jpg'
    },
    {
        id:9,
        name: 'The amazing Spiderman',
        price: '400.000',
        description: 'The amazing Spiderman',
        image:  '/front/images/marvel-spiderman-amazing.jpg'
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
                window.location.href = '/front/images/fantasticFour.jpg';
                /*alert(`Se agregó al carrito el producto: ${selectedProduct.name}`)
                cart.push(selectedProduct)*/
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
            <div class="card-content">   
            <h3>$${product.price}</h3>
            <h4>${product.description}</h4>
           
            <button id='${product.id}' class='button'>Ver Mas</button>
            </div>
            </div>
          
            
        `
        root.appendChild(card)
    });
    loadEvents()
}

createProducts()