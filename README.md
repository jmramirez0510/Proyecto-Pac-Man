# Documentación del Código de Pac-Man en Pygame

## Introducción
Este trabajo fue realizado por **Juan Miguel Ramírez** y **Roberth Mauricio López**, estudiantes del programa de **Ingeniería en Sistemas** de **séptimo semestre** de la **Universidad Santiago de Cali**. 

Este documento describe el funcionamiento del código de Pac-Man implementado en Pygame. Se explican los módulos utilizados, las funciones clave y el comportamiento general del juego.

## Dependencias
El código usa las siguientes bibliotecas:
- `pygame`: Para manejar los gráficos y eventos del juego.
- `random`: Para la aleatoriedad en los movimientos de los fantasmas.
- `time`: Para manejar tiempos de espera.
- `sys`: Para gestionar la salida del programa.

## Configuración del Juego
- **Dimensiones:** El juego se ejecuta en una ventana de `1000x600` píxeles, mientras que la pantalla de inicio es de `800x600` píxeles.
- **Colores:** Se definen varios colores en formato RGB.
- **Velocidades:**
  - `GHOST_SPEED = 10`
  - `PACMAN_SPEED = 1.5`

## Carga de Imágenes
Se cargan imágenes para Pac-Man y los fantasmas (`ghost_red`, `ghost_blue`, `ghost_yellow`, `ghost_vulnerable`), ajustándolas al tamaño de los tiles (`TILE_SIZE`).

## Laberinto
El laberinto está representado como una lista de cadenas donde:
- `1` representa un muro.
- `0` representa un punto comestible.
- `P` indica la posición inicial de Pac-Man.

## Funciones Principales
### `show_intro_screen()`
Muestra la pantalla de inicio y espera que el jugador presione `1` para comenzar.

### `find_pacman_start()`
Busca y devuelve la posición inicial de Pac-Man en el laberinto.

### `check_collision()`
Verifica si Pac-Man choca con un fantasma. Si está en modo poder, el fantasma es eliminado temporalmente y colocado en la zona de espera por 5 segundos.

### `move_ghosts()`
Mueve los fantasmas de manera aleatoria en el laberinto. Si están en la zona de espera, se mueven de lado a lado hasta que termine el tiempo de espera.

## Comportamiento de los Fantasmas
Los fantasmas tienen los siguientes atributos:
- `released`: Indica si ya han salido de la base inicial.
- `vulnerable`: Indica si pueden ser comidos por Pac-Man.
- `respawn_time`: Controla el tiempo de espera antes de volver a moverse libremente.

## Manejo de Eventos
El juego responde a eventos de teclado para mover a Pac-Man en cuatro direcciones (`K_LEFT`, `K_RIGHT`, `K_UP`, `K_DOWN`).

## Conclusión
Este código implementa un clon de Pac-Man con funcionalidades clave como el movimiento de fantasmas, detección de colisiones y una pantalla de inicio. Se puede mejorar agregando más niveles y aumentando la inteligencia de los fantasmas.

## Licencia
```
MIT License

Copyright (c) 2025 Juan Miguel Ramírez y Roberth Mauricio López

Se concede permiso, de forma gratuita, a cualquier persona que obtenga una copia de este software y los archivos de documentación asociados (el "Software"), para utilizar el Software sin restricción, incluyendo sin limitación los derechos a usar, copiar, modificar, fusionar, publicar, distribuir, sublicenciar y/o vender copias del Software, y a permitir a las personas a las que se les proporcione el Software a hacer lo mismo, sujeto a las siguientes condiciones:

El aviso de copyright anterior y este aviso de permiso se incluirán en todas las copias o partes sustanciales del Software.

EL SOFTWARE SE PROPORCIONA "TAL CUAL", SIN GARANTÍA DE NINGÚN TIPO, EXPRESA O IMPLÍCITA, INCLUYENDO PERO NO LIMITADO A GARANTÍAS DE COMERCIALIZACIÓN, IDONEIDAD PARA UN PROPÓSITO PARTICULAR Y NO INFRACCIÓN. EN NINGÚN CASO LOS AUTORES O TITULARES DEL COPYRIGHT SERÁN RESPONSABLES POR NINGUNA RECLAMACIÓN, DAÑO U OTRA RESPONSABILIDAD, YA SEA EN UNA ACCIÓN DE CONTRATO, AGRAVIO O CUALQUIER OTRO MOTIVO, DERIVADO DE O EN CONEXIÓN CON EL SOFTWARE O EL USO U OTROS TRATOS EN EL SOFTWARE.
```

