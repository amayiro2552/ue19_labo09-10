import requests

def fetch_pun():
    url = 'https://punapi.rest/api/pun'  # L'URL de l'API de blagues
    headers = {'Accept': 'application/json'}  # Les en-têtes spécifiant le format de réponse souhaité (JSON)

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        pun = response.json()['pun']
        return pun  # Renvoie la blague si la requête est réussie (statut 200)
    else:
        return "Impossible de récupérer un jeu de mots pour le moment."  # Renvoie un message d'erreur si la requête échoue

if __name__ == "__main__":
    joke = fetch_pun()
    print("Voici un jeu de mots :")
    print(joke)  # Affiche la blague récupérée depuis l'API
