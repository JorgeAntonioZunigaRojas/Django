#drop schema aquiesta;
#create schema aquiesta;
#use aquiesta;

insert into ubigeo
select*from aquiestav2.ubigeo;

insert into moneda
select*from aquiestav2.moneda;

insert into usuario(id_usuario, tipo_doc_ident, num_doc_ident, nombre, direccion, telefono, imagen, id_ubigeo)
select	id_usuario, tipo_doc_ident, num_doc_ident, nombre, direccion, telefono, imagen, id_ubigeo
from	aquiestav2.usuario where id_usuario in (1,2);

insert into empresa(ruc, rznsocial, direccion, telefono, detalle, imagen, logo, st_sgestion, id_ubigeo, id_usuario)
select ruc, rznsocial, direccion, telefono, detalle, imagen, logo, st_sgestion, id_ubigeo, id_usuario
from aquiestav2.empresa;

insert into categoria(id_empresa, nombre)
select id_empresa, nombre from aquiestav2.categoria;

insert into producto(codigo, nombre, precio, imagen, id_categoria, id_moneda)
select codigo, nombre, precio, imagen, id_categoria, id_moneda from aquiestav2.producto;


select*from usuario;
select*from empresa;
select*from producto
order by id_producto desc;

update	producto
set		imagen='static/imagen_no_disponible.png'
where	id_producto not in (135, 134)


select*from categoria
where id_empresa=2
order by fecha_edicion desc

id_categoria, nombre, id_empresa

'imagen': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Seleccione imagen',
                    'id': 'imagen',
                }
            ),
            