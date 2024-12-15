n = int(input("Entrez un nombre entier compris entre 0 et 10 inclus : "))
if n < 0 or n > 10:
    print("ERREUR : le nombre doit être entre 0 et 10 !")
else:
    for i in range(0, 11):
        print(i, "*", n, "=", i * n)