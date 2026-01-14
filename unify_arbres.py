import json
import os

def unify_data():
    unified_arbres = []

    if os.path.exists('data-raw/arbres_paris.json'):
        with open('data-raw/arbres_paris.json', 'r', encoding='utf-8') as f:
            paris_data = json.load(f)
            for item in paris_data:
                genre = item.get("genre", "")
                espece = item.get("espece", "")
                nom_latin = f"{genre} {espece}".strip()

                tree = {
                    "source": "Paris",
                    "commune": "Paris",
                    "code_insee": "75000", 
                    "nom": item.get("libelle_francais"),
                    "latin": nom_latin if nom_latin else None,
                    "hauteur": item.get("hauteur_m"),
                    "circonference": item.get("circonference_cm"),
                    "location": item.get("geo_point_2d")
                }
                unified_arbres.append(tree)

    if os.path.exists('data-raw/arbres_hds.json'):
        with open('data-raw/arbres_hds.json', 'r', encoding='utf-8') as f:
            hds_data = json.load(f)
            for item in hds_data:
                tree = {
                    "source": "Hauts-de-Seine",
                    "commune": item.get("ville"),
                    "code_insee": item.get("code_insee"),
                    "nom": item.get("nom_commun"),
                    "latin": item.get("nom_latin"), 
                    "hauteur": item.get("hauteur"),
                    "circonference": item.get("circonference"),
                    "location": item.get("geo_point_2d")
                }
                unified_arbres.append(tree)

    os.makedirs('data', exist_ok=True)

    with open('data/arbres.json', 'w', encoding='utf-8') as f:
        json.dump(unified_arbres, f, indent=4, ensure_ascii=False)
    
    print(f"{len(unified_arbres)} arbres unifiés dans 'data/arbres.json'")

if __name__ == "__main__":
    unify_data()