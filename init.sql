CREATE TABLE customer
(
  customer_id integer(10) AUTO_INCREMENT NOT NULL PRIMARY KEY, 
  name varchar(255) NOT NULL,
  email varchar(255) NOT NULL
);

CREATE TABLE order_
(
  order_id integer(10) AUTO_INCREMENT NOT NULL PRIMARY KEY, 
  customer_id integer(10), 
  delivery_address integer(10),
  creation_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT order_fk1 FOREIGN KEY (customer_id)
  REFERENCES customer (customer_id) 
  ON UPDATE NO ACTION ON DELETE NO ACTION
);

CREATE TABLE product
(
  product_id integer(10) AUTO_INCREMENT NOT NULL PRIMARY KEY, 
  name varchar(255) NOT NULL,
  unit_price integer(10) NOT NULL
);

CREATE TABLE order_detail
(
  product_description varchar(255) NOT NULL,
  price integer(10) NOT NULL, 
  order_id integer(10) NOT NULL,
  CONSTRAINT order_detail_fk1 FOREIGN KEY (order_id)
  REFERENCES order_ (order_id) 
  ON UPDATE NO ACTION ON DELETE NO ACTION
);

CREATE TABLE products_customer
(
  customer_id integer(10) AUTO_INCREMENT NOT NULL, 
  product_id integer(10) NOT NULL,
  CONSTRAINT products_customer_fk1 FOREIGN KEY (customer_id)
  REFERENCES customer (customer_id) 
  ON UPDATE NO ACTION ON DELETE NO ACTION,
  CONSTRAINT products_customer_fk2 FOREIGN KEY (product_id)
  REFERENCES product (product_id) 
  ON UPDATE NO ACTION ON DELETE NO ACTION
);

INSERT INTO customer (name, email) VALUES ("jorge", "jorge@hotmail.com");
INSERT INTO customer (name, email) VALUES ("nicolas", "nicolas@gmail.com");
INSERT INTO customer (name, email) VALUES ("valentina", "valen12@gmail.com");
INSERT INTO customer (name, email) VALUES ("hector", "hector12@gmail.com");

INSERT INTO product (name,unit_price) VALUES ("productA",200);
INSERT INTO product (name,unit_price) VALUES ("productB",150);
INSERT INTO product (name,unit_price) VALUES ("productC",170);
INSERT INTO product (name,unit_price) VALUES ("productD",700);
INSERT INTO product (name,unit_price) VALUES ("productE",350);

INSERT INTO products_customer (customer_id,product_id) VALUES (1,1);
INSERT INTO products_customer (customer_id,product_id) VALUES (1,2);
INSERT INTO products_customer (customer_id,product_id) VALUES (1,5);

drop table order_detail;
drop table products_customer;
drop table product;
drop table order_;
drop table customer;

