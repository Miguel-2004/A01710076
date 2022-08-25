# A01710076 BECERRA AYALA MIGUEL ANGEL
Repositorio para subir trabajos escolares

“No hay freno posible que pare el aumento de precios en México.” La inflación general en el país se situó en 8,15% en julio de 2022, lo que lo coloca como la tasa más alta en los últimos 22 años. Según el Índice Nacional de Precios al Consumidor, dado a conocer este martes por el Inegi, la tasa de inflación presentó una variación de 0,74% respecto a junio de este año. Se trata de un salto drástico respecto al índice del año pasado, cuando la tasa anual se ubicó en 5,81%. https://elpais.com/mexico/economia/2022-08-09/sigue-la-escalada-de-precios-la-inflacion-anual-se-ubica-en-815-en-mexico.html#:~:text=No%20hay%20freno%20posible%20que,ubicara%20en%209%2C12%25.

CONTEXTO

En base a esta problemática que actualmente enfrenta el país he tomado la iniciativa de crear un compilador de datos que ayude a las personas a ahorrar un poco en estos tiempos, lo que se intentará lograr es crear un compilador donde cada semana se puedan actualizar los precios de algunos productos de la canasta básica y algunos otros y que haya dos tipos de usuarios:

Los primeros serán las personas que quieran adquirir los productos y puedan checar los precios por medio del compilador creado y de esta manera poder recurrir a los lugares donde los precios sean más accesibles.

Los segundos usuarios serán personas o tiendas que nos ayuden con la recopilación de datos para de esta manera poder brindarle a las personas información certera y que se haya obtenido de una fuente de información confiable.

1. Algoritmo de control o menú (hacer lo que el usuario le indique)
   opcion= proporcionado por el usuario
   
0. Pedir opcion al usuario 

1. Si opcion = 1 
1.1 Ejecutar “buscar producto” algo que vamos a buscar
2. Si opcion = 2
2.1 Ejecutar “mostrar todo los productos”
3. Si opción=3
ejecutar “registrar un producto”
4.Si opción =4
4.1 finalizar 
Algoritmo “buscar producto”
En lista buscar el producto que ingrese el usuario y mostrar el resultado (precios del producto, tienda donde puede ser adquirido)

Variables

1. lista_productos
2. producto_buscar
3. intentos=0
Pasos

1. Pedir producto al usuario 
2. intentos=intentos+1
3. Para cada producto en la lista 
   3.1 si nombre_producto=producto_buscar 
       3.1.1 Mostrar datos del producto
       3.1.2 Terminar algoritmo
4. Si intentos <5 
   4.1 volver a paso 1
5. Si no 
   5.1 volver a menu 
   
Algoritmo “mostrar todos los productos”
Mostrar todos los productos, pero de cada producto mostrar cual es la tienda donde puedes adquirirlo al menor costo 

Variables:

1. productos_buscar
2. precio_minimo

Pasos

1. Si opción=4 
   1.1 Por cada producto en la lista
   1.2 si nombre_producto=producto_buscar
   1.3 Buscar precio_minimo 
2. Mostrar precio_minimo
3. Terminar algoritmo


Algoritmo “ registrar producto ”
Para obtener un mejor desarrollo del programa y una optimización acerca de la actualización de los precios existe esta opción que te permitirá capturar los precios y las tiendas donde los podrás adquirir.

Variables:
1. registrar_producto
2. precio_producto
3. tienda_nombre

Pasos:
1. si opción=4
   1.1 producto_buscar
   1.2 si nombre_producto=producto_buscar
2. ingresar producto_precio
   2.1 si solo desea cambiar precio_producto
   2.2 si salir, no registrar tienda_nombre
3. ingresar tienda_nombre
   3.1 finalizar
 



