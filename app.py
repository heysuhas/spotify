import streamlit as st
import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth 

load_dotenv()

SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
SPOTIPY_REDIRECT_URI = os.getenv('SPOTIPY_REDIRECT_URI')

st.set_page_config(page_title="Music Recommendation System", page_icon="🎶")

st.markdown("""
    <link rel="icon" href="https://www.flaticon.com/free-icon/spotify_2111624" type="image/x-icon">
""", unsafe_allow_html=True)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
    redirect_uri=SPOTIPY_REDIRECT_URI,
    scope="playlist-read-private"
))

def get_playlist_tracks(playlist_url):
    """Fetch tracks from the user's playlist."""
    playlist_id = playlist_url.split("/")[-1].split("?")[0]
    results = sp.playlist_tracks(playlist_id)
    track_ids = [item['track']['id'] for item in results['items'] if item['track'] is not None]
    return track_ids

def recommend_songs(track_ids):
    """Get song recommendations based on seed tracks."""
    if len(track_ids) > 5:
        track_ids = track_ids[:5]
    recommendations = sp.recommendations(seed_tracks=track_ids, limit=5)
    return [(track['name'], track['artists'][0]['name']) for track in recommendations['tracks']]

playlist_url = st.text_input("🔗 Enter your Spotify playlist or song URL:")

if st.button("Get Recommendations"):
    if playlist_url:
        try:
            if "track" in playlist_url:  
                track_ids = [playlist_url.split("/")[-1].split("?")[0]]  
            else:
                track_ids = get_playlist_tracks(playlist_url)

            if track_ids:
                recommended_songs = recommend_songs(track_ids)
                st.success("📜 Recommended Songs:")
                for song_name, artist_name in recommended_songs:
                    st.markdown(f"<div class='song'>{song_name} - By {artist_name}</div>", unsafe_allow_html=True)
            else:
                st.warning("No valid tracks found.")
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter a valid Spotify URL.")

st.markdown("""
    <style>
    body {
        background-color: #121212;
        color: #ffffff;
        font-family: 'Helvetica Neue', sans-serif;
        padding: 20px;
    }
    h1 {
        font-size: 2.5rem;
        text-align: center;
        color: #1DB954;
    }
    input {
        width: 100%;
        padding: 15px;
        margin: 20px 0;
        border: 1px solid #1DB954;
        border-radius: 4px;
        background-color: #282828;
        color: #ffffff;
    }
    button {
        background-color: #1DB954;
        color: white;
        padding: 15px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        width: 100%;
    }
    button:hover {
        background-color: #1ed760;
    }
    .song {
        background-color: #1e1e1e;
        padding: 15px;
        border-radius: 5px;
        margin: 10px 0;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.5);
        transition: transform 0.2s, box-shadow 0.2s;
    }
    .song:hover {
        transform: scale(1.02);
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.6);
    }
    footer {
        margin-top: 20px;
        text-align: center;
        color: #aaa;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <footer style="background: linear-gradient(135deg, #7289DA, #40444B); padding: 20px; border-radius: 8px; position: relative;">
        <div style="animation: fade-in 2s; text-align: center;">
            <p style="color: white; font-size: 18px;">Made with ❤️ by Suhas, 2024 | This project uses the Spotify API</p>
            <p style="color: #1DB954;">
                <a href="#privacy-policy" style="color: #1DB954; text-decoration: none;">Privacy Policy</a>
            </p>
        </div>
        <style>
            @keyframes fade-in {
                from {
                    opacity: 0;
                }
                to {
                    opacity: 1;
                }
            }
        </style>
    </footer>
""", unsafe_allow_html=True)
st.markdown("""
    <h2 id="privacy-policy" style="color: #1DB954;">Privacy Policy</h2>
    <p>Your privacy is important to me. This Privacy Policy outlines how I collect, use, and protect your information when you use my Music Recommendation System.</p>
    
    <h3>1. Information I Collect</h3>
    <p>I do not collect or store any personal information from users. The only information processed is the Spotify playlist or song URL you provide, which is used solely for generating song recommendations.</p>
    
    <h3>2. How I Use Your Information</h3>
    <p>The information you enter is utilized to fetch your Spotify data and to generate music recommendations based on your preferences. I do not use this information for any other purpose.</p>
    
    <h3>3. Data Security</h3>
    <p>I am committed to ensuring that your information is secure. I implement appropriate technical and organizational measures to protect the information processed from unauthorized access, disclosure, alteration, or destruction.</p>
    
    <h3>4. Cookies</h3>
    <p>My application may use cookies to enhance user experience. Cookies are small files that are stored on your device. You can choose to accept or decline cookies. Most web browsers automatically accept cookies, but you can usually modify your browser setting to decline cookies if you prefer.</p>
    
    <h3>5. Third-Party Services</h3>
    <p>My application uses the Spotify API to fetch data. Please refer to Spotify's Privacy Policy for information on how they handle your data: <a href="https://www.spotify.com/us/legal/privacy-policy/" target="_blank">Spotify Privacy Policy</a>.</p>
    
    <h3>6. User Rights</h3>
    <p>You have the right to access, rectify, or delete your information. However, as I do not store any personal information, there is no information to access, rectify, or delete.</p>
    
    <h3>7. Changes to This Privacy Policy</h3>
    <p>I may update the Privacy Policy from time to time. I will notify you of any changes by posting the new Privacy Policy on this page. You are advised to review this Privacy Policy periodically for any changes.</p>
    
    <h3>8. Contact Me</h3>
    <p>If you have any questions or concerns about this Privacy Policy, please contact me at [tsuhasgamer@gmail.com].</p>
""", unsafe_allow_html=True)

