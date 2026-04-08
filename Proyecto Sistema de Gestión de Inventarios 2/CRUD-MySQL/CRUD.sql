CREATE SCHEMA Sistema_Control;

Use Sistema_Control;

Create table usuario(
id_usuario int auto_increment not null,
usuario varchar(50) unique,
contrasenia varchar(50) unique,
Primary Key (id_usuario)
);

Create table producto(
id_ptoducto int auto_increment not null,
codigo varchar(50) not null,
descripcion varchar(100) not null,
unidad_M varchar(50),
presentacion varchar(50),
precio float not null,
estado varchar(50) not null,
fecha date,
Primary Key (id_ptoducto)
);



