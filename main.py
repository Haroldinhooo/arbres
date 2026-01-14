import json
from config import collection

# 1. Injection
with open('data/arbres.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

collection.delete_many({})
collection.insert_many(data)
print(f"{len(data)} arbres.")

print("\nListe des arbres enregistrés")
for arbre in collection.find():
    nom = arbre.get('nom') or arbre.get('nom_commun') or arbre.get('libellefrancais')
    commune = arbre.get('commune') or arbre.get('ville')
    
    nom_final = nom if nom else "Nom inconnu"
    commune_final = commune if commune else "Commune inconnue"
    
    print(f"Arbre : {nom_final} | Commune : {commune_final}")