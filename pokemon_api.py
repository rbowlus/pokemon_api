#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Take a look at PokeAPI: https://pokeapi.co/.
# On this website you will see an API simulator. Trying any combination of correct possible server requests should yield you a successful result in the scrollable area.
# In this scrollable area is an exact server response you will get if you sent a response to it.
# Click on the Documentation tab, then click on v2. On the next page you'll see a bunch of words that seemingly make no sense. Just like with any API, there is documentation
# showing you how to use it. API documentation, by nature, is very wordy, overwhelming and almost never straightforward. You will find very few APIs that have simple documentation.
# Once you start to become a mid-senior level engineer, the little details in documentation will make all the difference in the quality of your results. Most people find API
# documentation difficult to navigate at first. Don't worry, it's normal.
# That being said, familiarize yourself with everything in the documentation and try to skim as much as possible to get a feel for where everything is before proceeding.
import requests
from IPython.display import clear_output as co
class Pokemon:
    def __init__(self, _name, poke):
        self.info = {
            'name': _name,
            'type': poke['types'][0]['type']['name'],
            'height': poke['height'],
            'weight': poke['weight'],
            'stats': {
                'hp': poke['stats'][0]['base_stat'],
                'attack': poke['stats'][1]['base_stat'],
                'defense': poke['stats'][2]['base_stat'],
                'speed': poke['stats'][3]['base_stat'],
                'special attack': poke['stats'][4]['base_stat'],
                'special defense': poke['stats'][5]['base_stat']
            },
            'abilities': [i['ability']['name'] for i in poke['abilities']]
        }
    def get_info(self):
        return self.info
    def __repr__(self):
        return self.info['name']
class PokemonList:
    def __init__(self, *args):
        self.pokedex = {}
        for arg in args:
            self.add(arg)
# ADD FUNCTION
    def add(self, _name):
        #requests.get("https://pokeapi.co/api/v2/pokemon/{_name}")
        new_poke = Pokemon(_name, requests.get(f"https://pokeapi.co/api/v2/pokemon/{_name}").json())
        if new_poke.info['type'] in self.pokedex.keys():
            self.pokedex[new_poke.info['type']].append(new_poke)
        else:
            self.pokedex[new_poke.info['type']]= []
            self.pokedex[new_poke.info['type']].append(new_poke)
    
    #Attempting to average the class statistics - Rachel & Carine
    def avg_type(self, a_type):
        curr_totals = {}
        num_ = 0
        for pokemon in self.pokedex[a_type]:
            for k,v in pokemon.get_info()["stats"].items():
                if k in curr_totals.keys():
                    curr_totals[k] += v
                else:
                    curr_totals[k] = v
            num_ += 1
        curr_averages = {}
        for k,v in curr_totals.items():
             curr_averages[k] = v / num_
        return curr_averages
        
    
    def __repr__(self):
        return 
    def print_pokemon(self):
        for k in self.pokedex.keys():
            print(k.title())

            print("-_-_" * 12)
            for p in self.pokedex[k]:
                averages = self.avg_type(p.info['type'])
                # print averages
                print(f'Average Health: {averages["hp"]}')
                print(f'Average Attack: {averages["attack"]}')
                print(f'Average Speed: {averages["speed"]}')
                print(f'Average Defense: {averages ["defense"]}')
                print("~~~~~"*12)
                print(f'Name: {p.info["name"].title()}')
                print(f'Type: {p.info["type"]}')
                print(f'Height: {p.info["height"]}')
                print(f'Weight: {p.info["weight"]}')
                print(f'Stats: {p.info["stats"]}')
                print(f'Abilities: {p.info["abilities"]}')
                print("~~~~~"*12)
                print("\n")
    def instructions(self): 
        print('Build  your pokedex!')
    def run(self):
        print("~~~~~"*12+"\nWelcome to Nohtyp, the Python-based Pokedex!\n"+"~~~~~"*12+"\n")
        quit = False
        while not quit:
            choice = input("""Enter 'add' to add a Pokemon. \n
Enter 'show' to see Pokedex. \n
Enter 'quit' to leave game.\n""").lower()
            co()
            if choice == 'add':
                add_pokemon = input('Enter your Pokemon: \n')
                self.add(add_pokemon)
                co()
            if choice == 'show':
                self.print_pokemon()
            if choice == 'quit':
                quit = True
                print('Goodbye!')

plist = PokemonList()
                
plist.run()


# In[ ]:




