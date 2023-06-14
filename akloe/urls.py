"""akloe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from akloe.api.views import PokemonListView, PokemonLocationsView, PokemonTypeView, PokemonByHMView, PokemonSpriteView, PokemonTypes, PokemonLocations, PokemonListViewAll, MachineListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pokemon/', PokemonListView.as_view(), name='pokemon-list'),
    path('location/<str:pokemon_name>/', PokemonLocationsView.as_view(), name='location-list'),
    path('type/<str:type_name>/', PokemonTypeView.as_view(), name='type-list'),
    path('hm/<str:hm_number>/', PokemonByHMView.as_view(), name='hm-list'),
    path('sprite/<str:pokemon_name>/', PokemonSpriteView.as_view(), name='sprite-list'),
    path('types/', PokemonTypes.as_view(), name='types-list'),
    path('locations/', PokemonLocations.as_view(), name='types-list'),
    path('names/', PokemonListViewAll.as_view(), name='types-list'),
    path('machines/', MachineListView.as_view(), name='types-list'),
    
    
]
