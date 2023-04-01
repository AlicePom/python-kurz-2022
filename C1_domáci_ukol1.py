# Domácí úkol - část 1
jmeno = input("Zadejte prosím Vaše křestní jméno: ")
print(f"{jmeno}@czechitas.cz")

# Domácí úkol - část 2 - bonus
jmeno = input("Zadejte prosím Vaše křestní jméno: ")
prijmeni = input("Zadejte prosím Vaše příjmení: ")
jmeno_a_prijmeni = jmeno + " " + prijmeni
print(jmeno_a_prijmeni.upper())
print(jmeno_a_prijmeni.lower())
print(f"{jmeno[0].upper()}{jmeno[1:].lower()} {prijmeni[0].upper()}{prijmeni[1:].lower()}")
print(f"{jmeno[0].upper()}. {prijmeni[0].upper()}.")

if len(jmeno) > 5:
    print(f"{jmeno[0].upper()}. {prijmeni[0].upper()}{prijmeni[1:].lower()}")
else:
    print(f"{jmeno[0].upper()}{jmeno[1:].lower()} {prijmeni[0].upper()}{prijmeni[1:].lower()}")


