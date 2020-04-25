drop schema aquiesta;
create schema aquiesta;
use aquiesta;

CREATE TABLE Categoria
(
	id_categoria         INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
	id_empresa           INTEGER NULL,
	nombre               VARCHAR(60) NULL,
	st_registro          BIT NULL DEFAULT 1
);

CREATE TABLE Empresa
(
	id_empresa           INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
    id_usuario			 INTEGER,
	ruc                  CHAR(11) NULL,
	rznsocial            VARCHAR(120) NULL,
	direccion            VARCHAR(120) NULL,
	id_ubigeo            CHAR(6) NULL,
	logo                 VARCHAR(60) NULL,
	st_registro          BIT NULL DEFAULT 1
);

CREATE TABLE EmpresaUsuario
(
	id_eusuario          INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
	id_empresa           INTEGER NULL,
	tipoUsuario          VARCHAR(15) NULL,
	apellidos            VARCHAR(30) NULL,
	nombre               VARCHAR(30) NULL,
	idUsuario            VARCHAR(100) NULL,
	contrasena           VARCHAR(20) NULL,
    imagen				 VARCHAR(60) NULL,
	st_registro          BIT NULL DEFAULT 1
);

CREATE TABLE Moneda
(
	id_moneda            CHAR(2) NOT NULL,
	nombre               VARCHAR(30) NULL,
	abreviatura          VARCHAR(10) NULL,
	PRIMARY KEY (id_moneda)
);

CREATE TABLE Pedido
(
	id_pedido            INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
	id_tienda            INTEGER NULL,
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
	costo_entrega        VARCHAR(120) NULL,
	st_pedido            VARCHAR(20) NULL,
	cancelado            BIT NULL,
    st_registro          BIT NULL DEFAULT 1
);

CREATE TABLE PedidoDetalle
(
	id_item              INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
	id_pedido            INTEGER NULL,
	id_producto          INTEGER NULL,
	coproducto           VARCHAR(15) NULL,
	descripcion          VARCHAR(60) NULL,
	cantidad             DECIMAL(12,2) NULL,
	precio               DECIMAL(12,2) NULL
);

CREATE TABLE Producto
(
	id_producto          INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
	id_categoria         INTEGER NULL,
	codigo               VARCHAR(15) NULL,
	nombre               VARCHAR(60) NULL,
	id_moneda            CHAR(2) NULL,
	precio               DECIMAL(12,2) NULL,
	imagen               VARCHAR(60) NULL,
	st_registro          BIT NULL DEFAULT 1
);



CREATE TABLE ProductoDetalle
(
	id_detalle           INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
	id_producto          INTEGER NULL,
	clave                VARCHAR(30) NULL,
	valor                VARCHAR(60) NULL,
	st_registro          BIT NULL DEFAULT 1
);



CREATE TABLE Tienda
(
	id_tienda            INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
	id_empresa           INTEGER NULL,
	nombre               VARCHAR(60) NULL,
	direccion            VARCHAR(120) NULL,
	id_ubigeo            CHAR(6) NULL,
	ug_latitud           VARCHAR(20) NULL,
	ug_longitud          VARCHAR(20) NULL,
	telefono             VARCHAR(20) NULL,
	foto                 VARCHAR(60) NULL,
	st_gestion           VARCHAR(10) NULL,
	st_registro          BIT NULL DEFAULT 1
);



CREATE TABLE TiendaProducto
(
	id_tproducto         INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
	id_tienda            INTEGER NULL,
	id_producto          INTEGER NULL,
	en_venta             BIT NULL
);



CREATE TABLE TiendaUsuario
(
	id_tusuario          INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
	id_tienda            INTEGER NULL,
	id_eusuario          INTEGER NULL,
	acceder              BIT NULL
);



CREATE TABLE Ubigeo
(
	id_ubigeo            CHAR(6) NOT NULL,
	nombre               VARCHAR(60) NULL,
	PRIMARY KEY (id_ubigeo)
);



CREATE TABLE Usuario
(
	id_usuario           INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
	email                VARCHAR(100) NULL,
	contrasena           VARCHAR(20) NULL,
	tipo_doc_ident       CHAR(1) NULL,
	num_doc_ident        VARCHAR(15) NULL,
	nombre               VARCHAR(60) NULL,
	direccion            VARCHAR(120) NULL,
	id_ubigeo            CHAR(6) NULL,
	telefono             VARCHAR(20) NULL,
    imagen				 VARCHAR(60) NULL,
	st_registro          BIT NULL DEFAULT 1
);

ALTER TABLE Categoria
ADD FOREIGN KEY (id_empresa) REFERENCES Empresa (id_empresa);


ALTER TABLE Empresa
ADD FOREIGN KEY (id_ubigeo) REFERENCES Ubigeo (id_ubigeo);

ALTER TABLE Empresa
ADD FOREIGN KEY (id_usuario) REFERENCES Usuario (id_usuario);

ALTER TABLE EmpresaUsuario
ADD FOREIGN KEY (id_empresa) REFERENCES Empresa (id_empresa);

ALTER TABLE Pedido
ADD FOREIGN KEY (id_tienda) REFERENCES Tienda (id_tienda);

ALTER TABLE Pedido
ADD FOREIGN KEY (id_usuario) REFERENCES Usuario (id_usuario);


ALTER TABLE Pedido
ADD FOREIGN KEY (id_ubigeo) REFERENCES Ubigeo (id_ubigeo);


ALTER TABLE PedidoDetalle
ADD FOREIGN KEY (id_pedido) REFERENCES Pedido (id_pedido);



ALTER TABLE PedidoDetalle
ADD FOREIGN KEY (id_producto) REFERENCES Producto (id_producto);



ALTER TABLE Producto
ADD FOREIGN KEY (id_moneda) REFERENCES Moneda (id_moneda);


ALTER TABLE Producto
ADD FOREIGN KEY (id_categoria) REFERENCES Categoria (id_categoria);


ALTER TABLE ProductoDetalle
ADD FOREIGN KEY (id_producto) REFERENCES Producto (id_producto);


ALTER TABLE Tienda
ADD FOREIGN KEY (id_empresa) REFERENCES Empresa (id_empresa);


ALTER TABLE Tienda
ADD FOREIGN KEY (id_ubigeo) REFERENCES Ubigeo (id_ubigeo);


ALTER TABLE TiendaProducto
ADD FOREIGN KEY (id_producto) REFERENCES Producto (id_producto);


ALTER TABLE TiendaProducto
ADD FOREIGN KEY (id_tienda) REFERENCES Tienda (id_tienda);


ALTER TABLE TiendaUsuario
ADD FOREIGN KEY (id_eusuario) REFERENCES EmpresaUsuario (id_eusuario);


ALTER TABLE TiendaUsuario
ADD FOREIGN KEY (id_tienda) REFERENCES Tienda (id_tienda);


ALTER TABLE Usuario
ADD FOREIGN KEY (id_ubigeo) REFERENCES Ubigeo (id_ubigeo);

