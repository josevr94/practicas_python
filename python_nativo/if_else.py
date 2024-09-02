# #Objetivo: Crear un programa que permita al usuario adivinar un número secreto. 
# El programa debe dar una sola oportunidad al usuario para adivinar 
# y debe indicar si el usuario adivinó correctamente o no.

# Instrucciones:

# Genera un número secreto.
# Pide al usuario que adivine el número.
# Usa estructuras if y else para comparar 
# la adivinanza del usuario con el número secreto.
# Indica al usuario si su adivinanza es correcta o no.

# import random

# # Generar un número secreto
# numero_secreto = random.randint(1, 20)

# numero_persona = int(input("Bienvenido al adivinador\n ingresa un numero del 1 al 20: "))

# # Comparar la adivinanza del usuario con el número secreto
# if  numero_persona < 20:
    
#     if  numero_persona != numero_secreto:
#         print(f"Lo siento pero el numero secreto era:  {numero_secreto}")    
#     elif numero_persona == numero_secreto:
#         print("Felicidades, has adivinado el numero secreto!")
# else:
#     print("Porfavor ingresa un numero del 1 al 20")
    
    
###############################################segundo desafio#######
# Título: Sistema de Puntuación Interactivo para un Juego de Niveles

# Descripción:
# Desarrolla un sistema de puntuación interactivo para un juego de niveles utilizando Python.
# El sistema debe cumplir con los siguientes requisitos:

# 1. Utiliza un diccionario para almacenar los jugadores y sus puntuaciones.

# 2. Implementa una lista de niveles (Fácil, Medio, Difícil, Experto)
# y sus correspondientes puntuaciones.

# 3. Recibe información de la consola para simular una ronda de juego:
#    - Pide al usuario que ingrese el nombre del jugador actual.
#    - Solicita el nivel completado por el jugador.
#    - Pregunta por el tiempo que tardó en completar el nivel.

# 4. Valida la entrada del usuario:
#    - Verifica que el jugador exista en el diccionario de jugadores.
#    - Asegúrate de que el nivel ingresado sea válido.
#    - Comprueba que el tiempo ingresado sea un número positivo.

# 5. Actualiza la puntuación del jugador basándote en el nivel completado.

# 6. Incluye un sistema de bonificación: 
# si un jugador completa un nivel Difícil o Experto en 30 segundos o menos, 
# recibe puntos extra.

# 7. Determina el líder actual del juego.
# En caso de empate, muestra todos los jugadores empatados.

# 8. Muestra las puntuaciones actuales de todos los jugadores.

# Restricciones:
# - Utiliza estructuras if-else para la lógica condicional.
# - Emplea operadores lógicos cuando sea necesario.
# - Usa listas y diccionarios para almacenar y manipular datos.
# - Utiliza input() para recibir información del usuario.

# # Lista de niveles con sus respectivos puntos
# niveles = ["Fácil", "Medio", "Difícil", "Experto"]
# puntos_por_nivel = [10, 20, 30, 50]    

jugadores = {"nombre1":"juan","puntos1": 2, "nombre2": "pedro","puntos2": 3, "nombre3": "maria","puntos3":  4}

niveles = {"facil":1,"medio":2,"dificil":3,"experto":4}
puntos = {"facil": 10, "medio":20, "dificil":30, "experto":40}

print("bienvenido al juego de niveles python")
x = input("ingresa el nombre del jugador: ")

if x == jugadores["nombre1"or"nombre2"or"nombre3"]:
    print("muy bien estas en la lista")
    y = input("ingresa el nivel: ")
    z = int(input("ingresa el tiempo: "))
    if y == niveles and z >= 0:
        
        print(f"hola {x}" )
        jugadores[x]+= puntos[y] 
        print(jugadores)
        
        
        
        
        
    else:
        print("el nivel no es valido")    
    
    
else:
    print("no estas en la lista de jugadores")    
