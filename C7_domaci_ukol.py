class Auto:
    def __init__(self, registracni_znacka, typ_vozidla, najete_km):
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.dostupne = True
    
    def pujc_auto(self):
        if self.dostupne:
            text = f"Potvrzuji zapůjčení vozidla."
        else:
            text = f"Vozidlo není k dispozici."
        return text

    def get_info(self):
        return f"Automobil {self.typ_vozidla}, registrační značka {self.registracni_znacka}."
    
    def vrat_auto(self, stav_tachometru_vraceni, pocet_dni_uzivani):
        self.stav_tachometru_vraceni = stav_tachometru_vraceni
        self.pocet_dni_uzivani = pocet_dni_uzivani
        self.volne = True
        """ 
        # Funkce mi nefunguje, viz níže line 51, neumím ji zavolat

        if pocet_dni_uzivani < 7:
            cena = f"Cena za 1 den vypůjčení je 400 Kč. Prosím, zaplaťte {self.pocet_dni_uzivani * 400} Kč."
        elif pocet_dni_uzivani >= 7:
            cena = f"Cena za 1 den vypůjčení je 300 Kč. Prosím, zaplaťte {self.pocet_dni_uzivani * 300} Kč."
        return cena 
        """

Peugeot = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534)
Škoda = Auto("1P3 4747", "Škoda Octavia", 41253)

dotaz_na_auto = input("Zadejte prosím typ vozu, který si chcete vypůjčit (Peugeot/Škoda): ")

if dotaz_na_auto == "Peugeot":
    print(Peugeot.get_info())
    print(Peugeot.pujc_auto())
    Peugeot.dostupne = False
    # self.dostupne = False
    
if dotaz_na_auto == "Škoda":
    print(Škoda.get_info())
    print(Škoda.pujc_auto())
    Škoda.dostupne = False
    # self.dostupne = False

pocet_dni_uzivani = int(input("Kolik dní jste měl/a auto vypůjčené? "))
# "print(pocet_dni_uzivani.vrat_auto())" nefunguje, funkci neumím zavolat

# Toto (asi ne požadované) řešení mi původně (nejak) fungovalo, pak jsem se snažila řešení modifikovat (neuložila jsem si původní) a nyní nefunguje, hlásí mi to ValueError: invalid literal for int() with base 10: ''
if pocet_dni_uzivani < 7:
    print(f"Cena za 1 den vypůjčení je 400 Kč. Prosím, zaplaťte {pocet_dni_uzivani * 400} Kč.")
if pocet_dni_uzivani >= 7:
    print(f"Cena za 1 den vypůjčení je 300 Kč. Prosím, zaplaťte {pocet_dni_uzivani * 300} Kč.") 









