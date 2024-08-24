import requests


def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']

    for cosmo in planets:
        if cosmo['isPlanet']:
            name = cosmo.get('englishName', 'Unknown')  
            mass = cosmo.get('mass', {}).get('massValue', 'Unknown') 
            orbit_period = cosmo.get('sideralOrbit', 'Unknown')  
            print(f"The Planet in the name of: {name}, has a Mass of {mass}, with an Orbit of  {orbit_period} days")

fetch_planet_data()

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']

  
    formatted_planets = []
    for cosmo in planets:
        if cosmo['isPlanet']:
            name = cosmo.get('englishName', 'Unknown')  
            mass = cosmo.get('mass', {}).get('massValue', 'Unknown') 
            orbit_period = cosmo.get('sideralOrbit', 'Unknown')
            formatted_planets.append({'name': name, 'mass': mass, 'orbit_period': orbit_period})

    return formatted_planets

def find_heaviest_planet(planets):
    heaviest_planet = max(planets, key=lambda p: p['mass'])
    return heaviest_planet['name'], heaviest_planet['mass']


planets = fetch_planet_data()
planet_name, mass = find_heaviest_planet(planets)


print(f"{planet_name} is consider the heaviest planet. With a mass of {mass} kg.")

