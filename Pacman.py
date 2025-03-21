import pygame
import random
import time
import sys

pygame.init()

# Configuración de constantes
TILE_SIZE = 40
GHOST_SPEED = 10
PACMAN_SPEED = 1.5
pacman_speed_counter = 0
score = 0
ghost_speed_counter = 0
pacman_moved = False
power_mode = False
power_mode_start = 0
lives = 3

# Definición de colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GOLD = (255, 215, 0)
RED = (255, 0, 0)

# Configuración de la pantalla
INTRO_WIDTH, INTRO_HEIGHT = 800, 600
GAME_WIDTH, GAME_HEIGHT = 1000, 600
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Pacman")
clock = pygame.time.Clock()

# Cargar imagen de introducción
screen = pygame.display.set_mode((800, 600))
intro_image = pygame.image.load("intro.png")
intro_image = pygame.transform.scale(intro_image, (800, 700))

def show_intro_screen():
    while True:
        screen.blit(intro_image, (0, 0))
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return  

# Llamar a la pantalla de inicio antes de iniciar el juego
show_intro_screen()
screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
# Cargar imágenes de personajes
pacman_img_right = pygame.image.load("pacman.png")
ghost_red = pygame.image.load("ghost_red.png")
ghost_blue = pygame.image.load("ghost_yellow.png")
ghost_yellow = pygame.image.load("ghost_blue.png")
ghost_vulnerable = pygame.image.load("ghost_vulnerable.png")
life_icon = pygame.transform.scale(pacman_img_right, (30, 30))

# Ajustar imágenes de Pac-Man
pacman_img_right = pygame.transform.scale(pacman_img_right, (TILE_SIZE, TILE_SIZE))
pacman_img_left = pygame.transform.flip(pacman_img_right, True, False)
pacman_img_up = pygame.transform.rotate(pacman_img_right, 90)
pacman_img_down = pygame.transform.rotate(pacman_img_right, -90)
pacman_img = pacman_img_right
# Ajustar imágenes de fantasmas
ghost_red = pygame.transform.scale(ghost_red, (TILE_SIZE, TILE_SIZE))
ghost_blue = pygame.transform.scale(ghost_blue, (TILE_SIZE, TILE_SIZE))
ghost_yellow = pygame.transform.scale(ghost_yellow, (TILE_SIZE, TILE_SIZE))
ghost_vulnerable = pygame.transform.scale(ghost_vulnerable, (TILE_SIZE, TILE_SIZE))

# Definición del laberinto
maze = [
    "1111111111111111111111111",
    "1000000000111110000000001",
    "1011111110111111111110101",
    "1010000000000000000000101",
    "1010110111110110110110101",
    "100011000P000000000110001",
    "1010110110110110110110101",
    "1000000000000000000000001",
    "1011111110111111111111101",
    "1010000000000000000000101",
    "1010110111110110110110101",
    "1000000000000000000000001",
    "1011111110111111111111101",
    "1010000000000000000000101",
    "1111111111111111111111111"
]

# Lista de puntos especiales
special_dots = []
for row in range(len(maze)):
    for col in range(len(maze[row])):
        if (row == 1 and col == 1) or (row == 1 and col == 23) or \
           (row == 13 and col == 1) or (row == 13 and col == 23):
            special_dots.append((col * TILE_SIZE, row * TILE_SIZE))

def find_pacman_start():
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == "P":
                return col * TILE_SIZE, row * TILE_SIZE
    return 0, 0

pacman_x, pacman_y = find_pacman_start()
pacman_dx, pacman_dy = 0, 0
initial_pacman_pos = (pacman_x, pacman_y)

# Lista de fantasmas con sus atributos iniciales
ghosts = [
    {"image": ghost_red, "x": 9 * TILE_SIZE, "y": 6 * TILE_SIZE, "dx": 0, "dy": 0, "released": False, "release_time": 1, "original_image": ghost_red, "vulnerable": False},
    {"image": ghost_blue, "x": 10 * TILE_SIZE, "y": 6 * TILE_SIZE, "dx": 0, "dy": 0, "released": False, "release_time": 8, "original_image": ghost_blue, "vulnerable": False},
    {"image": ghost_yellow, "x": 11 * TILE_SIZE, "y": 6 * TILE_SIZE, "dx": 0, "dy": 0, "released": False, "release_time": 12, "original_image": ghost_yellow, "vulnerable": False}
]

