age = int(input("donner votre age: "))
if age > 0:
    if age > 60:
        print("c'est une personne agee")
    elif age < 15 and age > 0:
        print("c'est un enfant")
    else:
        print("c'est un adulte")
else:
    print("entrer votre vrai age")
