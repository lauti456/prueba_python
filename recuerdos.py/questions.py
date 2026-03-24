import random

words = ["python", "programa", "variable", "funcion", "bucle", "cadena", "entero", "lista"]
word = random.choice(words)
guessed = []
attempts = 6

print("¡Bienvenido al Ahorcado!\n")


while attempts > 0:
    #todo esto pasa en CADA turno
    progress = ""
    
    #REVISAR LETRA POR LETRA PARA ARMAR LOS "GUIONES"
    for letter in word:
        if letter in guessed:
            progress += letter + " "
        else:
            progress += "_ "
            
    print(progress)

    #COMPROBAR SI GANÓ
    if "_" not in progress:
        print("¡Ganaste!")
        break
        
    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {', '.join(guessed)}")
    
    letter = input("Ingresá una letra: ")
    
    if letter in guessed:
        print("Ya usaste esa letra.")
    elif letter in word:
        guessed.append(letter)
        print("¡Bien! Esa letra está en la palabra.")
    else:
        guessed.append(letter)
        attempts -= 1
        print("Esa letra no está en la palabra.")
    print()


else:
    print(f"¡Perdiste! La palabra era: {word}")