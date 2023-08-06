import pygame
from random import randint 
import math


# Inicia o Pygame
pygame.init()

# Abre a Tela
screen = pygame.display.set_mode((800,600))

# Imagem e Música de Background 
background = pygame.image.load('background.png')
pygame.mixer.music.load('background.wav')
pygame.mixer.music.play(-1)

# Titulo e Icone da Tela
pygame.display.set_caption("Unimate - Space Invaders")
icone = pygame.image.load('espaco-sideral.png')
pygame.display.set_icon(icone)

# Pontuação
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

# Texto de Game Over
over_font = pygame.font.Font('freesansbold.ttf', 64)

# Jogador
playerImg = pygame.image.load('nave-espacial.png')
playerX = 370
playerY = 470
playerX_change = 0

# Inimigos
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('alien.png'))
    enemyX.append(randint(0,735))
    enemyY.append(randint(50, 150))
    enemyX_change.append(10)
    enemyY_change.append(40)

# Laser
laserImg = pygame.image.load('laser.png')
laserX = 400
laserY = 480
laserX_change = 0
laserY_change = 10
laser_state = "ready"
# Ready - não é possível ver o laser
# Fire - o laser está se movendo

# Funções do Jogo

# Função para Posição do Jogador
def player(x,y):
    screen.blit(playerImg, (x, y))

# Função para Posição do Inimigo
def enemy(x,y,i):
    screen.blit(enemyImg[i], (x, y))

# Função para Posição do Laser
def fire_laser(x,y):
    global laser_state
    laser_state = "fire"
    screen.blit(laserImg, (x+16, y+10))

# Função para Detecção de Colisão Inimigo-Laser
def isCollision(enemyX, enemyY, laserX, laserY):
    distance = math.sqrt((math.pow(enemyX - laserX, 2)) + (math.pow(laserY - enemyY, 2)))
    if distance < 27:
        return True
    else:
        return False
    
# Função para Pontuação
def show_score(x,y):
    score = font.render("Score: " + str(score_value),True, (230,230,255))
    screen.blit(score, (x, y))

# Função para Texto de Game Over
def game_over_text():
    over_text = over_font.render("Game Over!",True, (255,10,60))
    screen.blit(over_text, (215, 270))

# Rodar o Jogo

# Looping do Jogo (Deixar Rodando até o Usuário Fechar)
running = True
while running:

    # Rodar o Background
    screen.blit(background,(0,0))

    # Detectar "Eventos" do Jogador
    for event in pygame.event.get():

        # Fechar o programa no X
        if event.type == pygame.QUIT:
            running = False

        # Movimentação em Teclado
        
        # Se alguma tecla é pressionada
        if event.type == pygame.KEYDOWN:

            # Verifica se é o botão esquerdo ou direito 
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5

            # Se a tecla espaço é pressionada
            if event.key == pygame.K_SPACE:
                if laser_state is "ready":
                    laser_Sound = pygame.mixer.Sound('laser.wav')
                    laser_Sound.play()
                    laserX = playerX
                    fire_laser(laserX, laserY)

        # Se alguma tecla é soltada
        if event.type == pygame.KEYUP:

            # Verifica se é o botão esquerdo ou direito 
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Movimentação do Jogador
    playerX += playerX_change
    player(playerX, playerY)

    # Bordas para Jogador 
    if playerX <= 0:
        playerX = 0
    if playerX >= 736:
        playerX = 736

    # Interações com o Inimigo
    for i in range(num_of_enemies):

        # Game Over!
        if enemyY[i] > 430:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break
    
        # Movimentação do Inimigo
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = randint(3, 6)
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -randint(3, 6)
            enemyY[i] += enemyY_change[i] 

        # Colisão Inimigo-Laser
        collision = isCollision(enemyX[i], enemyY[i], laserX, laserY)
        if collision:
           explosion_Sound = pygame.mixer.Sound('explosion.wav')
           explosion_Sound.play()
           laserY = 480
           laser_state = "ready"
           score_value += 1
           enemyX[i] = randint(0,735)
           enemyY[i] = randint(50, 150)
        enemy(enemyX[i], enemyY[i], i)

    # Movimentação do Laser
    if laserY <= 0:
        laserY = 480
        laser_state = "ready"
    if laser_state is "fire":
        fire_laser(laserX, laserY)
        laserY -= laserY_change

    # Mostrar Pontuação
    show_score(textX, textY)

    pygame.display.update()
