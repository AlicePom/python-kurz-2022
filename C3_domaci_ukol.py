import json

with open('Dlouhodobý kurz/body.json', encoding='utf-8') as file:
    slovnik = json.load(file)

    prospech = {}
    for jmeno, body in slovnik.items():
        if body >= 60:
            prospel = "Pass"
        else:
            prospel = "Fail" 
        prospech[jmeno] = prospel
            
with open('Dlouhodobý kurz/prospech.json', mode = 'w') as file:
    json.dump(prospech, file, ensure_ascii=False)

print(prospech)
