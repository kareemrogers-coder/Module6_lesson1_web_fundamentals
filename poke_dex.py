###Task 1:

import requests # importing requests 
import json
from helper import d

###Task 2: Fetching Data from the Pokémon API


#Write a Python script to make a GET request to the Pokémon API (https://pokeapi.co/api/v2/pokemon/pikachu).

response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu") # Fetch the the pokemon data.

poke_data = response.json()

#### Extracting and printing the name and abilities of the Pokémon.

print(f"The pokemon that is name {(poke_data["name"].title())}")
print("Has several abilites such as: ")
print(poke_data["abilities"][0]["ability"]["name"])
print(poke_data["abilities"][1]["ability"]["name"])
print(f"Coming in at a weight of: {(poke_data["weight"])} lbs")

d()
#### Task : Analyzing and Displaying Data

def fetch_pokemon_data():
    responsev2 = requests.get("https://pokeapi.co/api/v2/pokemon/bulbasaur")
    poke_data2 = responsev2.json()
    print(f"The pokemon that is name {(poke_data2["name"].title())}")
    print("Has several abilites such as: ")
    print(poke_data2["abilities"][0]["ability"]["name"])
    print(poke_data2["abilities"][1]["ability"]["name"])
    print(f"Coming in at a weight of: {(poke_data2["weight"])} lbs")
    d()
    responsev3 = requests.get("https://pokeapi.co/api/v2/pokemon/charmander")
    poke_data3 = responsev3.json()
    print(f"The pokemon that is name {(poke_data3["name"].title())}")
    print("Has several abilites such as: ")
    print(poke_data3["abilities"][0]["ability"]["name"])
    print(poke_data3["abilities"][1]["ability"]["name"])
    print(f"Coming in at a weight of: {(poke_data3["weight"])} lbs")
    d()
    responsev4 = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
    poke_data4 = responsev3.json()
    print(f"The pokemon that is name {(poke_data4["name"].title())}")
    print("Has several abilites such as: ")
    print(poke_data4["abilities"][0]["ability"]["name"])
    print(poke_data4["abilities"][1]["ability"]["name"])
    print(f"Coming in at a weight of: {(poke_data["weight"])} lbs")

fetch_pokemon_data()

d()

def calculate_average_weight():
    response4 = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu") # Fetch the the pokemon data.
    poke_data = response4.json()
    responsev2 = requests.get("https://pokeapi.co/api/v2/pokemon/bulbasaur")
    poke_data2 = responsev2.json()
    responsev3 = requests.get("https://pokeapi.co/api/v2/pokemon/charmander")
    poke_data3 = responsev3.json()

    pikachu = (poke_data["weight"])
    bulbasaur = (poke_data2["weight"])
    charmander = (poke_data3["weight"])

    average = (pikachu+bulbasaur+charmander)/3
    print(f"Tha average weight between Pikachu, Bulbasuar, Charmander is: {average}")

calculate_average_weight()