import pgzrun
import random
from pygame import Rect

# Configurações do jogo
WIDTH = 800
HEIGHT = 600
TITLE = "Bíblia Roguelike"

# Cores
WHITE = (255, 255, 255)

# Estado do jogo
game_state = "menu"

# Música e sons
music_on = True

# Personagem principal
hero = Actor("hero_idle", (WIDTH//2, HEIGHT//2))
hero.speed = 3
hero.frame = 0

# Lista de inimigos
enemies = [Actor("enemy_idle", (random.randint(50, WIDTH-50), random.randint(50, HEIGHT-50))) for _ in range(3)]
for enemy in enemies:
    enemy.direction = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])

# Função para desenhar os elementos na tela
def draw():
    screen.clear()
    if game_state == "menu":
        screen.draw.text("Bíblia Roguelike", center=(WIDTH//2, HEIGHT//3), color=WHITE, fontsize=50)
        screen.draw.text("Pressione ENTER para começar", center=(WIDTH//2, HEIGHT//2), color=WHITE, fontsize=30)
    elif game_state == "playing":
        hero.draw()
        for enemy in enemies:
            enemy.draw()
    elif game_state == "gameover":
        screen.draw.text("Game Over! Pressione R para reiniciar", center=(WIDTH//2, HEIGHT//2), color=WHITE, fontsize=40)

# Atualiza o jogo
def update():
    global game_state
    if game_state == "playing":
        move_hero()
        move_enemies()
        check_collisions()

# Movimentação do herói
def move_hero():
    if keyboard.left and hero.x > 20:
        hero.x -= hero.speed
    if keyboard.right and hero.x < WIDTH - 20:
        hero.x += hero.speed
    if keyboard.up and hero.y > 20:
        hero.y -= hero.speed
    if keyboard.down and hero.y < HEIGHT - 20:
        hero.y += hero.speed

# Movimentação dos inimigos
def move_enemies():
    for enemy in enemies:
        enemy.x += enemy.direction[0] * 2
        enemy.y += enemy.direction[1] * 2
        if random.random() < 0.01:
            enemy.direction = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])

# Verifica colisões
def check_collisions():
    global game_state
    for enemy in enemies:
        if hero.colliderect(enemy):
            game_state = "gameover"

# Controle de teclas
def on_key_down(key):
    global game_state
    if game_state == "menu" and key == keys.RETURN:
        game_state = "playing"
    elif game_state == "gameover" and key == keys.R:
        reset_game()

# Reiniciar o jogo
def reset_game():
    global game_state
    hero.pos = (WIDTH//2, HEIGHT//2)
    for enemy in enemies:
        enemy.pos = (random.randint(50, WIDTH-50), random.randint(50, HEIGHT-50))
    game_state = "playing"

pgzrun.go()