import random
N = int(input("Entrez le nombre de lancers (de 1 à 10) : "))
for i in range(1, N+1):
    D1 = random.randint(0, 9)
    D2 = random.randint(0, 9)
    resultat = D1 * 10 + D2
    print("Lancer n", i, "=", resultat)