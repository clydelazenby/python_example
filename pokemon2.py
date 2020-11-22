import requests
import json

print("Welcome To Clyde's PokeDex!")

pokemonName = input("Which Pokemon Do You Want To See? ")

data = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemonName}" )

if data.status_code == 200:
    data = json.loads(data.text)

    print(f"You Chose {data['name']}")

    action = input("What information would you like to see?  \n(i = info, s = stats) ")

    if action == "i" or action == "info":

        print(f"id: {data['id']}\n")
        print(f"name: {data['name']}\n")
        print(f"height: {data['height']}\n")
        print(f"weight: {data['weight']}\n")
        pokemon_type =""
        for type in data["types"]:
            if data["types"].index(type) == (len(data["types"]) -1):
        
                 pokemon_type += f"{type['type']['name']}"
        else:
            pokemon_type += f"{type['type']['name']}, "

        print(f"type: {pokemon_type}")

    elif action == "s" or action == "stats":
        print(f"Speed: {data['stats'][0]['base_stat']}")
        print(f"Special Defense: {data['stats'][0]['base_stat']}")
        print(f"Special Attack: {data['stats'][0]['base_stat']}")
        print(f"Defense: {data['stats'][0]['base_stat']}")
        print(f"Attack: {data['stats'][0]['base_stat']}")
        print(f"HP: {data['stats'][0]['base_stat']}")

    else: 

        print("Sorry We Dont Recongnize That Command")
else:
    print("Sorry That's Not A Valid Pokemon")

#i = info, s = stats,
# name,id, weight, height, types of pokemon