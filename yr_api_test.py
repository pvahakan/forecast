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

def test_print():
    json_data = read_weather_data()
    for i in json_data:
        print(i)

if __name__ == '__main__':
    # test_print()
    read_weather_data()
