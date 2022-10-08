temperature = int(input("entrer la temperature: "))

if temperature > 100:
    print("gazeux")
elif temperature <= 100 and temperature >= 0:
    print("liquide")
else:
    print("solide")
