# TransferPlaylist

#### An application to transfer your liked songs from Spotify library to YouTube music Playlist

## Story behind the app:
##### Spotify is removing some old Hindi songs so I am planning to switch to Youtube music, and I don't want to manually search and add all the songs myself so I created this application

## Steps to run the program:
##### 1. Setup Developer Accounts
###### -> Register as a developer on the Spotify Developer Dashboard (https://developer.spotify.com/dashboard/) and the Google Developers Console (https://console.developers.google.com/). Create a new app on both platforms to get the necessary API keys and credentials.
##### 2. Install Required Libraries
###### -> You'll need to install the following Python libraries using pip:

    pip install spotipy google-auth google-auth-oauthlib google-auth-httplib2 youtube-data-api python-dotenv

##### 3. Get your access keys:
###### -> Create an app in Spotify API and choose Redirect URI as localhost:XXXX, it will generate your API keys (client id, client secret). Paste the client ID and secret in the ".env" file with the same name as written in the Python script.
###### -> Create an app in the Google developer console, then go to credentials and create the OAuth2 key for Google API, also Enable Youtube Data API v3 for the secret key. Then, go to the OAuth consent screen, check if the publishing status of the app is in testing, set the user type to external, and add your email ID as a test user. Download the OAuth2 credentials file and place it in the same folder as the Python file and rename it to "client_secret".
##### 4. Run the app:
###### -> Finally, you can just run your python code and see the magic happen.

Note: I believe there is a limit of 20 in the spotify API, so it only fetches 20 songs for now I will be changing it in the future. Stay Tuned!


 
