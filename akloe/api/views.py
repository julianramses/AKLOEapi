from django.shortcuts import render
import re
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PokemonSerializer, PokemonLocationSerializer
import requests



class PokemonListViewAll(APIView):
    def get(self,request):
        response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=2000')
        data = response.json()
        names = [names_data['name'] for names_data in data['results']]
        return Response(names)
        
        
class PokemonListView(APIView):
    def get(self, request):
        response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=2000')
        data = response.json()
        x = filter(lambda y: "c" in set(y['name']), data['results'])
        c = map(lambda p: asd(p), x)
        #y = re.search((r"/(\d+)/$",['url']).group(1) in set(['url']), data['results'])
        #z = filter(lambda b: "id"in set(b['url']['id']), data['results'])
        #id = filter(data['url'][id], data['results'])   
        return Response(c)
    #def get(self, request, x):
        #response = requests.get(f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/home/{}.png')
        #data = response.json()
        #return sprite_url
    #def get_pokemon_sprite(self, pokemon_url):
    #    data = response.json()
    #    sprite_url = data['sprites ']['other']['official-artwork']['front_default']
    #    return sprite_url
def asd(pokemon):
   name = pokemon['name'] 
   id = re.search(r"/(\d+)/$",pokemon['url']).group(1)
   image_url = f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/home/{id}.png'
   return {'name':name, 'id': id,'image_url': image_url}
   
    


class PokemonSpriteView(APIView):
    def get(self, request, pokemon_name):
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}/"
        response = requests.get(url)
        data = response.json()
        sprite_url = data['sprites']['other']['official-artwork']['front_default']
        
        return Response({'sprite_url': sprite_url})     
    
class PokemonLocationsView(APIView):
     def get(self, request, pokemon_name):
        url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}/encounters/'
        response = requests.get(url)
        data = response.json()
            
        location_areas = [encounter['location_area']['name'] for encounter in data ]
        return Response(location_areas)
    
class PokemonTypeView(APIView):
    def get(self, request, type_name):
        url = f'https://pokeapi.co/api/v2/type/{type_name}/'
        response = requests.get(url)
        data = response.json()

        pokemons = [pokemon_data['pokemon']['name'] for pokemon_data in data['pokemon']]
        return Response(pokemons)
    
class PokemonTypes(APIView):
      def get(self, request):
        url = 'https://pokeapi.co/api/v2/type/'
        response = requests.get(url)
        data = response.json()
        types = [type_data['name'] for type_data in data['results']]
        return Response(types)
    
class PokemonLocations(APIView):
    def get(self, request):
        url = 'https://pokeapi.co/api/v2/location/'
        response = requests.get(url)
        data = response.json()
        locations = [locations_data['name'] for locations_data in data['results']]
        return Response(locations)
                        
    
class PokemonByHMView(APIView):
    def get(self, request, hm_number):
        url = f'https://pokeapi.co/api/v2/move/{hm_number}/'
        response = requests.get(url)
        data = response.json()

        pokemons = []
        if 'learned_by_pokemon' in data:
            for pokemon_data in data['learned_by_pokemon']:
                pokemon_name = pokemon_data['name']
                pokemons.append(pokemon_name)

        return Response(pokemons)

class MachineListView(APIView):
    def get(self, request):
        url = 'https://pokeapi.co/api/v2/machine/'
        response = requests.get(url)
        data = response.json()

        machines = []
        for result in data['results']:
            machine_name = result['url'].split('/')[-2]
            machines.append(machine_name)
        return Response(machines)