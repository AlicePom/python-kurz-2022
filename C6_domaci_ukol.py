""" domaci ukol 6

bod 1 - řešení: 
(\d{1,2}(\. ?|/)){2}\d{4}
nebo složitějsí varianta:
\d{1,2}(\.|\. |/)\d{1,2}(\.|\. |/)\d{4}

bod 2 - řešení:
\d{3} ?\d{2} +(\w+ ?)+ 

"""


""" 
bonusová úloha:
"""
import re

jmeno = input("Zadejte prosím Vaše přihlašovací jméno: ")
regularni_vyraz_jmeno = re.compile(r"[a-zA-Z]{6,10}")
overeni_jmeno = regularni_vyraz_jmeno.fullmatch(jmeno)

if overeni_jmeno:
    print("Přihlašovací jméno je v pořádku.")
else:
    print("Nesprávně zadané přihlašovací jméno!")

email = input("Zadejte prosím Vaši e-mailovou adresu: ")
regularni_vyraz_email = re.compile(r"([a-zA-Z0-9_]|\")?[a-zA-Z0-9_]+\.?(\w|\+|\-|\")+\.?(\w|\")+@(\w+|\[|\])+(\.|\+|\-|\")?(\w+\.)+(\w+|\[|\])+")
overeni_email = regularni_vyraz_email.fullmatch(email)
# níže jsou zaindexované moje jednoušší, ale méně dokonalé pokusy o regulární výraz:
# \w+\.?\w+@(\w+\.)+\w+
# \w+(\.\w+)*@(\w+\.)+\w+
# ([a-zA-Z0-9_]|\")+\w*\.?(\w|\+|\-|\")+\.?(\w|\")+@(\w+\.)+\w+

if overeni_email:
    print("Zadaná e-mailová adresa je v pořádku.")
else:
    print("Nesprávně zadaná e-mailová adresa!")

heslo = input("Zadejte prosím Vaše heslo: ")
regularni_vyraz_heslo = re.compile(r"[a-zA-Z0-9_\-\.\+\=]{12,30}")
overeni_heslo = regularni_vyraz_heslo.fullmatch(heslo)
# nebo: [\w\-\.\+\=]{12,30} # toto řešení je obecnější, poněvadž povoluje i symboly jako např. あいうえお

if overeni_heslo:
    print("Zadané heslo je v pořádku.")
else:
    print("Nesprávně zadané heslo!")
