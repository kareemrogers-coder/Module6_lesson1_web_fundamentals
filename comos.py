import requests

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']

    #process each planet info
    for planet in planets:
        if planet['isPlanet']:
            name = planet.get('englishName', 'Unknown')
            mass = planet.get('mass', {}).get('massValue', 0) * planet.get('mass', {}).get('massExponent', 0)
            orbit_period = planet.get('sideralOrbit', 0)
            print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")

fetch_planet_data()

def find_heaviest_planet(planets):
    first_planet = planets[0]
    planet_with_greater_mass = {'name': first_planet['englishName'], 'mass': first_planet['mass']['massValue']}
    for planet in planets:
        if planet['mass'] and planet['mass']['massValue'] >= planet_with_greater_mass['mass']:
            planet_with_greater_mass = {'name': planet['englishName'], 'mass': planet['mass']['massValue']}


planets = fetch_planet_data()
name, mass = find_heaviest_planet(planets)
print(f"The heaviest planet is {name} with a mass of {mass} kg.")

