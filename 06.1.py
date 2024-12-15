import random
N = int(input("Entrez le nombre de lancers (de 1 à 10) : "))
if N < 0 or N > 10:
    print("Nombre de lancers incorrect !")
else:
    for i in range(1, N+1):
        print("Lancer n", i, "=", random.randint(1, 6))