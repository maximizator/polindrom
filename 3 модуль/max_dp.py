# import requests
#
#
# def find_max_diameter_planet():
#     planets_url = 'https://swapi.dev/api/planets/'
#     max_diameter = 0
#     max_diameter_planet = ''
#     while planets_url:
#         response = requests.get(planets_url)
#         data = response.json()
#         for planet in data['results']:
#             if planet['diameter'] != 'unknown' and int(planet['diameter']) > max_diameter:
#                 max_diameter = int(planet['diameter'])
#                 max_diameter_planet = planet['name']
#         planets_url = data['next']
#     return max_diameter_planet


import requests


def get_starship_with_highest_atmospheric_speed():
    starship_url = "https://swapi.dev/api/starships/"
    max_speed = -1
    highest_atmospheric_speed_starship = ''
    while starship_url:
        response = requests.get(starship_url)
        data = response.json()
        for starship in data['results']:
            if starship['max_atmosphering_speed'].isdigit() and int(starship['max_atmosphering_speed']) > max_speed:
                max_speed = int(starship['max_atmosphering_speed'])
                highest_atmospheric_speed_starship = starship['name']
        starship_url = data['next']
    return highest_atmospheric_speed_starship