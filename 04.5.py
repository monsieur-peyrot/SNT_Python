n = int(input("Entrez un nombre entier compris entre 0 et 10 inclus : "))
while n < 0 or n > 10:
    print("ERREUR : le nombre doit être compris entre 0 et 10 !")
    n = int(input("Veuillez recommencer en entrant un nombre valide : "))
for i in range(0, 11):
    print(i, "*", n, "=", i * n)