# A01710076 BECERRA AYALA MIGUEL ANGEL
Repositorio para subir trabajos escolares

“No hay freno posible que pare el aumento de precios en México.” La inflación general en el país se situó en 8,15% en julio de 2022, lo que lo coloca como la tasa más alta en los últimos 22 años. Según el Índice Nacional de Precios al Consumidor, dado a conocer este martes por el Inegi, la tasa de inflación presentó una variación de 0,74% respecto a junio de este año. Se trata de un salto drástico respecto al índice del año pasado, cuando la tasa anual se ubicó en 5,81%. https://elpais.com/mexico/economia/2022-08-09/sigue-la-escalada-de-precios-la-inflacion-anual-se-ubica-en-815-en-mexico.html#:~:text=No%20hay%20freno%20posible%20que,ubicara%20en%209%2C12%25.

CONTEXTO

En base a esta problemática que actualmente enfrenta el país he tomado la iniciativa de crear un compilador de datos que ayude a las personas a ahorrar un poco en estos tiempos, lo que se intentará lograr es crear un compilador donde cada semana se puedan actualizar los precios de algunos productos de la canasta básica y algunos otros y que haya dos tipos de usuarios:

Los primeros serán las personas que quieran adquirir los productos y puedan checar los precios por medio del compilador creado y de esta manera poder recurrir a los lugares donde los precios sean más accesibles.



1. Algoritmo de control o menú (hacer lo que el usuario le indique)
   opcion= proporcionado por el usuario
   
0. Pedir opcion al usuario 

1. Si opcion = 1 
1.1 Ejecutar “buscar producto” sera la opción donde el usuario podrá ver el menor precio de un objeto indicado por el usuario

2. Si opcion = 2
2.1 Ejecutar “calculate basic basket” dara el precio al usuario de la canasta básica buscando en cada producto el precio menor

3. Si opción=3
ejecutar “precio promedio” sumara el precio de todos los productos del programa y dará un resultado promedio


Algoritmo “buscar producto”

En lista buscar el producto que ingrese el usuario y mostrar la mejor opción donde el usuario pueda comprarlo

Variables

1. lista_productos
2. producto_buscar
3. intentos=0


Pasos

1. Pedir producto al usuario 

3. Depende del producto que ingrese:
   2.1 Buscarlo en las listas
     2.1.1 En cada lista buscar el mejor precio es decir el menor
    
4. Mostrar al usuario la mejor opción

6. Terminar el ciclo
   
Algoritmo “calcular precio de la canasta basica”

Mostrar el precio de la canasta básica buscando en cada uno de los productos guardados y así dar un precio de la canasta con el menor costo.

1. productos_buscar
2. precio_minimo

Pasos

1. Si opción=4 
   1.1 Por cada producto en la lista
   1.2 Buscar precio_minimo

2. Guardar precio_minimo en una variable

4. Sumar todos los productos con los precios menores

6. Dar el precio de la canasta básica


Algoritmo “ precio promedio de todos los productos ”

Para obtener los precios promedio de todos los productos guardados para de esta amenra el usuario se pueda dar una idea del precio promedio de cada uno de los proctos

Variables:

1. precio_promedio
2. precio_producto
3. final_price

Pasos:
1. si opción=4
   1.1 producto_buscar
   1.2 buscar en productos todos los precios 
  
2. Guardar todos los precios
   2.1 Sumar todos los precios y dividirlos entre la cantidad de productos que tenemos
   2.2 Dar el precio promedio de los productos al usuario
 



