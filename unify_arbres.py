import json
import os

def unify_data():
    unified_arbres = []

    if os.path.exists('data-raw/arbres_paris.json'):
        with open('data-raw/arbres_paris.json', 'r', encoding='utf-8') as f:
            paris_data = json.load(f)
            for item in paris_data:
                fields = item 
                
                tree = {
                    "source": "Paris",
                    "id_externe": fields.get("idbase"),
                    "nom_commun": fields.get("libelle_francais"),
                    "genre": fields.get("genre"),
                    "espece": fields.get("espece"),
                    "circonference_cm": fields.get("circonference_cm"),
                    "hauteur_m": fields.get("hauteur_m"),
                    "stade_developpement": fields.get("stade_developpement"),
                    "adresse": f"{fields.get('adresse', '')} {fields.get('arrondissement', '')}".strip(),
                    "geo": fields.get("geo_point_2d")
                }
                unified_arbres.append(tree)

    if os.path.exists('data-raw/arbres_hds.json'):
        with open('data-raw/arbres_hds.json', 'r', encoding='utf-8') as f:
            hds_data = json.load(f)
            for item in hds_data:
                tree = {
                    "source": "Hauts-de-Seine",
                    "id_externe": item.get("objectid"),
                    "nom_commun": item.get("nom_commun"),
                    "genre": item.get("genre"),
                    "espece": item.get("espece"),
                    "circonference_cm": item.get("circonference"), 
                    "hauteur_m": item.get("hauteur"),
                    "stade_developpement": item.get("stade_de_developpement"),
                    "adresse": f"{item.get('nom_du_site', '')} - {item.get('ville', '')}".strip(),
                    "geo": item.get("geo_point_2d")
                }
                unified_arbres.append(tree)

    os.makedirs('data', exist_ok=True)

    with open('data/arbres.json', 'w', encoding='utf-8') as f:
        json.dump(unified_arbres, f, indent=4, ensure_ascii=False)
    
    print(f"{len(unified_arbres)} arbres dans data/arbres.json")

if __name__ == "__main__":
    unify_data()