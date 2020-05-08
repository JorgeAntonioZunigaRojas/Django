#drop schema aquiesta;
#create schema aquiesta;
#use aquiestav3;

insert into ubigeo
select*from aquiesta.ubigeo;

insert into moneda
select*from aquiesta.moneda;

insert into usuario(id_usuario, tipo_doc_ident, num_doc_ident, nombre, direccion, telefono, imagen, id_ubigeo)
select	id_usuario, '00', num_doc_ident, nombre, direccion, telefono, imagen, id_ubigeo
from	aquiesta.usuario where id_usuario in (1,2);

insert into empresa(ruc, rznsocial, direccion, telefono, detalle, imagen, logo, st_sgestion, id_ubigeo, id_usuario)
select ruc, rznsocial, direccion, telefono, detalle, imagen, logo, st_sgestion, id_ubigeo, id_usuario
from aquiesta.empresa;

insert into categoria(id_empresa, nombre)
select id_empresa, nombre from aquiesta.categoria;

insert into producto(codigo, nombre, precio, imagen, id_categoria, id_moneda)
select codigo, nombre, precio, imagen, id_categoria, id_moneda from aquiesta.producto;


select*from usuario;
select*from empresa;
select*from producto
order by id_producto desc;

'imagen': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Seleccione imagen',
                    'id': 'imagen',
                }
            ),
            