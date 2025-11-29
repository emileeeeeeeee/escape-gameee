import random

def enigme1():
    print("Enigme 1: Combien sa fais 1 + 1?")
    answer = input("Your answer: ")
    if answer == "3":
        print("Bien joué loniiiieeeee")
        return True
    else:
        print("Mauvaise réponse. Réessayez.")
        return False
    

def enigme2():
    print("Ok, cette enigme va être un peu plus dure.")
    with open("nioniiiiieeeee.txt", "a") as f:
        for i in range(50):
            f.write(f"\n{random.randint(1, 1000000000000000000000000)}")
        f.write("3x2x6x9x7x6x0x2x8x2x0x4x5x3x8x7x9x1x4x8x6x5x3x7x9x2x0x1x4x6x8x5x3x7x9x2x0x1 + 2580")
        for i in range(50):
            f.write(f"\n{random.randint(1, 1000000000000000000000000)}")
    reponse = input("Code secret (mets 1 pour un indice) : ")
    if reponse == "1":
        print("Va voir dans tes fichiers ...")
    elif reponse == "2580":
        print("Bien joué loniiiieeeee")
        return True
    else:
        print("Mauvaise réponse. Réessayez.")
        return False
    

    

while True:
    if enigme1():
        if enigme2():
            print("Félicitations! Vous avez réussi toutes les énigmes.")
            input("Le tresor est dans un tiroir de ma chambre, appuie sur Entrée pour terminer le jeu.")
            break