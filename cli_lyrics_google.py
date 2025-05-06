import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import lyricsgenius
import platform
#import openai 
#from openai import OpenAI
from deep_translator import GoogleTranslator
from langdetect import detect
from dotenv import load_dotenv
import time


# Load environment variables from .env file
load_dotenv()

# Clear the console for better readability
os.system('cls' if platform.system() == 'Windows' else 'clear')

# Set your credentials from environment variables
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
SPOTIFY_REDIRECT_URI = os.getenv("SPOTIFY_REDIRECT_URI")
GENIUS_ACCESS_TOKEN = os.getenv("GENIUS_ACCESS_TOKEN")
#OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client
#client = OpenAI(api_key=OPENAI_API_KEY)

# Initialize APIs
#openai.api_key = OPENAI_API_KEY
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri=SPOTIFY_REDIRECT_URI,
    scope="user-read-playback-state"
))
genius = lyricsgenius.Genius(GENIUS_ACCESS_TOKEN)

def get_current_song():
    try:
        current = sp.current_playback()
        if not current or not current.get("is_playing"):
            print("No song is currently playing.")
            return None, None

        track = current["item"]
        song_name = track["name"]
        artist_name = track["artists"][0]["name"]
        print(f"🎵 Currently Playing: {song_name} by {artist_name}")
        return song_name, artist_name
    except Exception as e:
        print(f"Error fetching current song: {e}")
        return None, None

def fetch_lyrics(song, artist):
    try:
        song_data = genius.search_song(song, artist)
        if song_data and song_data.lyrics:
            return song_data.lyrics
        return "Lyrics not found."
    except Exception as e:
        return f"Error fetching lyrics: {e}"

def translate_to_english(text):
    try:
        detected_lang = detect(text)
        if detected_lang == 'en':
            print("🌐 Detected language: English - No translation needed.")
            return text
        print(f"🌐 Detected language: {detected_lang} - Translating to English...")
        return GoogleTranslator(source=detected_lang, target='en').translate(text)
    except Exception as e:
        return f"Error in translation: {str(e)}"

## Using OpenAI for translation instead of Google Translate
## This is a more advanced translation method that can handle complex lyrics and idiomatic expressions better than Google Translate.
## It also allows for more customization in the translation process, such as specifying the tone or style of the translation.
## BUT BUT KEEP REMEMBER THAT THIS IS A PAID SERVICE AND YOU WILL BE CHARGED FOR THE API USAGE.
# def translate_to_english(text):
#     try:
#         detected_lang = detect(text)
#         if detected_lang == 'en':
#             print("🌐 Detected language: English - No translation needed.")
#             return text
#         print(f"🌐 Detected language: {detected_lang} - Translating to English...")
#         response = client.chat.completions.create(
#             model="gpt-4o",
#             messages=[
#                 {"role": "user", "content": f"Translate the following song lyrics to English:\n\n{text}"}
#             ]
#         )
#         return response.choices[0].message.content.strip()
#     except Exception as e:
#         return f"Error in translation: {str(e)}"

def main():
    last_song = None
    last_artist = None

    print("🎵 CLI Lyrics Translator is running... (Press Ctrl+C to stop)\n")

    try:
        while True:
            song, artist = get_current_song()
            if song and artist and (song != last_song or artist != last_artist):
                last_song, last_artist = song, artist
                time.sleep(2)  # optional delay
                lyrics = fetch_lyrics(song, artist)
                print("\n🎶 Lyrics:\n")
                translated = translate_to_english(lyrics)
                print(translated)
                print("\n--- Waiting for next song ---\n")
            time.sleep(5)  # check every 5 seconds
    except KeyboardInterrupt:
        print("\n👋 Stopped by user. Goodbye!")

if __name__ == "__main__":
    main()
