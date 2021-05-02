import requests
import pandas as pd

def get_pokemons(url='https://pokeapi.co/api/v2/pokemon-form/?limit=1118'):
#get pokemons from api and return a dictionary
	i_id=1
	pokeDict = dict()
	response = requests.get(url)
	if response.status_code == 200:

		payload = response.json()
		#try to get results, if not possible then get empty list
		results = payload.get('results', [])

		if results:
			#if list not empty, iterate it
			for pokemon in results:
				name = pokemon ['name']
				pokeDict[i_id] = name
				i_id+=1

		return pokeDict


def poke_df (poke_dict):
	#
    df_pokeDex = pd.DataFrame(index = poke_dict.keys() , data = poke_dict.values(), columns = ['Pokemon'])
    return df_pokeDex

if __name__ == '__main__':
    url = 'https://pokeapi.co/api/v2/pokemon-form'
    df_pokeDex = poke_df(get_pokemons())
    df_pokeDex.to_csv('pokemons_list.csv')