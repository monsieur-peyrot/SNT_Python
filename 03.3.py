a = float(input("Veuillez entrer le nombre a : "))
b = float(input("Veuillez entrer le nombre b : "))
choix = int(input("Tapez 1 pour +, 2 pour -, 3 pour * ou 4 pour / : "))
if choix == 1:
    resultat = a + b
    print("Le résultat de l'opération est", resultat)
elif choix == 2:
    resultat = a - b
    print("Le résultat de l'opération est", resultat)
elif choix == 3:
    resultat = a * b
    print("Le résultat de l'opération est", resultat)
elif choix == 4:
    resultat = a / b
    print("Le résultat de l'opération est", resultat)
else:
    print("ERREUR : il faut taper 1, 2, 3 ou 4")