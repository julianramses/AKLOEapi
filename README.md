#AKLOEapi 
AKLOEapi es la api hecha con Django-Rest-Framework, basada en las funcionalidades exigidas en el proyecto.
Prerequisitos: 
```sh
Django, Python, pyenv, pip.
```
La instalación de DRF se realiza en el siguiente link:

```sh
https://www.django-rest-framework.org/tutorial/quickstart/
```

Suponiendo que Django-Rest-Framework está instalado, se debe clonar el proyecto:
```sh
git clone https://github.com/julianramses/AKLOEapi.git
```
Luego de clonar, se entra al directorio del proyecto.

```sh
cd AKLOEapi
```

Luego de esto, se tiene que crear un entorno virtual, de la siguiente manera:

```sh
python3 -m venv venv
```

Luego se activa de la siguiente forma:
```sh
source venv/bin/activate
```
Luego, se instalan los requerimientos.
```sh
pip install -r requirements.txt
```
Se realizan migraciones 

```sh
python manage.py migrate
```
Y por último se corre el servidor.
```sh
python manage.py runserver
```

La API consta de variados endpoints, un ejemplo de endpoint sería éste, que se encuentra en views.py.

```sh
class PokemonSpriteView(APIView):
    def get(self, request, pokemon_name):
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}/"
        response = requests.get(url)
        data = response.json()
        sprite_url = data['sprites']['other']['official-artwork']['front_default']
        
        return Response({'sprite_url': sprite_url})     
```

Lo que se puede apreciar en este endpoint es que desde la dirección que está dentro de url, podemos hacer un fetch de los atributos que sean necesarios, en este caso
```sh
{
    "sprite_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png"
}
```
Podemos encontrar el atributo de sprite, lo que es una foto que ya viene dentro de la API de pokemon.
Pero dentro de la lógica

```sh
        sprite_url = data['sprites']['other']['official-artwork']['front_default']
        
        return Response({'sprite_url': sprite_url})     
```
Tuvimos que entrar primero en sprites->other->official-artwork->front_default para extraer el atributo del pokemon, el json crudo de la api es:

```sh
"sprites": {
		"back_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/25.png",
		"back_female": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/female/25.png",
		"back_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/shiny/25.png",
		"back_shiny_female": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/shiny/female/25.png",
		"front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png",
		"front_female": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/female/25.png",
		"front_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/25.png",
		"front_shiny_female": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/female/25.png",
		"other": {
			"dream_world": {
				"front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/dream-world/25.svg",
				"front_female": null
			},
			"home": {
				"front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/home/25.png",
				"front_female": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/home/female/25.png",
				"front_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/home/shiny/25.png",
				"front_shiny_female": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/home/shiny/female/25.png"
			},
			"official-artwork": {
				"front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png
   ```
   
Este es un ejemplo del endpoint realizado, se puede ver la respuesta del request en un programa para validar request, ya sea postman, insomnia u otro:

```sh
https://akloeapi.fly.dev/sprite/pikachu/
```
El json que arroja el endpoint es:
```sh
GET /sprite/pikachu/
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "sprite_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png"
}
```
De esta manera, vemos un ejemplo de un endpoint, en este caso, se extrae el atributo que otorga las imágenes, para luego consumirlas en el front.

Todos los endpoints de la APi están acá:
```sh
1)https://akloeapi.fly.dev/pokemon/
2)https://akloeapi.fly.dev/location/<str:pokemon_name>/
3)https://akloeapi.fly.dev/type/<str:type_name>/
4)https://akloeapi.fly.dev/hm/<str:hm_number>/
5)https://akloeapi.fly.dev/sprite/<str:pokemon_name>/
6)https://akloeapi.fly.dev/types/
7)https://akloeapi.fly.dev/locations/
8)https://akloeapi.fly.dev/names/
9)https://akloeapi.fly.dev/machines/
```
- En 1 se muestran todos los pokemones filtrados por la letra C
- En 2 se muestran todos las locaciones donde encontrar los pokemones, en '<str:pokemon_name' se ingresa el nombre de un pokemon.
- En 3 se muestran todos los pokemones por tipo, los tipos están identados por número o nombre del tipo, este endpoint se utilizó para llamar los nombres y hacer el filtro en el front.
- En 4 se muestran todos los pokemones por hidden machine, las hidden machines están por su id o nombre.
- EN 5 se muestra la imagen del pokemon, en '<str:pokemon_name' se ingresa el nombre de un pokemon.
- En 6 se muestran todos los tipos de pokemon que existen, se utilizó para nombrar los tipos de pokemon en el front.
- En 7 se muestran todas las locaciones, se utilizó para nombrar en el front.
- En 8 se muestran todos los nombres de los pokemones.
- En 9 se muestran 20 máquinas, este endpoint no se utilizó ya que las máquinas solo cambiaban cuando el movimiento de la maquina cambiaba por lo tanto habian muchas repetidas.










