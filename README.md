# **BadgeBattles**

## **Integrantes**

David Moure Cerqueira y Lucía Lagares Álvarez

## **Descripción y objetivo**

Aplicación de servidor que consiste en peleas entre pokemon, en la que para honrar el nombre del proyecto, con cada victoria se obtendrá una medalla hasta lograr el máximo de 8 medallas.

## **Instrucciones**

Será necesario para descargar este proyecto tener Python 3.13.7 y Flask 3.1.2

Crear entorno virtual usando python -m venv .venv

Instalar las dependencias con ./venv/Scripts/pip.exe install -r ./requirements.txt

Para la creación de la base de datos ejecutar: ./.venv/Scripts/flask --app app.main create-tables.

Para la población de entrenadores en la base de datos, ejecutar: ./.venv/Scripts/flask --app app.main add-opponents.
Este comando no se puede ejecutar más de una vez después de crear tablas.

En caso de querer registrar o utilizar un entrenador predefinido en la base de datos, en la pagina de login será necesario escribir su nombre, e introducir la contraseña:0000

Ejecutar el documento utilizando ./venv/Scripts/python -m app.main

Registrate con tu nombre y género, haz click sobre la carta del Pokemon que te interesa para poder ver sus estadísticas, una vez decidas tu favorito, escribe su nombre en el buscador de la lista y disfruta de las batallas!

## **Vistas**

**Vista welcome:**

![alt text](imagenes/welcome.png)

**Vista registro:**
![alt text](imagenes/register-page.png)

**Vista pokemon-list:**

![alt text](imagenes/pokemon-list.png)

**Vista pokemon-details:**

![alt text](imagenes/pokemon-details.png)

**Vista pokemon-battle:**

![alt text](imagenes/pokemon-battle.png)

**Vista winner-page:**

![alt text](imagenes/winner-page.png)

**Vista trainer-details:**
![alt text](imagenes/trainer-details.png)

**Vista battle-details:**
![alt text](imagenes/battle-detail.png)

## **Distribución**

Al mismo nivel de app esta almacenada la 'data' ya que en este momento utilizamos un JSON como base de datos, este está compuesto de un array de diccionarios en el que cada uno es un Pokemon diferente, del cual solo leemos información.

Dentro de app:

- **Templates** contiene cada una de las vistas de la aplicación, se compone por un HTML base que contiene el header y footer, y cada una de las plantillas que hereda de esta completándola con su propio contenido.

- **Static** contiene elementos estáticos como son en este caso, CSS, imágenes y fuentes (en nuestro caso hemos utilizado Tailwind y DaisyUI para el estilo del HTML).

- **Services** contiene dos archivos los archivos y .
  - **pokemon_service.py** que contiene la lógica de obtención del listado de Pokemons, de un Pokemon o del valor de una stat:
    - **get_pokemons()**
    - **get_pokemon_by_id(id)**
    - **is_pokemon_shiny(id,max):**

      Partiendo del ID hace raices cuadradas para reducirlo hasta lograr que sea menor que el max enviado (ayuda a controlar la probabilidad), y lo compara con un número aleatorio entre 0 y el máximo.

    - **get_pokemon_by_name(name)**
    - **get_stat_value(pokemon, stat_name)**

  - **battle_service.py** que contiene la lógica de batalla, obtener cuál será el Pokemon enemigo, cuales serán los movimientos de cada Pokemon, creación de batalla y el combate:
    - **enemyPokemonSelector(my_pokemon)**
    - **random_moves(pokemon, moves)**
    - **create_battle(my_pokemon, enemy_pokemon, my_pokemon_moves):** Crea el objeto batalla.
    - **attack(battle, option):**

      Se compara que Pokemon ataca primero y en función de la salida, ataca el rival o nosotros. Se evalua si el ataque impacta (booleano), se calcula el daño, se resta, se evalua si el Pokemon está vivo, en caso afirmativo le toca al rival, en caso contrario, se termina el combate.

    - **calculatePrecision(move):** Booleano.
    - **enemyAttack(moves):** Calcula que ataque usará el enemigo.
    - **write_log(battle, attacker, move, damage, reciever)**
    - **miss_log(battle)**
    - **winner_log(battle, ganador, perdedor)**
    - **calculate_HP_to_substract(attacker, reciever, move)**
    - **substract_HP(pokemon, damage)**
    - **evaluate_pokemon(hp)**
    - **rivalSpriteSelector()**

