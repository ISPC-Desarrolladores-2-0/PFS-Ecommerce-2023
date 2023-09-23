import sqlite3

# Conexión a la  base de datos (o crea una nueva si no existe)
conn = sqlite3.connect("mi_base_de_datos.db")
cursor = conn.cursor()

# Define el código SQL que deseas ejecutar para configurar y poblar las tablas
sql_script = """
-- Tabla categories
CREATE TABLE IF NOT EXISTS categories (
  id_categories INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL
);

-- Tabla products
CREATE TABLE IF NOT EXISTS products (
  id_products INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT,
  description TEXT NOT NULL,
  price REAL NOT NULL,
  discount INTEGER,
  stock INTEGER NOT NULL, 
  image TEXT,
  pages INTEGER,
  formato TEXT,  
  weight REAL,
  isbn TEXT,
  id_categories INTEGER NOT NULL,
  FOREIGN KEY (id_categories) REFERENCES categories(id_categories)
);

-- Tabla users
CREATE TABLE IF NOT EXISTS users (
  id_users INTEGER PRIMARY KEY AUTOINCREMENT,
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  email TEXT NOT NULL,
  password TEXT NOT NULL,
  address TEXT,
  image TEXT,
  UNIQUE(email)
);

-- Tabla roles
CREATE TABLE IF NOT EXISTS roles (
  id_role INTEGER NOT NULL,
  name TEXT NOT NULL,
  users_id_users INTEGER NOT NULL,
  PRIMARY KEY (id_role),
  FOREIGN KEY (users_id_users) REFERENCES users(id_users)
);

-- Tabla orders
CREATE TABLE IF NOT EXISTS orders (
  id_order INTEGER PRIMARY KEY AUTOINCREMENT,
  id_user INTEGER,
  state TEXT NOT NULL,
  orderDate DATE,
  payment_method TEXT NOT NULL,
  shipping_method TEXT,
  payment_status TEXT,
  total_amount REAL
);

-- Tabla order_items
CREATE TABLE IF NOT EXISTS order_items (
  id_order_items INTEGER PRIMARY KEY AUTOINCREMENT,
  quantity INTEGER NOT NULL,
  id_products INTEGER,
  id_order INTEGER NOT NULL,
  FOREIGN KEY (id_products) REFERENCES products(id_products),
  FOREIGN KEY (id_order) REFERENCES orders(id_order)
);

-- Inserta valores en categories
INSERT INTO categories (name) VALUES ('Marvel'), ('DC');

-- Inserta valores en products
INSERT INTO products (name, description, price, discount, stock, image, pages, formato, weight, isbn, id_categories)
VALUES
(
  'Capitan America',
  'El primer año de la revolucionaria etapa que devolvió toda su gloria al Centinela de la Libertad. Después de que fuera dado por muerto por los suyos...',
  9800.00,
  30,
  64,
  'marvel-capitanAmerica.jpg',
  64,
  '20x29x2cm',
  0.60,
  '9788416998166',
  1  
),
(
    'Daredevil Comic',
    '¡El hombre sin miedo desapareción! Daredevil ya no está más en Hell''s Kitchen, y en su ausencia, los verdaderos demonios salen a jugar...',
    3040.00,
    10,
    120,
    'DareD.png',
    120,
    '26x17x2cm',
    0.45,
    '9786075688336',
    1    
),
(
    'Dead Pool Comic',
    'Es una historia de amor, Deadpool, ¡solo di que sí! Elsa Bloodstone, la cazadora de monstruos, está muriendo, y el único que puede salvarla es… ¡Wade Wilson! ...',
    9800.00,
    10,
    64,
    'marvel-deadpool.jpg',
    64,
    '20x29x2cm',
    0.60,
    '9788416998166',
    1
    
),
(
    'Flash: Flashpoint',
    '¡Todo lo que Barry Allen conoce ha cambiado en un instante! Flash es el hombre más rápido del mundo, pero este no es su mundo. El curso de la historia ha cambiado...',
    9800.00,
    30,
    240,
    'dc-flash.jpg',
    240,
    '20x29x2cm',
    0.60,
    '978-987-819-167-6',
    2    
),
(
    'Ironman: The invincible',
    'Con un trozo de metralla incrustado en su pecho, peligrosamente cerca del corazón, lo único que mantiene con vida al multimillonario Tony Stark es su supertraje de hierro...',
    9800.00,
    30,
    64,
    'marvel-ironMan.jpg',
    64,
    '20x29x2cm',
    0.60,
    '9788416998166',
    1
),
(
    'Justice League: The New 52',
    'El título insignia del relanzamiento de New 52 de DC, Justice League busca definir el nuevo DC Universe con historias y personalidades de personajes modificadas...',
    9800.00,
    30,
    64,
    'dc-justiceLeague.jpg',
    64,
    '20x29x2cm',
    0.60,
    '1401237886',
    2
),
(
    'Spiderman',
    'Un gigantesco volumen, que reúne tanto Universo Spiderman como Spidergedón, las dos grandes sagas dedicadas a unir a todos los Hombres y Mujeres Araña...',
    30600.00,
    10,
    300,
    'marvel-spiderman.jpg',
    300,
    '20x29x5cm',
    0.80,
    '9788416998166',
    1
),
(
    'Stan Lee meets Spiderman',
    '¡El primero de una serie de especiales independientes que celebran el 65 aniversario del empleo de Stan Lee en Marvel!...',
    9800.00,
    10,
    64,
    'marvel-spiderman-amazing.jpg',
    64,
    '20x29x2cm',
    0.60,
    '9788416998166',
    1
),
(
    'Supergirl: Brainiac',
    '¡La Tierra está siendo atacada por mil millones de Braniacs! El malvado androide y sus fríos y calculadores clones han engañado a Superman para que se aleje...',
    9800.00,
    30,
    64,
    'dc-superGirlpg.jpg',
    64,
    '20x29x2cm',
    0.60,
    '9788416998166',
    2
),
(
    'Superman: The last',
    '¡LAS MEJORES AVENTURAS DEL HOMBRE DE ACERO Y LA PRINCESA GUERRERA! Desde 1940, Wonder Woman ha sido un símbolo de la libertad, la justicia y la igualdad...',
    4950.00,
   10,
    64,
    'dc-wonderWomen.jpg',
    64,
    '20x29x2cm',
    0.60,
    '9788416998166',
    2
),
(
    'X-Men comic',
    '¡El amanecer de los mutantes no para de asombrar! Fuera de Krakoa, Domino tiene una misión: encontrar a la persona que, de alguna forma, le está robando sus poderes...',
    9800.00,
    30,
    64,
    'marvel-xmen.jpg',
    64,
    '20x29x2cm',
    0.60,
    '9788416998166',
    1
),
(
  'Batman: Killing Joker',
  'De acuerdo con el motor de locura y caos conocido como el Joker, eso es todo lo que separa a los cuerdos de los psicóticos. Liberado una vez más de los confines del Asilo Arkham, está dispuesto a demostrar su perturbador punto. Y va a usar al principal policía de Gotham, el comisionado Jim Gordon, y a su brillante y bella hija Bárbara para hacerlo. Ahora Batman deberá correr para detener a su archienemigo antes de que su reinado de terror reclame a dos de los amigos más cercanos del Caballero Oscuro. ¿Podrá finalmente poner fin al ciclo de sed de sangre y locura que une a estos dos enemigos icónicos antes de que conduzca a su conclusión fatal? Y a medida que finalmente se revela el horroroso origen del Príncipe Payaso del Crimen, ¿la delgada línea que separa a la nobleza de Batman y la locura del Joker se romperá de una vez por todas?',
  9800.00,
  30,
  50,
  'batman-killing-joker.jpg', 
  64,
  '20x29x2cm',
  0.55,
  '978-987-819-184-3',
  1
),
(
  'Black Widow',
  'La historia de espías del siglo! Natasha Romanoff es la espía más letal del Universo Marvel y el corazón palpitante de los Avengers. Pero cuando una figura misteriosa comienza a explotar su turbio pasado, ¡Black Widow debe pasar a la clandestinidad y desaparecer del mapa! ¿En quién puede confiar en esta red de engaños? Y lo que es más importante, ¿pueden sus amigos seguir confiando en ella? Natasha debe analizar todos los nombres de su pasado, ¡comenzando con Tony Stark y Bucky Barnes! Black Widow y el Soldado del Invierno tienen una gran historia, pero cuando se reúnan, pueden terminar sin futuro. Su compañera Yelena Belova llama a su puerta, pero, ¿puede ayudar a Natasha a superar su pasado? Y cuando Black Widow apunte a Hawkeye, ¡ella podría recibir un disparo en el corazón!',
  9800.00,
  30,
  50,
  'marvel-blackwidow.jpg',  
  64,
  '20x29x2cm',
  0.60,
  '9788416998166',
  1  
),
(
  'Batman: Rebirth',
  'Hay dos nuevos héroes en la ciudad: un par de metahumanos enmascarados que tienen los poderes de Superman y muestran una devoción inquebrantable por preservar todo lo bueno de esta enfermiza urbe. Se hacen llamar Gotham y Gotham Girl, ha salvado la vida de Batman, han luchado junto a él y le han tomado como referente y ejemplo en su aprendizaje. Pero... ¿qué ocurre si los nuevos guardianes de Gotham se vuelven malvados? ¿Y si culpan al Caballero Oscuro de las tinieblas que amenazan con engullir su ciudad?',
  9800.00,
  30,
  15,
  'dc-batman.jpg',
  64,
  '20x29x2cm',
  0.55,
  '978-987-819-184-3',
  2 
);


-- Inserta valores en users
INSERT INTO users (first_name, last_name, email, password, address, image)
VALUES
('John', 'Doe', 'johndoe@example.com', 'password', '123 Main St', 'john_doe.jpg'),
('Joan', 'Doe', 'joane@example.com', 'password', '456 Main St', 'joan_doe.jpg'),
('Alice', 'Smith', 'alice@example.com', 'password', '789 Elm St', 'alice_smith.jpg'),
('Bob', 'Johnson', 'bob@example.com', 'password', '101 Oak St', 'bob_johnson.jpg'),
('Eva', 'Williams', 'eva@example.com', 'password', '246 Pine St', 'eva_williams.jpg'),
('Michael', 'Brown', 'michael@example.com', 'password', '555 Maple St', 'michael_brown.jpg');


-- Inserta un rol para el usuario en roles
INSERT INTO roles (id_role, name, users_id_users)
VALUES
(1, 'User', 1),
(2, 'Admin', 1),
-- (Inserta los demás roles aquí...)
;

-- Inserta valores en orders y order_items (deberás adaptar los valores según corresponda)
INSERT INTO orders (id_user, state, orderDate, payment_method, shipping_method, payment_status, total_amount)
VALUES
(2, 'Procesado', '2023-09-25', 'Tarjeta de crédito', 'Envío exprés', 'Aprobado', 200.00),
(1, 'Enviado', '2023-09-26', 'PayPal', 'Envío estándar', 'Aprobado', 150.00),
(2, 'Procesado', '2023-09-25', 'Tarjeta de crédito', 'Envío exprés', 'Aprobado', 200.00),
(1, 'Enviado', '2023-09-26', 'PayPal', 'Envío estándar', 'Aprobado', 150.00),
(2, 'Entregado', '2023-09-27', 'Tarjeta de crédito', 'Envío estándar', 'Completado', 95.00),
(1, 'Procesado', '2023-09-28', 'PayPal', 'Envío exprés', 'Aprobado', 300.00),
(2, 'Enviado', '2023-09-29', 'Tarjeta de crédito', 'Envío estándar', 'Aprobado', 180.00),
(1, 'Entregado', '2023-09-30', 'PayPal', 'Envío estándar', 'Completado', 75.00);

INSERT INTO order_items (quantity, id_products, id_order)
VALUES
(3, 1, 1),
(2, 2, 1),
(1, 3, 2),
(2, 4, 3),
(4, 5, 3),
(1, 6, 4);
"""

# Ejecuta el script SQL
cursor.executescript(sql_script)
conn.commit()

# Cierra la conexión
conn.close()
