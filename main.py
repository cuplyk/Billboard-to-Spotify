from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth


def get_billboard_songs(date):
    """
    Scrapes the Billboard Hot 100 for a given date and returns a list of song names.
    """
    url = f"https://www.billboard.com/charts/hot-100/{date}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    song_names_spans = soup.find_all("span", class_="chart-element__information__song")
    song_names = [song.getText() for song in song_names_spans]
    return song_names


def search_spotify_for_songs(sp, song_names, year):
    """
    Searches Spotify for the given song names and returns a list of song URIs.
    """
    song_uris = []
    for song in song_names:
        query = f"track:{song} year:{year}"
        results = sp.search(q=query, type="track")
        if results["tracks"]["items"]:
            uri = results["tracks"]["items"][0]["uri"]
            song_uris.append(uri)
        else:
            print(f"{song} doesn't exist in Spotify. Skipped.")
    return song_uris


def create_spotify_playlist(sp, user_id, date):
    """
    Creates a new private playlist in the user's Spotify account and returns the playlist object.
    """
    playlist_name = f"{date} Billboard 100"
    playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False)
    return playlist


def add_songs_to_spotify_playlist(sp, playlist_id, song_uris):
    """
    Adds the given song URIs to the specified Spotify playlist.
    """
    sp.playlist_add_items(playlist_id=playlist_id, items=song_uris)


if __name__ == "__main__":
    # Set up Spotify authentication
    scope = "playlist-modify-private"
    redirect_uri = "http://example.com"
    client_id = "YOUR CLIENT ID"
    client_secret = "YOUR CLIENT SECRET"
    cache_path = "token.txt"
    auth_manager = SpotifyOAuth(scope=scope, redirect_uri=redirect_uri, client_id=client_id,
                                client_secret=client_secret, show_dialog=True, cache_path=cache_path)
    sp = spotipy.Spotify(auth_manager=auth_manager)

    # Get user ID from Spotify
    user_id = sp.current_user()["id"]
    print(f"Logged in as {user_id}")

    # Prompt user for date
    date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
    year = date.split("-")[0]

    # Get song names from Billboard
    song_names = get_billboard_songs(date)

    # Search Spotify for songs by title
    song_uris = search_spotify_for_songs(sp, song_names, year)

    # Create a new playlist in Spotify
    playlist = create_spotify_playlist(sp, user_id, date)
    print(f"Created playlist {playlist['name']}")

    # Add songs to the playlist
    add_songs_to_spotify_playlist(sp, playlist["id"], song_uris)
    print("Songs added to playlist") 
