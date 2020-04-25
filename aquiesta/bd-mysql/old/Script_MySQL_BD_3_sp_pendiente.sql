delimiter $$
create procedure sp_empresausuario_q01(
p_ruc varchar(20),
p_usuario varchar(100),
p_contrasena varchar(100))
begin
	Select	e.id_empresa as empresa_id_empresa
    		, e.ruc as empresa_ruc
			, e.rznsocial as empresa_rznsocial
            , e.logo as empresa_logo
            , eu.id_eusuario as usuario_id_eusuario
            , eu.idusuario as usuario_idusuario
            , eu.nombre as usuario_nombre
            , count(t.id_tienda) as cantidad_tiendas
	From	empresa e inner join
			tienda t on e.id_empresa=t.id_empresa inner join
			tiendausuario tu on tu.id_tienda=t.id_tienda inner join
			empresausuario eu on tu.id_eusuario=eu.id_eusuario
	where	e.st_registro=1
	and		t.st_registro=1
	and		eu.st_registro=1
	and		tu.acceder=1
    and		e.ruc=p_ruc
	and		eu.idusuario=p_usuario
	and		eu.contrasena=p_contrasena
	Group by e.id_empresa, e.ruc, e.rznsocial, e.logo, eu.id_eusuario, eu.idusuario, eu.nombre;
end;$$


call sp_empresausuario_q01('10438098981','admin@gmail.com','123')

select*from empresausuario;
select*from empresa

/*
*/

select	c.id_categoria
		, c.nombre
from	categoria c inner join
		empresa e on c.id_empresa=e.id_empresa
where	e.id_empresa=1
and		c.st_registro=1
order by c.nombre;

select	p.id_producto
		, p.codigo
		, c.nombre as categoria
        , p.nombre
        , m.abreviatura as moneda
        , p.precio
        , p.imagen
from	empresa e inner join
		tienda t on t.id_empresa=e.id_empresa inner join
        categoria c on c.id_empresa=e.id_empresa inner join
        producto p on p.id_categoria=c.id_categoria inner join
        moneda m on m.id_moneda=p.id_moneda inner join
        tiendaproducto tp on tp.id_tienda=t.id_tienda and tp.id_producto=p.id_producto
where	e.id_empresa=1
and		t.id_tienda=1
and		p.st_registro=1
order by c.nombre, p.nombre;



id_categoria, id_empresa, nombre, st_registro




        
        