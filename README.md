[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)

# Billboard to Spotify Playlist

## 🛠️ Description
This Python program allows users to create a private Spotify playlist containing the songs that were on the Billboard Hot 100 chart on a specific date.
The program uses web scraping to retrieve the song names from the Billboard Hot 100 chart for a specified date, and then uses the Spotify API to search for each song and add it to a new private playlist

## ⚙️ Usage
To use this program, run the billboard_to_spotify.py file from your terminal, and follow the prompts to specify the date you want to create a playlist for.

The program will prompt you to log in to your Spotify account, and will then create a new private playlist with the name "<date> Billboard 100", where <date> is the date you specified. The program will then search for each song on Spotify, and add any matches to the new playlist.

Note that if a song cannot be found on Spotify, it will be skipped and a message will be printed to the console.

