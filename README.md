# 🎵 CLI Lyrics Translator 🎧

A simple yet powerful Python-based CLI tool that fetches the currently playing song from Spotify, retrieves its lyrics using Genius, and automatically translates them into English using Deep Translator.

---

## ✨ Features

- 🔍 Detects the song currently playing on your Spotify account
- 🎤 Fetches lyrics via Genius API
- 🌍 Automatically detects the lyrics' language
- 🔁 Translates non-English lyrics to English using Deep Translator
- ⚡ Lightweight, clean CLI output

---

## 🛠️ Requirements

- Python 3.8+
- Spotify Premium account (required for playback access)
- Genius API token
- `.env` file with your credentials

---

## 📦 Setup

1. **Clone this repo**

```bash
git clone https://github.com/yourusername/cli-lyrics-translator.git
cd cli-lyrics-translator

2. **Install dependencies**
pip install -r requirements.txt

3. **Create a .env file**
SPOTIFY_CLIENT_ID=your_spotify_client_id
SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
SPOTIFY_REDIRECT_URI=http://localhost:8888/callback
GENIUS_ACCESS_TOKEN=your_genius_api_token

4. **Run the script**
python cli_lyrics_google.py

**🧪 Example Output**
🎵 Currently Playing: Despacito by Luis Fonsi
🌐 Detected language: es - Translating to English...

🎶 Lyrics:
Slowly
I want to breathe your neck slowly...
