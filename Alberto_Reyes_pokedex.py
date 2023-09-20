import os
import requests
import json
import matplotlib.pyplot as plt
from PIL import Image
from urllib.request import urlopen

#Creamos la función para ontener los datos del pokémon
def obtener_datos_pokemon(nombre):

    """Funcion para solicitar a la API una peticion de un pokémon"""
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre.lower()}/"
    
    try :
        #Hacemos la peticion con el metodo get que contiene la variable con la ruta de la API
        respuesta = requests.get(url, timeout=10)
    except requests.Timeout:
        print('Error, el tiempo de espera a finalizado.')

  
    
   
    if respuesta.status_code == 200:
        datos_pokemon1 = respuesta.json()
        return datos_pokemon1
    else:
        return None

#creamos una fucion para guardar los datos
def guardar_datos_pokemon_en_json(nombre, datos_pokemon2):

    """Función que guarda los datos en un archivo .json que esta
     dentro de la carpeta pokedex """
    carpeta_pokedex = "pokedex"

    #Verificamos si la carpeta existe de lo contrario la creara con la funcion
    #.osmakedirs
    if not os.path.exists(carpeta_pokedex):
        os.makedirs(carpeta_pokedex)

    #Almacenamos en la variable archivo_json el nombre del archivo con la extension .json
    archivo_json = os.path.join(carpeta_pokedex, f"{nombre.lower()}.json")
    with open(archivo_json, "w") as archivo:
        json.dump(datos_pokemon2, archivo, indent=4)

def mostrar_pokemon(datos_pokemon3):

    print(f"Nombre del Pokémon: {datos_pokemon3['name'].capitalize()}")

    try:
        url_imagen = datos_pokemon3['sprites']['front_default']
        imagen = Image.open(urlopen(url_imagen))
    except:
            print('Fallo la imagen')       

    plt.title(datos_pokemon3['name'])
    imgplot = plt.imshow(imagen)
    plt.show()
        
    print(f"Peso: {datos_pokemon3['weight']} hectogramos")
    print(f"Tamaño: {datos_pokemon3['height']} decímetros")

    print("Habilidades:")
    for habilidad in datos_pokemon3['abilities']:
        print(f"- {habilidad['ability']['name']}")

    print("Tipos:")
    for tipo in datos_pokemon3['types']:
        print(f"- {tipo['type']['name']}")    
    
#Funcion que imprime todos los datos del pokémon
def main():
    while True:
        """Funcion que realiza  las acciones del Programa principal"""
        print()
        print('************ BIENVENIDO A TU POKEDEX ***********')
        print('Conoce las diferentes habilidades de los Pokémon, ¡Atrapalos Ya!')
        print('\n') 
        nombre_pokemon = input("Introduce el nombre de un Pokémon: ")

        
        datos_pokemon3 = obtener_datos_pokemon(nombre_pokemon)
        
        #Hacemos una condicion en donde si la variable no es none o que si contiene los datos va a empezar a ejecutar las instrucciones que son los datos del pokemon
        if datos_pokemon3 is not None:
            guardar_datos_pokemon_en_json(nombre_pokemon, datos_pokemon3)
            mostrar_pokemon(datos_pokemon3)
            salir = input('¿Deseas buscar otro Pokémon? oprime enter para continuar o 0 + enter, para salir del programa: ' )
            if (salir == '0'):
                break
        else:
            print(f"No se encontró información para el Pokémon {nombre_pokemon}.")

if __name__ == "__main__":
    main()
