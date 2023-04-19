sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

kod_soucastky = input("Zadejte prosím kód součástky: ")
if kod_soucastky not in sklad:
        print("Vámi požadovaná součástka není skladem.")
else:
    pocet_kusu = int(input("Zadejte prosím počet požadovaných kusů: "))
    if pocet_kusu > sklad[kod_soucastky]:
        print(f"Této součástky máme pouze {sklad[kod_soucastky]} kusů.")
        sklad.pop(kod_soucastky)
        print(f"Na skladě už zbyly jen tyto součástky: {sklad}.")
    else:
        print(f"Na skladě máme dostatečný počet Vámi požadovaného zboží.")
        value = sklad[kod_soucastky] - pocet_kusu
        print(f"Na skladě nyní zbývá pouze {value} ks součástky {kod_soucastky}.")