initial_ghost_positions = [(ghost["x"], ghost["y"]) for ghost in ghosts]

#Verifica si Pac-Man colisiona con un fantasma y maneja las consecuencias.
def move_ghosts():
    global pacman_moved, power_mode
    current_time = time.time()
    for ghost in ghosts:
        if pacman_moved and not ghost["released"] and current_time - start_time >= ghost["release_time"]:
            ghost["released"] = True
            ghost["dx"], ghost["dy"] = random.choice([(TILE_SIZE, 0), (-TILE_SIZE, 0), (0, TILE_SIZE), (0, -TILE_SIZE)])
        
        if ghost["released"]:
            if power_mode:
                ghost["dx"] *= 0.5
                ghost["dy"] *= 0.5
            
            possible_moves = []
            for dx, dy in [(-TILE_SIZE, 0), (TILE_SIZE, 0), (0, -TILE_SIZE), (0, TILE_SIZE)]:
                new_x, new_y = ghost["x"] + dx, ghost["y"] + dy
                row, col = int(new_y // TILE_SIZE), int(new_x // TILE_SIZE)
                if 0 <= row < len(maze) and 0 <= col < len(maze[0]) and maze[row][col] != "1":
                    possible_moves.append((dx, dy))
            
            if possible_moves:
                ghost["dx"], ghost["dy"] = random.choice(possible_moves)
            ghost["x"] += ghost["dx"]
            ghost["y"] += ghost["dy"]

#Accion a la hora de comer los puntos especiales
def handle_power_pellet():
    global power_mode, power_mode_start, special_dots
    for dot in special_dots[:]:
        if abs(pacman_x - dot[0]) < TILE_SIZE and abs(pacman_y - dot[1]) < TILE_SIZE:
            special_dots.remove(dot)
            power_mode = True
            power_mode_start = time.time()
            for ghost in ghosts:
                ghost["vulnerable"] = True
                ghost["image"] = ghost_vulnerable

#Funcion de modo power
def check_power_mode():
    global power_mode, power_mode_start
    if power_mode and time.time() - power_mode_start >= 10:
        power_mode = False
        for ghost in ghosts:
            ghost["vulnerable"] = False
            ghost["image"] = ghost["original_image"]
#Funcion para resetear la posicion de los fantasmas 
def reset_positions():
    global pacman_x, pacman_y, pacman_dx, pacman_dy
    pacman_x, pacman_y = initial_pacman_pos
    pacman_dx, pacman_dy = 0, 0
    
    for i, ghost in enumerate(ghosts):
        ghost["x"], ghost["y"] = initial_ghost_positions[i]
        ghost["dx"], ghost["dy"] = 0, 0
        ghost["released"] = False
        ghost["vulnerable"] = False
        ghost["image"] = ghost["original_image"]
#Funcion para manejas las colisiones o comer los fantasmas
def check_collision():
    global score, power_mode, lives
    for ghost in ghosts:
        if abs(pacman_x - ghost["x"]) < TILE_SIZE and abs(pacman_y - ghost["y"]) < TILE_SIZE:
            if power_mode and ghost["vulnerable"]:
                score += 200
                ghost["x"], ghost["y"] = initial_ghost_positions[ghosts.index(ghost)]
                ghost["released"] = False
                ghost["vulnerable"] = False
                ghost["image"] = ghost["original_image"]
            else:
                lives -= 1
                if lives > 0:
                    reset_positions()
                    return True
                else:
                    return "game_over"
    return False

start_time = time.time()
#Dibujar los puntos
def draw_maze():
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            x, y = col * TILE_SIZE, row * TILE_SIZE
            if maze[row][col] == "1":
                pygame.draw.rect(screen, BLUE, (x, y, TILE_SIZE, TILE_SIZE))
            elif maze[row][col] == "0":
                pygame.draw.circle(screen, WHITE, (x + TILE_SIZE // 2, y + TILE_SIZE // 2), TILE_SIZE // 6)
    
    for x, y in special_dots:
        pygame.draw.circle(screen, RED, (x + TILE_SIZE // 2, y + TILE_SIZE // 2), TILE_SIZE // 4)
#Dibujar las vidas
def draw_lives():
    for i in range(lives):
        screen.blit(life_icon, (900 + i * 30, 3))

def handle_events():
    global pacman_dx, pacman_dy, running, pacman_img, pacman_moved, start_time
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if not pacman_moved:
                pacman_moved = True
                start_time = time.time()
            if event.key == pygame.K_LEFT:
                pacman_dx, pacman_dy = -TILE_SIZE, 0
                pacman_img = pacman_img_left
            elif event.key == pygame.K_RIGHT:
                pacman_dx, pacman_dy = TILE_SIZE, 0
                pacman_img = pacman_img_right
            elif event.key == pygame.K_UP:
                pacman_dx, pacman_dy = 0, -TILE_SIZE
                pacman_img = pacman_img_up
            elif event.key == pygame.K_DOWN:
                pacman_dx, pacman_dy = 0, TILE_SIZE
                pacman_img = pacman_img_down

running = True
game_over = False
while running:
    screen.fill(BLACK)
    draw_maze()
    
    if not game_over:
        screen.blit(pacman_img, (pacman_x, pacman_y))
        
        ghost_speed_counter += 1
        if ghost_speed_counter >= 5:
            move_ghosts()
            ghost_speed_counter = 0  
        
        for ghost in ghosts:
            screen.blit(ghost["image"], (ghost["x"], ghost["y"]))
        
        handle_events()
        
        collision_result = check_collision()
        if collision_result == "game_over":
            game_over = True
        
        handle_power_pellet()
        check_power_mode()
        
        pacman_speed_counter += 1
        if pacman_speed_counter >= PACMAN_SPEED:
            new_x, new_y = pacman_x + pacman_dx, pacman_y + pacman_dy
            row, col = int(new_y // TILE_SIZE), int(new_x // TILE_SIZE)
            if 0 <= row < len(maze) and 0 <= col < len(maze[0]) and maze[row][col] != "1":
                if maze[row][col] == "0":
                    score += 50
                    maze_row = list(maze[row])
                    maze_row[col] = " "
                    maze[row] = "".join(maze_row)
                pacman_x, pacman_y = new_x, new_y
            pacman_speed_counter = 0
    else:
        font_big = pygame.font.Font('emulogic.ttf', 62)
        game_over_text = font_big.render("GAME OVER", True, RED)
        screen.blit(game_over_text, (250, 250))
        
        font = pygame.font.Font('emulogic.ttf', 26)
        restart_text = font.render("Presiona R para reiniciar", True, YELLOW)
        screen.blit(restart_text, (200, 320))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                lives = 3
                score = 0
                game_over = False
                reset_positions()
                maze = [row.replace(" ", "0") for row in maze]
                special_dots = []
                for row in range(len(maze)):
                    for col in range(len(maze[row])):
                        if (row == 1 and col == 1) or (row == 1 and col == 23) or \
                           (row == 13 and col == 1) or (row == 13 and col == 23):
                            special_dots.append((col * TILE_SIZE, row * TILE_SIZE))
    
    font = pygame.font.Font('emulogic.ttf', 26)
    score_text = font.render(f"HIGH SCORE:{score}", True, WHITE)
    screen.blit(score_text, (10, 0))

    font = pygame.font.Font('emulogic.ttf', 26)
    score_text = font.render(f"BY: MAURICIO LOPEZ AND JUAN RAMIREZ ", True, WHITE)
    screen.blit(score_text, (35, 560))

    font = pygame.font.Font('emulogic.ttf', 26)
    score_text = font.render(f"LIVES: ", True, WHITE)
    screen.blit(score_text, (745, 0))
    
    draw_lives()
    
    pygame.display.update()
    clock.tick(15)

pygame.quit()
