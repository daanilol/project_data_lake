import requests
import boto3


try:
    response_pokemon = requests.get("https://pokeapi.co/api/v2/pokemon/?limit=-1")
    response_chain_evolution = requests.get("https://pokeapi.co/api/v2/evolution-chain/?limit=-1")

    pokemon_json = response_pokemon.json()
    chain_evolution_json = response_chain_evolution.json()
    print("REQUISIÇAO OK")

except:
    print("ERRO AO REQUISITAR")