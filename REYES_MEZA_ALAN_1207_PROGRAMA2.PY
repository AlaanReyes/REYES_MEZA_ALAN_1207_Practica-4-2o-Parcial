# Add your program code here.
print("Welcome to Practica 4 2o Parcial!") # Mensaje de bienvenida al usuario
print(" ")
print("REYES MEZA ALAN EDUARDO_1207 :   3W")  # INFO DE PRACTICA Y PROGRAMADOR 
print(" ")  # ESPACIO

# diccionario vacío para las traducciones
diccionario = {}

# Solicitar al usuario que introduzca las traducciones
entrada = input("Introduce las palabras en espanol e ingles (formato: espanol:ingles, ...): ")

# Separar las traducciones y llenar el diccionario
for par in entrada.split(','):
    espanol, ingles = par.split(':')
    diccionario[espanol.strip().lower()] = ingles.strip().lower()

# Mostrar el diccionario creado
print("\nDiccionario de traduccion:")
print(diccionario)

# Solicitar una frase en espanol para traducir
frase = input("\nIntroduce una frase en espanol para traducir: ")

# Traducir la frase palabra por palabra
traduccion = []
for palabra in frase.split():
    # Traducir o dejar la palabra sin traducir
    traduccion.append(diccionario.get(palabra.strip().lower(), palabra))

# Mostrar la traducción
frase_traducida = ' '.join(traduccion)
print("\nFrase traducida:")
print(frase_traducida)
