create trigger tr_producto after insert
on producto
for each row
	insert into tiendaproducto
	(id_producto, id_tienda, en_venta)
    select	new.id_producto, id_tienda, 1
    from	tienda
    where	id_empresa=(select	id_empresa
						from	categoria
                        where	id_categoria=new.id_categoria)

				
