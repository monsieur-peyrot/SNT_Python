import random
jeu = 1
while jeu == 1:
    print()
    running = 1
    nombre_essais = 0
    nombre_mystere = random.randint(1, 100)
    while running == 1:
        nombre_essais = nombre_essais + 1
        print("Ceci est votre essai numéro", nombre_essais)
        correct = 0
        while correct == 0:
            nombre_joueur = int(input("Entrez un nombre entre 1 et 100 : "))
            if nombre_joueur >= 1 and nombre_joueur <= 100:
                correct = 1
            else:
                print("Le nombre entré est incorrect ! Recommencez !")
        if nombre_joueur < nombre_mystere:
            print("Le nombre cherché est plus grand que", nombre_joueur)
        elif nombre_joueur > nombre_mystere:
            print("Le nombre cherché est plus petit que", nombre_joueur)
        else:
            running = 0
    print("Vous avez trouvé le nombre mystérieux en", nombre_essais, "coups")
    print()
    correct = 0
    while correct == 0:
        reponse = input("Voulez-vous rejouer (oui ou non) ? ")
        if reponse == "oui":
            correct = 1
        elif reponse == "non":
            correct = 1
            jeu = 0
        else:
            print("Réponse incorrecte !")
print()
print("Au revoir ! Merci d'avoir joué avec moi !")