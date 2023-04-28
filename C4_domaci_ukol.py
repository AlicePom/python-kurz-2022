import math

tel_cislo = input("Zadejte prosím telefonní číslo, na které chcete zprávu zaslat: ")
tel_cislo = tel_cislo.replace(" ", "")

def overeni(tel_cislo):
    if len(tel_cislo) == 13 and tel_cislo[0:4] == "+420":
        return True
    elif len(tel_cislo) == 9:
        return True
    else:
        return False
print(overeni(tel_cislo))


def cena_zpravy(zprava):
    delka = int(len(zprava))
    cena_za_1_SMS = 3
    pocet_SMS = math.ceil(delka / 180)
    cena = cena_za_1_SMS * pocet_SMS
    return cena

if overeni(tel_cislo):
    zprava = input("Zadejte prosím zprávu, kterou chcete odeslat: ")
    print(f"Cena za zprávu je {cena_zpravy(zprava)} Kč.")
else:
    print("Číslo je zadané v nesprávném formátu.")
