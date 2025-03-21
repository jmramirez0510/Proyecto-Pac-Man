# Proyecto-Pac-Man
Introducción
Este documento describe el funcionamiento del código de Pac-Man implementado en Pygame. Se explican los módulos utilizados, las funciones clave y el comportamiento general del juego.
Dependencias
El código usa las siguientes bibliotecas:
•	pygame: Para manejar los gráficos y eventos del juego.
•	random: Para la aleatoriedad en los movimientos de los fantasmas.
•	time: Para manejar tiempos de espera.
•	sys: Para gestionar la salida del programa.
Configuración del Juego
•	Dimensiones: El juego se ejecuta en una ventana de 1000x600 píxeles, mientras que la pantalla de inicio es de 800x600 píxeles.
•	Colores: Se definen varios colores en formato RGB.
•	Velocidades:
o	GHOST_SPEED = 10
o	PACMAN_SPEED = 1.5
Carga de Imágenes
Se cargan imágenes para Pac-Man y los fantasmas (ghost_red, ghost_blue, ghost_yellow, ghost_vulnerable), ajustándolas al tamaño de los tiles (TILE_SIZE).
Laberinto
El laberinto está representado como una lista de cadenas donde:
•	1 representa un muro.
•	0 representa un punto comestible.
•	P indica la posición inicial de Pac-Man.
Funciones Principales
show_intro_screen()
Muestra la pantalla de inicio y espera que el jugador presione "1" para comenzar.
find_pacman_start()
Busca y devuelve la posición inicial de Pac-Man en el laberinto.
check_collision()
Verifica si Pac-Man choca con un fantasma. Si está en modo poder, el fantasma es eliminado temporalmente y colocado en la zona de espera por 5 segundos.
move_ghosts()
Mueve los fantasmas de manera aleatoria en el laberinto. Si están en la zona de espera, se mueven de lado a lado hasta que termine el tiempo de espera.
Comportamiento de los Fantasmas
Los fantasmas tienen los siguientes atributos:
•	released: Indica si ya han salido de la base inicial.
•	vulnerable: Indica si pueden ser comidos por Pac-Man.
•	respawn_time: Controla el tiempo de espera antes de volver a moverse libremente.
Manejo de Eventos
El juego responde a eventos de teclado para mover a Pac-Man en cuatro direcciones (K_LEFT, K_RIGHT, K_UP, K_DOWN).
Conclusión
Este código implementa un clon de Pac-Man con funcionalidades clave como el movimiento de fantasmas, detección de colisiones y una pantalla de inicio. Se puede mejorar agregando más niveles y aumentando la inteligencia de los fantasmas.
Ejecución del videojuego
 


