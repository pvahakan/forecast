#!/usr/bin/env python3

import urllib.request
import json

def read_user_agent(path_to_file):
    f = open(path_to_file, 'r')
    str_agent = f.read()
    f.close()
    return str_agent


def read_weather_data():
    """
    Tällä tavalla saadaan yr.no -sivustolta säätiedotuksia jsonina pihalle.
    """
    # Greenwich
    # request_url = 'https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=51.5&lon=0'
    # Oulu
    request_url = 'https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=65.0&lon=25.5'
    # User agent pitää olla, jotta YR antaa dataa, oli joku nettisivu, joka näytti tämän
    user_agent = read_user_agent('./user_agent.txt')
    headers = {'User-Agent': user_agent,}
    # Data saadaan ulos näin
    response = urllib.request.Request(request_url, None, headers)
    req = urllib.request.urlopen(response)
    string_data = req.read()
    json_data = json.loads(string_data)
    return json_data

def find_location():
    """
    Returns a location data for forecast as a list. Location has form 'longitude, latitude, elevation'.
    """
    json_data = read_weather_data()
    location = json_data['geometry']['coordinates']
    return location

def parse_timeseries():
    """
    Parses json weather data to dictionary in form {date: [(time_0, air_temperature), (time_1, air_temperature), ... ] }
    """
    # json_data = read_weather_data()

    # Vähennetään netin yli tapahtuvaa tiedonsiirtoa ja luetaan data tiedostosta
    f = open('./data.json', 'r')
    json_data = json.loads(f.read())
    f.close()

    timeseries = json_data['properties']['timeseries']

    weather_data = {} # a dictionary to store data as a {date: [time]}

    for t in timeseries:
        air_temperature = t['data']['instant']['details']['air_temperature']
        date, time = t['time'].strip('Z').split('T')
        if date not in weather_data.keys():
            weather_data[date] = [(time, air_temperature)]
        else:
            weather_data[date].append((time, air_temperature))

    return weather_data

if __name__ == '__main__':
    # find_location()
    # read_weather_data()
    print(parse_timeseries())
