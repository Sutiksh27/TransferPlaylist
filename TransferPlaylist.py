import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from dotenv import load_dotenv
load_dotenv()

spotify_client_id = os.getenv('SPOTIFY_CLIENT_ID')
spotify_client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=spotify_client_id, client_secret=spotify_client_secret, redirect_uri="http://localhost:5000", scope="user-library-read playlist-read-private"))

flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", scopes=["https://www.googleapis.com/auth/youtube.force-ssl"])
credentials = flow.run_local_server(port=5000, prompt='consent')

youtube = build('youtube', 'v3', credentials=credentials)

# Search for the song on YouTube
def search_youtube_track(track_name, artist_name):
    search_query = f"{track_name} {artist_name} official audio"
    request = youtube.search().list(q=search_query, type='video', part="id", maxResults=1)
    response = request.execute()
    if 'items' in response:
        youtube_id = response['items'][0]['id']['videoId']
        return youtube_id
    return None

def create_youtube_playlist(playlist_name, playlist_description):
    request = youtube.playlists().insert(
        part="snippet,status",
        body={
          "snippet": {
            "title": playlist_name,
            "description": playlist_description
          },
          "status": {
            "privacyStatus": "private"
          }
        }
    )
    response = request.execute()
    return response['id']

liked_songs_id = create_youtube_playlist('Liked Songs', 'My liked songs from Spotify')
def addSongsToPlaylist(playlist_id):
    # Get the user's playlists
    likedSongs = sp.current_user_saved_tracks()
    for song in likedSongs['items']:
        # print(song['track']['name'] + ' - ' + song['track']['artists'][0]['name'])
        track_name = song['track']['name']
        artist_name = song['track']['artists'][0]['name']
        youtube_id = search_youtube_track(track_name, artist_name)
        if youtube_id is not None:
            request = youtube.playlistItems().insert(
                part="snippet",
                body={
                    "snippet": {
                        "playlistId": playlist_id,
                        "position": 0,
                        "resourceId": {
                            "kind": "youtube#video",
                            "videoId": youtube_id
                        }
                    }
                }
            )
            response = request.execute()
            print(response)

addSongsToPlaylist(liked_songs_id)
