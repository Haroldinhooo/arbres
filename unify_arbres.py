import json
import os

def unify_data():
    unified_arbres = []

    path_paris = 'data-raw/arbres_paris.json'
    if os.path.exists(path_paris):
        with open(path_paris, 'r', encoding='utf-8') as f:
            data = json.load(f)
            items = data.get('records', data) if isinstance(data, dict) else data
            
            for item in items:
                f = item.get('fields', item)
                
                tree = {
                    "source": "Paris",
                    "commune": "Paris",
                    "code_insee": "75000",
                    "nom": f.get("libelle_francais") or f.get("genre"),
                    "latin": f"{f.get('genre', '')} {f.get('espece', '')}".strip(),
                    "hauteur": f.get("hauteur_m"),
                    "circonference": f.get("circonference_cm"),
                    "location": f.get("geo_point_2d")
                }
                unified_arbres.append(tree)

    path_hds = 'data-raw/arbres_hds.json'
    if os.path.exists(path_hds):
        with open(path_hds, 'r', encoding='utf-8') as f:
            data = json.load(f)
            items = data.get('records', data) if isinstance(data, dict) else data
            
            for item in items:
                f = item.get('fields', item)
                
                circ = f.get("circonference")
                if circ and circ < 20: 
                    circ = circ * 100
                
                tree = {
                    "source": "Hauts-de-Seine",
                    "commune": f.get("ville"),
                    "code_insee": f.get("code_insee"),
                    "nom": f.get("nom_commun"),
                    "latin": f.get("nom_latin"),
                    "hauteur": f.get("hauteur"),
                    "circonference": circ,
                    "location": f.get("geo_point_2d")
                }
                unified_arbres.append(tree)

    os.makedirs('data', exist_ok=True)
    with open('data/arbres.json', 'w', encoding='utf-8') as f:
        json.dump(unified_arbres, f, indent=4, ensure_ascii=False)
    
    print(f"{len(unified_arbres)} arbres.")

if __name__ == "__main__":
    unify_data()