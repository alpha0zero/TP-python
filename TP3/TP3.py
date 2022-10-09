age = int(input("entrer votre age: "))
if age > 0:
    print(f"la personne a {age} {'ans' if age > 1 else 'an'}")
else:
    print("entrer votre vrai age")
