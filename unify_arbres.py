import json
import os

def unify_data():
    unified_arbres = []

    if os.path.exists('data-raw/arbres_paris.json'):
        with open('data-raw/arbres_paris.json', 'r', encoding='utf-8') as f:
            paris_data = json.load(f)
            for item in paris_data:
                tree = {
                    "source": "Paris",
                    "nom": item.get("nom_commun"),
                    "espece": item.get("espece"),
                    "adresse": item.get("adresse"),
                    "geo": item.get("geo_point_2d")
                }
                unified_arbres.append(tree)

    if os.path.exists('data-raw/arbres_hds.json'):
        with open('data-raw/arbres_hds.json', 'r', encoding='utf-8') as f:
            hds_data = json.load(f)
            for item in hds_data:
                tree = {
                    "source": "Hauts-de-Seine",
                    "nom": item.get("nom_commun"),
                    "espece": item.get("espece"),
                    "adresse": item.get("commune"),
                    "geo": item.get("geo_point_2d")
                }
                unified_arbres.append(tree)

    with open('data/arbres.json', 'w', encoding='utf-8') as f:
        json.dump(unified_arbres, f, indent=4, ensure_ascii=False)
    
    print(f"{len(unified_arbres)} arbres unifiés dans data/arbres.json")

if __name__ == "__main__":
    unify_data()