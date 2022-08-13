from pprint import pprint
import requests
import json


class SuperHeroes:

    def _get_all_heroes(self):
        url = 'https://akabab.github.io/superhero-api/api/all.json'
        response = requests.get(url)
        result = response.json()
        return result

    def _get_heroes_list(self):
        heroes_list = []
        for character in self._get_all_heroes():
            if (character['name'] == 'Hulk') or \
                    (character['name'] == 'Captain America') or (character['name'] == 'Thanos'):
                heroes_list.append(character)
        return heroes_list

    def get_most_intelligent(self):
        max_ = 0
        character_name = None
        for item in self._get_heroes_list():
            if item['powerstats']['intelligence'] > max_:
                max_ = item['powerstats']['intelligence']
                character_name = item['name']
        return f'The most intelligent superhero is {character_name}'


if __name__ == '__main__':
    s = SuperHeroes()
    print(s.get_most_intelligent())
