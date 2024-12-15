a = float(input("Veuillez entrer le nombre a : "))
b = float(input("Veuillez entrer le nombre b : "))
choix = int(input("Tapez 1 pour une addition ou 2 pour une soustraction : "))
if choix == 1:
    resultat = a + b
    print("Le résultat de a + b est", resultat)
elif choix == 2:
    resultat = a - b
    print("Le résultat de a - b est", resultat)
else:
    print("ERREUR : il faut taper 1 ou 2")