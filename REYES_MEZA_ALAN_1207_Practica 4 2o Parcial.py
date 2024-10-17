# Add your program code here.
print("Welcome to Practica 4 2o Parcial!") # Mensaje de bienvenida al usuario
print(" ")
print("REYES MEZA ALAN EDUARDO_1207 :   3W")  # INFO DE PRACTICA Y PROGRAMADOR 
print(" ")  # ESPACIO

# diccionario vacío
persona = {}

# Solicitar información al usuario

#introduce su nombre
nombre = input("Introduce tu nombre: ")
persona['Nombre'] = nombre

print(persona)
# introduce su domicilio
domicilio = input("Introduce tu domicilio: ")
persona['su domicilio es:'] = domicilio
print(persona)

# introduce año de nacimiento
donde_nacio = input("Introduce donde naciste: ")
persona['nacio en:'] = donde_nacio
print(persona)

# introduce lugar de trabajo
trabaja_en = input("Introduce tu sitio de trabajo: ")
persona['trabaja en:'] = trabaja_en
print(persona)

# año de nacimiento
ano_de_nacimiento = input("Introduce tu año de nacimiento: ")
persona['nacio en el año:'] = ano_de_nacimiento
print(persona)

# su edad
edad = input("Introduce tu edad: ")
persona['tu edad es:'] = edad
print(persona)

# genero
sexo = input("Introduce tu sexo: ")
persona['Sexo'] = sexo
print(persona)

# numero telefonico
telefono = input("Introduce tu telefono: ")
persona['tu numero de telefono:'] = telefono
print(persona)

# correo electronico
correo = input("Introduce tu correo electronico: ")
persona['su correo electronico:'] = correo
print(persona)

# Mostrar la informacion final del usuario
print("\nInformacion final del usuario:")
print(persona)
