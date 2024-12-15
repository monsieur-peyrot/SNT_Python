a = float(input("Veuillez entrer le nombre a : "))
b = float(input("Veuillez entrer le nombre b : "))
choix = int(input("Tapez 1 pour +, 2 pour -, 3 pour * ou 4 pour / : "))
if choix == 1:
    resultat = a + b
    print("On a :", a, "+", b, "=", resultat)
elif choix == 2:
    resultat = a - b
    print("On a :", a, "-", b, "=", resultat)
elif choix == 3:
    resultat = a * b
    print("On a :", a, "*", b, "=", resultat)
elif choix == 4:
    if b != 0:
        resultat = a / b
        print("On a :", a, "/", b, "=", resultat)
    else:
        print("ERREUR : on ne peut pas diviser par zéro !")
else:
    print("ERREUR : il faut taper 1, 2, 3 ou 4")