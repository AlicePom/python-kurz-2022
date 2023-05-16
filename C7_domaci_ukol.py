class Auto:
    def __init__(self, registracni_znacka, typ_vozidla, najete_km):
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.dostupne = True
    
    def pujc_auto(self):
        if self.dostupne:
            text = "Potvrzuji zapůjčení vozidla."
            self.dostupne = False
        else:
            text = "Vozidlo není k dispozici."
        return text

    def get_info(self):
        return f"Automobil {self.typ_vozidla}, registrační značka {self.registracni_znacka}."
    
    def vrat_auto(self, najete_km, pocet_dni_uzivani):
        self.najete_km = najete_km
        self.volne = True

peugeot = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534)
skoda = Auto("1P3 4747", "Škoda Octavia", 41253)

dotaz_na_auto = input("Zadejte prosím typ vozu, který si chcete vypůjčit (Peugeot/Škoda): ")

if dotaz_na_auto == "Peugeot":
    print(peugeot.get_info())
    print(peugeot.pujc_auto())
    print(peugeot.pujc_auto())
    
if dotaz_na_auto == "Škoda":
    print(skoda.get_info())
    print(skoda.pujc_auto())
    print(skoda.pujc_auto())

pocet_dni_uzivani = int(input("Kolik dní jste měl/a auto vypůjčené? "))

if pocet_dni_uzivani < 7:
    print(f"Cena za 1 den vypůjčení je 400 Kč. Prosím, zaplaťte {pocet_dni_uzivani * 400} Kč.")
if pocet_dni_uzivani >= 7:
    print(f"Cena za 1 den vypůjčení je 300 Kč. Prosím, zaplaťte {pocet_dni_uzivani * 300} Kč.") 

najete_km = int(input("Jaky je stav tachometru pri vraceni? "))

if dotaz_na_auto == "Peugeot":
    peugeot.vrat_auto(najete_km, pocet_dni_uzivani)
    print(f"Automobil Peugeot má nyní najeto {najete_km} km.")
if dotaz_na_auto == "Škoda":
    skoda.vrat_auto(najete_km, pocet_dni_uzivani)
    print(f"Automobil Škoda má nyní najeto {najete_km} km.")
