# POKEDEX_PROYECTO_M4
El siguiente código nos da algunos de los pokemon con algunas caracteristicas, por ejemplo su peso, su nombre, habilidades, la imagen del pokemon si la hay, etc.
Para que esta app funcione para otras personas es necesario que tengan descargadas algunas librerias como requests, matplotlib, PIL.
Para la elaboracion de este programa lo primero fue entrar a la API de pokemon y ver como estaba la estructura para poder acceder a los elementos.
Lo siguiente fue comenzar a elaborar el código importando y descargando algunas librerias ya mencionadas anteriormente, posterior a eso se definieron 4 funciones.
Lo siguiente fue empezar a darle las instrucciones a cada uno de lo que van a realizar, a la primera funcion con el nombre obtener_datos_pokemon lo que hace es
mandar una solicitud de a la API de algun pokemon que se le pase como parametro y en caso de que exista retornara la informacion, de lo contrario retornara none.
La siguiente funcion con el nombre guarar_datos_pokemon_en_json lo que hace que obtiene 2 parametros uno que es el nombre del pokemon y el otro son los datos, 
y estos se van a almacenar en formato json en una carpeta llamada pokedex que en caso de que no exista se creara.
La siguiente funcion  llamada mostrar_datos_pokemon recibe un parametro con los datos del pokemon, y la funcion los imprimira en este caso tenemos que es el nombre,
una imagen que esta dentro de un try, except para que en caso de que la imagen de algun pokemon no exista la aplicacion siga corriendo sin ningun problema.
La siguiente funcion es la del programa principal que esta es la que llamara a todas las funciones antes descritas, primero preguntara al usuario que ingrese
un pokemon y lo almacenara en una variable llamada nombre_pokemon que esta estara la pasaremos como parametro a la funcion obtener_datos_pokemon y esta se almacenara
en la variable datos_pokemon3 que estará  en un if que evaluara  la siguiente condicion  si datos_pokemon3 no es none 
entonces llame a las funciones correspondientes que es guardar los datos en formato json  y la impresion de los datos del pokemon ingresado por el usuario
al final de imprimir estos datos se le preguntará al usuario si desea agregar otro pokémon a desea salir y en caso de salir se le pedira que ingrese 0 + enter 
de lo contrario solo enter para continuar el programa.
