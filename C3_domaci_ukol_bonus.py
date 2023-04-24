import json

with open('Dlouhodobý kurz/body.json', encoding='utf-8') as file:
    slovnik1 = json.load(file)

with open('Dlouhodobý kurz/bonusy.json', encoding='utf-8') as file:
    slovnik2 = json.load(file)

    znamky = {}
    for jmeno in slovnik1:
        if jmeno in slovnik2:
            slovnik1[jmeno] = slovnik1[jmeno] + slovnik2[jmeno]
        else:
            pass
        
        if slovnik1[jmeno] >= 90:
            znamka = 1
        elif slovnik1[jmeno] >= 70:
            znamka = 2
        elif slovnik1[jmeno] >= 50:
            znamka = 3
        elif slovnik1[jmeno] >= 30:
            znamka = 4
        else:
            znamka = 5
             
        znamky[jmeno] = znamka

with open('Dlouhodobý kurz/znamky.json', mode = 'w') as file:
    json.dump(znamky, file, ensure_ascii=False)

print(znamky)