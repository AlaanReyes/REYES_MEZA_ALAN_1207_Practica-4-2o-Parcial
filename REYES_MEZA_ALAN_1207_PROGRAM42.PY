# Add your program code here.
print("Welcome to Practica 4 2o Parcial!") # Mensaje de bienvenida al usuario
print(" ")
print("REYES MEZA ALAN EDUARDO_1207 :   3W")  # INFO DE PRACTICA Y PROGRAMADOR 
print(" ")  # ESPACIO

def crear_diccionario(entradas):
    diccionario = {}
    for entrada in entradas.split(','):
        palabra, traduccion = entrada.split(':')
        diccionario[palabra.strip()] = traduccion.strip()
    return diccionario

def traducir_frase(diccionario, frase):
    palabras = frase.split()
    traduccion = []
    for palabra in palabras:
        traduccion.append(diccionario.get(palabra, palabra))  # Si no está en el diccionario, deja la palabra sin traducir
    return ' '.join(traduccion)

# Entrada de pares de palabras
entradas = input("Introduce las palabras en español e inglés (formato: español:inglés, ...): ")
diccionario = crear_diccionario(entradas)

# Entrada de la frase en español a traducir
frase = input("Introduce una frase en español: ")
traduccion = traducir_frase(diccionario, frase)

print("Traducción:", traduccion)
