CREATE SCHEMA IF NOT EXISTS `planetSuperheroesDB` DEFAULT CHARACTER SET utf8 ;
USE `planetSuperheroesDB` ;

-- Tabla categories
CREATE TABLE IF NOT EXISTS `planetSuperheroesDB`.`categories` (
  `id_categories` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_categories`)
) ENGINE = InnoDB;

-- Tabla products
CREATE TABLE IF NOT EXISTS `planetSuperheroesDB`.`products` (
  `id_products` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(100) NULL,
  `description` VARCHAR(255) NOT NULL,
  `price` DECIMAL NOT NULL,
  `discount` INT NULL,
  `stock` INT NOT NULL, 
  `image` VARCHAR(255) NULL,
  `pages` INT NULL,
  `formato` VARCHAR(45) NULL,  
  `weight` DECIMAL NULL,
  `isbn` VARCHAR(45) NULL,
  `id_categories` INT NOT NULL,
  PRIMARY KEY (`id_products`),
  INDEX `fk_products_categories1_idx` (`id_categories` ASC),
  CONSTRAINT `fk_products_categories1`
    FOREIGN KEY (`id_categories`)
    REFERENCES `planetSuperheroesDB`.`categories` (`id_categories`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) ENGINE = InnoDB;

-- Tabla users
CREATE TABLE IF NOT EXISTS `planetSuperheroesDB`.`users` (
  `id_users` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  `address` VARCHAR(255) NULL,  
  `image` VARCHAR(255) NULL,
  PRIMARY KEY (`id_users`),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC)
) ENGINE = InnoDB;


/* CREATE TABLE IF NOT EXISTS `planetSuperheroesDB`.`users` (
  `id_user` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  `address` VARCHAR(255) NULL,  
  `image` VARCHAR(255) NULL,
  PRIMARY KEY (`id_user`),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC)
) ENGINE = InnoDB; */


-- Tabla roles
CREATE TABLE IF NOT EXISTS `planetSuperheroesDB`.`roles` (
  `id_role` INT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `users_id_users` INT NOT NULL,
  PRIMARY KEY (`id_role`),
  INDEX `fk_roles_users1_idx` (`users_id_users` ASC),
  CONSTRAINT `fk_roles_users1`
    FOREIGN KEY (`users_id_users`)
    REFERENCES `planetSuperheroesDB`.`users` (`id_users`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) ENGINE = InnoDB;

-- Tabla orders
CREATE TABLE IF NOT EXISTS `planetSuperheroesDB`.`orders` (
  `id_order` INT NOT NULL AUTO_INCREMENT,
  `id_user` INT NULL,
  `state` VARCHAR(45) NOT NULL,
  `orderDate` DATE NULL,
  `payment_method` VARCHAR(45) NOT NULL,
  `shipping_method` VARCHAR(45) NULL,
  `payment_status` VARCHAR(45) NULL,
  `total_amount` DECIMAL(10, 2) NULL,
  PRIMARY KEY (`id_order`),
  UNIQUE INDEX `id_order_UNIQUE` (`id_order` ASC)
) ENGINE = InnoDB;


-- Tabla orders
/* CREATE TABLE IF NOT EXISTS `planetSuperheroesDB`.`orders` (
  `id_order` INT NOT NULL AUTO_INCREMENT,
  `id_user` INT NULL,
  `state` VARCHAR(45) NOT NULL,
  `orderDate` DATE NULL,
  `payment_method` VARCHAR(45) NOT NULL,
  `shipping_method` VARCHAR(45) NULL,
  `payment_status` VARCHAR(45) NULL,
  `total_amount` DECIMAL(10, 2) NULL,
  PRIMARY KEY (`id_order`),
  UNIQUE INDEX `id_order_UNIQUE` (`id_order` ASC),
  INDEX `fk_orders_users_idx` (`id_user` ASC),
  CONSTRAINT `fk_orders_users`
    FOREIGN KEY (`id_user`)
    REFERENCES `planetSuperheroesDB`.`users` (`id_user`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) ENGINE = InnoDB;
 */


-- Tabla order_items
CREATE TABLE IF NOT EXISTS `planetSuperheroesDB`.`order_items` (
  `id_order_items` INT NOT NULL AUTO_INCREMENT,
  `quantity` INT NOT NULL,
  `id_products` INT NULL,
  `id_order` INT NOT NULL,
  PRIMARY KEY (`id_order_items`),
  INDEX `fk_order_items_products1_idx` (`id_products` ASC),
  INDEX `fk_order_items_orders1_idx` (`id_order` ASC),
  CONSTRAINT `fk_order_items_products1`
    FOREIGN KEY (`id_products`)
    REFERENCES `planetSuperheroesDB`.`products` (`id_products`)
    ON DELETE CASCADE   
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_order_items_orders1`
    FOREIGN KEY (`id_order`)
    REFERENCES `planetSuperheroesDB`.`orders` (`id_order`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) ENGINE = InnoDB;

-- Insertar valores en categories
INSERT INTO `planetSuperheroesDB`.`categories` ( name) VALUES (  'Marvel'), ( 'DC');

-- Insertar valores en products
INSERT INTO `planetSuperheroesDB`.`products` (name, description, price, discount, stock, image, pages, formato, weight, isbn, id_categories)
VALUES (
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
  'De acuerdo con el motor de locura y caos conocido como el Joker, eso es todo lo que separa a los cuerdos de los psicóticos.',
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
  'La historia de espías del siglo! Natasha Romanoff es la espía más letal del Universo Marvel y el corazón palpitante de los Avengers. ',
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
  'Hay dos nuevos héroes en la ciudad',
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







-- Insertar valores en users
INSERT INTO `planetSuperheroesDB`.`users` (first_name, last_name, email, password, address, image)
VALUES
('John', 'Doe', 'johndoe@mail.com', 'password', '123 Main St', 'john_doe.jpg'),
('Joan', 'Doe', 'joane@mail.com', 'password', '456 Main St', 'joan_doe.jpg'),
('Alice', 'Smith', 'alice@mail.com', 'password', '789 Elm St', 'alice_smith.jpg'),
('Bob', 'Johnson', 'bob@mail.com', 'password', '101 Oak St', 'bob_johnson.jpg'),
('Eva', 'Williams', 'eva@mail.com', 'password', '246 Pine St', 'eva_williams.jpg'),
('Michael', 'Brown', 'michael@mail.com', 'password', '555 Maple St', 'michael_brown.jpg');

-- Insertar un rol para el usuario en roles
INSERT INTO `planetSuperheroesDB`.`roles` (id_role, name, users_id_users)
VALUES
(1, 'User', 1),( 2, 'Admin',1);

INSERT INTO `planetSuperheroesDB`.`orders` (id_user, state, orderDate, payment_method, shipping_method, payment_status, total_amount)
VALUES
(2, 'Procesado', '2023-09-25', 'Tarjeta de crédito', 'Envío exprés', 'Aprobado', 200.00),
(1, 'Enviado', '2023-09-26', 'PayPal', 'Envío estándar', 'Aprobado', 150.00),
(2, 'Entregado', '2023-09-27', 'Tarjeta de crédito', 'Envío estándar', 'Completado', 95.00),
(1, 'Procesado', '2023-09-28', 'PayPal', 'Envío exprés', 'Aprobado', 300.00),
(2, 'Enviado', '2023-09-29', 'Tarjeta de crédito', 'Envío estándar', 'Aprobado', 180.00),
(1, 'Entregado', '2023-09-30', 'PayPal', 'Envío estándar', 'Completado', 75.00);
-- Insertar valores en order_items
INSERT INTO `planetSuperheroesDB`.`order_items` (quantity, id_products, id_order)
VALUES
(3, 1, 1),
(2, 2, 1),
(1, 3, 2),
(2, 4, 3),
(4, 5, 3),
(1, 6, 4);