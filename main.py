import requests
#for shuffling possible answers later
import random
import Amiibo
import Pokemon


def main():
    name = input('what is the name of your Pokemon? ')

    amiiboAPI = Amiibo.Amiibo(name)
    results = amiiboAPI.get()

    pokeAPI = Pokemon.Pokemon(name)
    results = pokeAPI.get(name)

    win = random.randrange(0, 100)

    print(
        f'Based on these stats, {name} has a {win}% chance of winning a fight')


main()
