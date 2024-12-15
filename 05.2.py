def somme(n):
    resultat = 0
    for i in range(1, n+1):
        resultat = resultat + i
    return resultat

def produit(n):
    resultat = 1
    for i in range(1, n+1):
        resultat = resultat * i
    return resultat

def test(n):
    resultat = 0
    for i in range(1, n+1):
        resultat = resultat + i ** 2
    return resultat

def test2(n):
    resultat = 0
    for i in range(1, n+1):
        resultat = resultat + 1 / i ** 2
    return resultat