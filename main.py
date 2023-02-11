import os
import asyncio
import random

import discord
from dotenv import load_dotenv

import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
SPOTIFYID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIFYSECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
PLAYLISTID = os.getenv('SPOTIFY_PLAYLIST_ID')


# Default intents are now required to pass to Client
intents = discord.Intents.all()
client = discord.Client(intents=intents)


async def add_song_to_playlist(song_url, playlist_id):
    # Replace <client_id> and <client_secret> with your own Spotify API credentials
    auth = SpotifyOAuth(client_id=SPOTIFYID,
                         client_secret=SPOTIFYSECRET,
                         redirect_uri='http://localhost:8888/callback',
                         scope=['playlist-modify-public'])
    sp = spotipy.Spotify(auth_manager=auth)

    # Extract the song id from the song url
    song_id = song_url.split('track/')[1]
    song_id = song_id.split('?')[0]
    song_id = ("spotify:track:" + song_id)
    print(song_id)

    # Add the song to the playlist
    # await asyncio.sleep(0)
    sp.playlist_add_items(playlist_id=PLAYLISTID, items=[song_id], position=None)

    # Getting the song name for message formatting
    track_id = song_id.split(':')[2]
    track = sp.track(track_id)
    track_name = track['name']
    print(track_name)
    return track_name




@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('https://open.spotify.com/track/'):
        track_name = await add_song_to_playlist(message.content, PLAYLISTID)
        embed = discord.Embed(title=f"Adding '" + track_name + "' to my playlist.", color=0x00ff00)
        await message.channel.send(embed=embed)


client.run(TOKEN)