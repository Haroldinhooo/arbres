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
                f_data = item.get('fields', item)
                
                genre = f_data.get("genre", "")
                espece = f_data.get("espece", "")
                nom_latin = f"{genre} {espece}".strip()

                tree = {
                    "source": "Paris",
                    "commune": "Paris",
                    "code_insee": "75000",
                    "nom": f_data.get("libellefrancais"),
                    "latin": nom_latin if nom_latin else None,
                    "hauteur": f_data.get("hauteurenm"),
                    "circonference": f_data.get("circonferenceencm"),
                    "location": f_data.get("geo_point_2d")
                }
                unified_arbres.append(tree)

    path_hds = 'data-raw/arbres_hds.json'
    if os.path.exists(path_hds):
        with open(path_hds, 'r', encoding='utf-8') as f:
            data = json.load(f)
            items = data.get('records', data) if isinstance(data, dict) else data
            
            for item in items:
                f_data = item.get('fields', item)
                
                circ = f_data.get("circonference")
                if circ and circ < 20: 
                    circ = circ * 100
                
                tree = {
                    "source": "Hauts-de-Seine",
                    "commune": f_data.get("ville") or f_data.get("commune"),
                    "code_insee": f_data.get("code_insee"),
                    "nom": f_data.get("nom_commun"),
                    "latin": f_data.get("nom_latin"),
                    "hauteur": f_data.get("hauteur"),
                    "circonference": circ,
                    "location": f_data.get("geo_point_2d")
                }
                unified_arbres.append(tree)

    os.makedirs('data', exist_ok=True)
    with open('data/arbres.json', 'w', encoding='utf-8') as f:
        json.dump(unified_arbres, f, indent=4, ensure_ascii=False)
    
    print(f"{len(unified_arbres)} arbres unifiés avec succès.")

if __name__ == "__main__":
    unify_data()