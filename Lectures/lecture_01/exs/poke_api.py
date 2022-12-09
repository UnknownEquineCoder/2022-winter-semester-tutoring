import requests
import random
from pprint import pprint

random.seed(69420)

"""
You are tasked with creating the following script:

- Take N random pokemons from the database
- Verify which have the higher special attack score
- Print the winner's name and associated attack score
"""

with open("all_pokemons.txt", "r") as pokemons:
    all_pokemon = pokemons.read().splitlines()
    picked_pokemons = random.choices(all_pokemon, k=6)

    """
    Whenever you see, 
    ``__enter__`` and ``__exit__`` methods,
    you can use the ``with`` statement.
    """
    special_atks = {}

    for pokemon in picked_pokemons:
        with requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}") as req:
            json = req.json()
            # key: json["name"]
            # value: json["stats"][3]["base_stat"]
            # dict[key] = value
            special_atks[json["name"]] = json["stats"][3]["base_stat"]

            # delete a key
            # dict[key] = None

    strongest = None
    hi_atk = 0

    for pokemon, value in special_atks.items():
        if (strongest == None) or value > hi_atk:
            strongest = pokemon
            hi_atk = value

    print(
        f"{strongest} is the pokemon with the highest special attack: it has {hi_atk} of power!"
    )
