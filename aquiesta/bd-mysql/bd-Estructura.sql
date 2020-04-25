
create schema aquiesta;
use aquiesta;

CREATE TABLE Categoria
(
	id_categoria         INTEGER primary key auto_increment,
	id_empresa           INTEGER NULL,
	nombre               VARCHAR(60) NULL,
	st_registro          BIT NULL
);

CREATE TABLE Empresa
(
	id_empresa           INTEGER primary key auto_increment,
	id_usuario           INTEGER NULL,
	ruc                  CHAR(11) NULL,
	rznsocial            VARCHAR(120) NULL,
	direccion            VARCHAR(120) NULL,
	id_ubigeo            CHAR(6) NULL,
	logo                 VARCHAR(60) NULL,
	st_registro          BIT NULL
);

CREATE TABLE Moneda
(
	id_moneda            CHAR(2) PRIMARY KEY,
	nombre               VARCHAR(30) NULL,
	abreviatura          VARCHAR(10) NULL
);

CREATE TABLE Pedido
(
	id_pedido            INTEGER primary key auto_increment,
	serie                CHAR(4) NULL,
	numero               CHAR(8) NULL,
	fec_emision          DATETIME NULL,
	id_usuario           INTEGER NULL,
	tipo_doc_iden        CHAR(1) NULL,
	num_doc_iden         VARCHAR(15) NULL,
	nombre               VARCHAR(120) NULL,
	direccion            VARCHAR(120) NULL,
	id_ubigeo            CHAR(6) NULL,
	telefono             VARCHAR(20) NULL,
	subtotal             DECIMAL(12,2) NULL,
	entrega_domicilio    BIT NULL,
	costo_entrega        DECIMAL(12,2) NULL,
	st_pedido            VARCHAR(20) NULL,
	cancelado            BIT NULL,
	st_registro          BIT NULL
);

CREATE TABLE PedidoDetalle
(
	id_item              INTEGER primary key auto_increment,
	id_pedido            INTEGER NULL,
	id_producto          INTEGER NULL,
	coproducto           VARCHAR(15) NULL,
	descripcion          VARCHAR(60) NULL,
	cantidad             DECIMAL(12,2) NULL,
	precio               DECIMAL(12,2) NULL
);

CREATE TABLE Producto
(
	id_producto          INTEGER primary key auto_increment,
	id_categoria         INTEGER NULL,
	codigo               VARCHAR(15) NULL,
	nombre               VARCHAR(60) NULL,
	id_moneda            CHAR(2) NULL,
	precio               DECIMAL(12,2) NULL,
	imagen               VARCHAR(60) NULL,
	st_registro          BIT NULL
);

CREATE TABLE ProductoDetalle
(
	id_detalle           INTEGER primary key auto_increment,
	id_producto          INTEGER NULL,
	clave                VARCHAR(30) NULL,
	valor                VARCHAR(60) NULL,
	st_registro          BIT NULL
);

CREATE TABLE Ubigeo
(
	id_ubigeo            CHAR(6) PRIMARY KEY,
	nombre               VARCHAR(60) NULL
);

CREATE TABLE Usuario
(
	id_usuario           INTEGER primary key auto_increment,
	email                VARCHAR(100) NULL,
	contrasena           VARCHAR(20) NULL,
	tipo_doc_ident       CHAR(1) NULL,
	num_doc_ident        VARCHAR(15) NULL,
	nombre               VARCHAR(60) NULL,
	direccion            VARCHAR(120) NULL,
	id_ubigeo            CHAR(6) NULL,
	telefono             VARCHAR(20) NULL,
	imagen               VARCHAR(60) NULL,
	st_registro          BIT NULL
);

ALTER TABLE Categoria
ADD foreign key (id_empresa) REFERENCES Empresa (id_empresa);

ALTER TABLE Empresa
ADD foreign key (id_ubigeo) REFERENCES Ubigeo (id_ubigeo);

ALTER TABLE Empresa
ADD foreign key (id_usuario) REFERENCES Usuario (id_usuario);

ALTER TABLE Pedido
ADD foreign key (id_usuario) REFERENCES Usuario (id_usuario);

ALTER TABLE Pedido
ADD foreign key (id_ubigeo) REFERENCES Ubigeo (id_ubigeo);

ALTER TABLE PedidoDetalle
ADD foreign key (id_pedido) REFERENCES Pedido (id_pedido);

ALTER TABLE PedidoDetalle
ADD foreign key (id_producto) REFERENCES Producto (id_producto);

ALTER TABLE Producto
ADD foreign key (id_moneda) REFERENCES Moneda (id_moneda);

ALTER TABLE Producto
ADD foreign key(id_categoria) REFERENCES Categoria (id_categoria);

ALTER TABLE ProductoDetalle
ADD foreign key(id_producto) REFERENCES Producto (id_producto);

ALTER TABLE Usuario
ADD foreign key(id_ubigeo) REFERENCES Ubigeo (id_ubigeo);


