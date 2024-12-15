import random
T = int(input("Quel type de dé voulez-vous lancer ? (1=D4, 2=D6, 3=D8, 4=D10, 5=D12, 6=D20 :"))
if T < 1 or T > 6:
    print("Type de dé inconnu !")
else:
    if T == 1:
        nombre_faces = 4
    elif T == 2:
        nombre_faces = 6
    elif T == 3:
        nombre_faces = 8
    elif T == 4:
        nombre_faces = 10
    elif T == 5:
        nombre_faces = 12
    else:
        nombre_faces = 20
    N = int(input("Entrez le nombre de lancers : "))
    for i in range(1, N+1):
        print("Lancer n", i, "=", random.randint(1, nombre_faces))