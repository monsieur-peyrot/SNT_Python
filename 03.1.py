annee_naissance = int(input("Entrez votre année de naissance : "))
annee_courante = 2021   # à modifier le cas échéant
if annee_naissance < 1900 or annee_naissance > annee_courante:
    print("ERREUR : l'année doit être comprise entre 1900 et", annee_courante)
else:
    age = annee_courante - annee_naissance
    print("Il y a", age, "ans entre", annee_naissance, "et", annee_courante)