- **Routes:** Está compuesta por 3 archivos que contienen todas las rutas de la aplicación, cada una de ellas tiene un Blueprint asociado al main para poder repartir las rutas en diferentes directorios:
  - - **home_routes.py:**
    * '/' que contiene la función **welcome()**, la cual es la página de bienvenida de la aplicación.
      - **GET:** Muestra el formulario donde el usuario debe registrarse indicando su nombre de entrenador y género.
      - **POST:** Valida que el nombre del entrenador tenga entre 3 y 15 caracteres.
        - Si es válido, guarda el nombre y el género en sesión y redirige a la lista de Pokémon (`pokemon.pokemon_list`).
        - Si no, muestra un mensaje de error en la plantilla `index.html`.

      - '/file' que contiene la función **file_json()** para mostrar los datos del JSON en crudo.

  - **pokemon_routes.py:** - '/' que contiene la función **pokemon_list()**, la cual muestra la lista de Pokémon disponibles. Permite seleccionar un Pokémon mediante un formulario.  
     - Si el Pokémon existe, se guarda en sesión junto con un Pokémon enemigo, un rival y los movimientos aleatorios del Pokémon, redirigiendo al combate (`battle.pokemon_battle`).  
     - Si no existe, muestra un mensaje de error indicando que el Pokémon no está en la lista.

  - **pokemon_routes.py:**
    - Esta ruta contiene un verificador de login.
    - '/<int:pokemon_ID>/' que contiene la función **pokemon_details()**, la cual muestra los detalles de un Pokémon específico seleccionado por su ID y determina aleatoriamente si es shiny.
    - Renderiza la plantilla `pokemon_details.html` mostrando la información del Pokémon y si es shiny.

  - **battle_routes.py:**
    - Esta ruta contiene un verificador de login.
    - '/' que contiene la función **pokemon_battle()**, la cual gestiona la lógica de redireccionamiento del combate.
    - Utiliza la función create_battle de battle_service para guardar en sesión el objeto de batalla.
    - **GET:** Recupera los datos del Pokémon del jugador, sus movimientos y el enemigo desde la sesión. Si todos los datos están disponibles, crea la batalla y renderiza `pokemon_battle.html`. Si no, redirige a la lista de Pokémon.
    - **POST:** Procesa la acción seleccionada por el jugador mediante un formulario. Evalúa el resultado del ataque usando el servicio de batalla.
      - Si hay un ganador o perdedor, se muestran los resultados en `pokemon_winner.html` incluyendo turnos y registro de la batalla.
      - Al finalizar, elimina los datos de batalla y Pokémon de la sesión.

- **Repositories:** Obtiene la información del JSON.
  - **pokemon_repo.py:** Obtiene los datos de los Pokemons del JSON
    - **get_pokemons()**
    - **search_by_id(id)**

- **Models:** Contienen la clase de los objetos de pokemon y battle.

- **Base de datos:** El funcionamiento básico de la base de datos consiste en que el atacante siempre es el usuario en uso, el resultado es un booleano que devuelve true o false en base a este usuario, por lo que si el resultado es 1 es una victoria y si es 0 es una derrota. Si se utiliza un usuario que ha sido defensor, al ver los resultados se comprueba si su resultado ha sido true o false y que devuelva el resultado inverso.
  Usuario -> Atacante:
  resultado: true -> winner;
  resultado: false -> loser
  Usuario -> Defensor:
  resultado: true -> loser
  resultado: false -> winner

Hay una serie de archivos situados a primer nivel de app:

- **colors:** es un diccionario que asocia los tipos de los pokemons y sus ataques a nombres de colores
- **decorators** contiene el decorador de verificación de login.
- **rivas** contiene un diccionario con los nombres de los rivales y su imagen.

- **main** es donde se registran los blue prints, se configura las session y la contraseña, se inicia la extensión de sesiones.
