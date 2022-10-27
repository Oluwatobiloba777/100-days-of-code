from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# beautiful soup---getting titles using dates----
URL = "https://www.billboard.com/charts/hot-100/"

userInput = input("Which year do you want to travel? Type the date in this format YYYY-MM-DD:")

response = requests.get(URL + userInput)

musicPage = response.text

soup = BeautifulSoup(musicPage, "html.parser")

songs = soup.select(".a-no-trucate")

topHundred = [song.getText().strip() for song in songs]

# print(topHundred)

##spotify urls

CLIENT_APP_ID = "CLIENT APP ID"
CLIENT_APP_SECRET_KEY = "CLIENT APP SECRET KEY"
REDIRECT_URI = "REDIRECT URI"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_APP_ID,
    client_secret=CLIENT_APP_SECRET_KEY,
    redirect_uri=REDIRECT_URI,
    scope="playlist-modify-private",
))

results = sp.current_user()
userId = results['id']

uris = [sp.search(title)['tracks']['items'][0]['uri'] for title in songs]


#playlist

playlist = sp.user_playlist_create(user=userId,public=False,name=f"{userInput} Billboard-100['id")

sp.playlist_add_items(playlist_id=playlist['id'], items=uris)