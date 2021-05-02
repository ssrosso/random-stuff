import requests
import pandas as pd
#import numpy as np

def get_pokemons(url = 'https://pokeapi.co/api/v2/pokemon/'):
	name = []
	weight = []
	height = []
	base_hp = []
	pokeid = []
	for i in range (1,899):
		response = requests.get(url+str(i))
		if response.status_code == 200:
			payload = response.json()
			pokeid.append(payload ['id'])
			#or pokeid.append(i_id)
			name.append(payload ['name'])
			weight.append(payload ['weight'])
			height.append(payload ['height'])
			base_hp.append(payload ['stats'] [0] ['base_stat'])
			print(i)

	#looks awkward, but Pokemon IDs make a jump from 898 to 10001 (so does the url)
	for i in range (10001,10221):
		response = requests.get(url+str(i))
		if response.status_code == 200:
			payload = response.json()
			pokeid.append(payload ['id'])
			#or pokeid.append(i_id)
			name.append(payload ['name'])
			weight.append(payload ['weight'])
			height.append(payload ['height'])
			base_hp.append(payload ['stats'] [0] ['base_stat'])
			print(i)
	return pokeid, name, weight, height, base_hp

pokeid, name, weight, height, base_hp = get_pokemons()
poke_df = pd.DataFrame({
	'pokemon_name' : name,
	'weight' : weight,
	'height' : height,
	'base_hp' : base_hp
	}, index = pokeid)

poke_df.to_csv('pokemon_details.csv')

"""

def get_pokemons(url = 'https://pokeapi.co/api/v2/pokemon/'):
	poke_df = pd.DataFrame(columns = ['id','name', 'weight', 'height', 'base_hp'])
	poke_df.id = np.arange(1,1119)
	poke_df.set_index('id')
	for i in range (1118):
		response = requests.get(url+str(i+1))
		if response.status_code == 200:
			payload = response.json()

			poke_df.append(pd.Series({
			    'name': payload ['name'],
			    'weight': payload ['weight'],
			    'height': payload ['height'],
			    'base_hp':payload ['stats'] [0] ['base_stat'],
			    }, name=payload ['id']))

	return poke_df

poke_df = get_pokemons()
poke_df.to_csv('pokemon_details.csv')
#print (pokeid, name, weight, height, base_hp)

#print (pokename)
#print(payload)

"""