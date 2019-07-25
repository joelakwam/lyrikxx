import requests
from constants import *
import json

while True:
    print()
    print("Welcome to LYRIKXX")
    print('Created by Joel Akwam')
    print()
    print('Choose one of the options:')
    print('1- Search for lyrics of a song')
    print('2- Quit')
    print()

    choice = input(">>> ")

    if choice == '2':
        break

    if choice == '1':
        print("Artist's name?")
        artist_name = input(">>> ")
        print("Name of the track?")
        track_name = input(">>> ")
        print()
        print()
        api_call = base_url + matcher_lyrics_get + api_key + q_artist + artist_name + q_track + track_name

        #Send request to the API
        api_request = requests.get(api_call)
        json_data = api_request.json()

        print()

        print(json_data['message']['body']['lyrics']['lyrics_body'])

    print()
    print()
    print()
    print("Search for lyrics for another song? yes/no")
    choice_2 = input(">>> ")

    if choice_2 == 'no':
        break
