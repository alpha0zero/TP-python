poids = float(input("entrer votre poids: "))
taille = float(input("entrer votre taille: "))

if taille != 0:
    imc = poids/taille**2
    print("l'indice de masse corporelle est:", imc)
else:
    print("entrer une taille valide")
