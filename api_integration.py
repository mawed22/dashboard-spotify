import requests
import pandas as pd
from dotenv import load_dotenv
import os

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

def get_spotify_token(client_id, client_secret):
    """
    Obtenir un jeton d'accès Spotify en utilisant les identifiants client.

    Arguments :
        client_id (str) : Votre ID client API Spotify.
        client_secret (str) : Votre secret client API Spotify.

    Retourne :
        str : Le jeton d'accès.
    """
    auth_url = 'https://accounts.spotify.com/api/token'
    auth_response = requests.post(auth_url, {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
    })
    auth_data = auth_response.json()
    return auth_data['access_token']

def search_track(track_name, artist_name, token):
    """
    Rechercher une piste sur Spotify et récupérer son ID.

    Arguments :
        track_name (str) : Le nom de la piste.
        artist_name (str) : Le nom de l'artiste.
        token (str) : Jeton d'accès API Spotify.

    Retourne :
        str ou None : L'ID de la piste si trouvé, sinon None.
    """
    query = f"{track_name} artist:{artist_name}"
    url = f"https://api.spotify.com/v1/search?q={query}&type=track"
    response = requests.get(url, headers={
        'Authorization': f'Bearer {token}'
    })
    json_data = response.json()
    try:
        first_result = json_data['tracks']['items'][0]
        return first_result['id']
    except (KeyError, IndexError):
        return None

def get_track_details(track_id, token):
    """
    Récupérer les détails d'une piste, comme l'URL de l'image de l'album, depuis Spotify.

    Arguments :
        track_id (str) : L'ID de la piste Spotify.
        token (str) : Jeton d'accès API Spotify.

    Retourne :
        str : L'URL de l'image de l'album.
    """
    url = f"https://api.spotify.com/v1/tracks/{track_id}"
    response = requests.get(url, headers={
        'Authorization': f'Bearer {token}'
    })
    json_data = response.json()
    return json_data['album']['images'][0]['url']

def main():
    """
    Fonction principale pour récupérer les détails des pistes Spotify et mettre à jour un DataFrame.
    """
    # Identifiants API Spotify depuis le fichier .env
    client_id = os.getenv('SPOTIFY_CLIENT_ID')
    client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')

    if not client_id or not client_secret:
        raise ValueError("L'ID client et le secret Spotify doivent être définis dans le fichier .env.")

    # Obtenir le jeton d'accès
    access_token = get_spotify_token(client_id, client_secret)

    # Lire le DataFrame à partir d'un fichier CSV
    input_file = 'spotify-2023.csv'
    output_file = 'spotify-2025.csv'
    df_spotify = pd.read_csv(input_file, encoding='ISO-8859-1')

    # Parcourir chaque ligne pour récupérer les détails des pistes et les ajouter au DataFrame
    for i, row in df_spotify.iterrows():
        track_id = search_track(row['track_name'], row['artist_name'], access_token)
        if track_id:
            image_url = get_track_details(track_id, access_token)
            df_spotify.at[i, 'image_url'] = image_url

    # Sauvegarder le DataFrame mis à jour dans un nouveau fichier CSV
    df_spotify.to_csv(output_file, index=False)
    print(f"Fichier mis à jour sauvegardé sous : {output_file}")

if __name__ == "__main__":
    main()
