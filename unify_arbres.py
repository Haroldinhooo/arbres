import json
import os

def unify_data():
    unified_arbres = []

    path_paris = 'data-raw/arbres_paris.json'
    if os.path.exists(path_paris):
        with open(path_paris, 'r', encoding='utf-8') as f:
            items = json.load(f)
            for item in items:
                
                nom = item.get("libelle_francais") or item.get("genre")
                
                genre = item.get("genre", "")
                espece = item.get("espece", "")
                latin = f"{genre} {espece}".strip()

                tree = {
                    "source": "Paris",
                    "commune": "Paris",
                    "code_insee": "75000",
                    "nom": nom,
                    "latin": latin if latin else None,
                    "hauteur": item.get("hauteur_m"),
                    "circonference": item.get("circonference_cm"),
                    "location": item.get("geo_point_2d")
                }
                unified_arbres.append(tree)

    path_hds = 'data-raw/arbres_hds.json'
    if os.path.exists(path_hds):
        with open(path_hds, 'r', encoding='utf-8') as f:
            items = json.load(f)
            for item in items:
                circ = item.get("circonference")

                if circ and circ < 10: 
                    circ = circ * 100

                tree = {
                    "source": "Hauts-de-Seine",
                    "commune": item.get("ville"),
                    "code_insee": item.get("code_insee"),
                    "nom": item.get("nom_commun"),
                    "latin": item.get("nom_latin"),
                    "hauteur": item.get("hauteur"),
                    "circonference": circ,
                    "location": item.get("geo_point_2d")
                }
                unified_arbres.append(tree)

    os.makedirs('data', exist_ok=True)
    with open('data/arbres.json', 'w', encoding='utf-8') as f:
        json.dump(unified_arbres, f, indent=4, ensure_ascii=False)  
    
    print(f"{len(unified_arbres)} arbres.")

if __name__ == "__main__":
    unify_data()