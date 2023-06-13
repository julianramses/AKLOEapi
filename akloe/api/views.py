from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PokemonSerializer, PokemonLocationSerializer
import requests




class PokemonListView(APIView):
    def get(self, request):
        response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=2000')
        data = response.json()
        
        filtered_pokemon = [
            pokemon for pokemon in data['results'] if 'c' in pokemon['name']
        ]
        
        serializer = PokemonSerializer(data=filtered_pokemon, many=True)
        serializer.is_valid()
        
        
        
        return Response(serializer.data)
    
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
