import requests
from os import getenv
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import random

def get_song_data(title, artist):
  base_url = 'https://api.genius.com'
  token = getenv("GENIUS_TOKEN")
  headers = { 'Authorization': 'Bearer ' + token }
  data = { 'q': title + ' ' + artist }
  data = requests.get(base_url + '/search', data=data, headers=headers).json()
  for song in data["response"]["hits"]:
    if artist.lower() in song['result']['primary_artist']['name'].lower():
      return song
      
def get_genius_lyrics(url):
  page = requests.get(url)
  html = BeautifulSoup(page.text, 'html.parser')
  lyrics = html.find('div', class_='lyrics').get_text()
  return lyrics
  
def get_song_lyrics(title, artist):
  try:
    song = get_song_data(title, artist)
  except Exception as error:
    print('Error getting song data for {}, {}: {}'.format(title, artist, error))
    return
  if song:
    lyrics = get_genius_lyrics(song['result']['url'])
    return lyrics


def generate_random_string(length):
  text = ""
  possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
  for i in range(0, length):
    random_index = random.randint(0, len(possible) - 1)
    text += possible[random_index]
  return text