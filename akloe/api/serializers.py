from rest_framework import serializers




class PokemonSerializer(serializers.Serializer):
    name = serializers.CharField()
    
class PokemonLocationSerializer(serializers.Serializer):
    location_area = serializers.URLField()