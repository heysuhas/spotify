
# Spotify Music Recommendation System

This project is a **Music Recommendation System** built using Streamlit and Spotify API. It allows users to input their Spotify playlist, and the system recommends five more songs based on the playlist's musical attributes. The goal is to provide song recommendations tailored to users' preferences for an enhanced music discovery experience.

## Features
- Takes a Spotify playlist URL as input.
- Fetches data from Spotify using Spotipy.
- Recommends five new songs based on the input playlist.
- Tailored song suggestions for enhanced accuracy.

## How it Works
1. Enter a Spotify playlist URL.
2. The system analyzes the tracks in the playlist, taking various musical attributes into account.
3. It recommends five new songs that match the user's preferences.

## Technologies Used
- **Streamlit**: For building the web interface.
- **Spotipy**: For interacting with the Spotify API to fetch playlist details.
- **Pandas**: For data manipulation and analysis.
- **Python**: As the core programming language.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/heysuhas/spotify.git
    ```
2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Set up your Spotify API credentials by adding `client_id` and `client_secret` as environment variables or in a `.env` file.

4. Run the app:
    ```bash
    streamlit run app.py
    ```

## Spotify API Credentials
To get the recommendations, you need to set up the Spotify API credentials:

1. Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications) and create an application.
2. Get your `client_id` and `client_secret`.
3. Add these to your environment variables or a `.env` file:

    ```bash
    SPOTIPY_CLIENT_ID=your_client_id
    SPOTIPY_CLIENT_SECRET=your_client_secret
    ```

## License
This project is licensed under the MIT License.

## Contact
Feel free to reach out if you have any questions or feedback!

- GitHub: [heysuhas](https://github.com/heysuhas)

---
**Made with ❤️ by Suhas**
