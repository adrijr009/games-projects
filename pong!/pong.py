#!/usr/bin/python

## importando modulo ##
import pygame
## definindo cores em RGB ##
black = (0,0,0)
white = (255,255,255)
## defindo clock, para renderização por quadros ##
clock = pygame.time.Clock()
## inciador do game ##
try:
    pygame.init()
except:
    print('ERRO')
## variaveis para tamanho da tela ##
width = 600
height = 440
## definições de tela ##
tela = pygame.display.set_mode((width,height))
pygame.display.set_caption("Pong!")
## variaveis placar ##
j1_p = 0
j2_p = 0
## dimensão os objetos por posição ##
j1_x = 20
j1_y = 170
j2_x = 560
j2_y = 170
ball_x = 280
ball_y = 200
## variavel de velocidade da bola ##
ball_vx = 3
ball_vy = 3
## variavel para pausa ##
pause = False
## variavel para sair ##
sair = True
## som de colisão ##
colisao_audio = pygame.mixer.Sound('collision.wav')
while sair:
    ## variavel para capturar eventos ##
    key = pygame.key.get_pressed()
    ## definição de textos
    font = pygame.font.Font('Gameplay.ttf', 20)
    text_p1 = font.render("Player 1", True, white)
    text_p2 = font.render("Player 2", True, white)
    text = font.render("PAUSE", True, white)
    placar_1 = font.render("{}".format(j1_p), True, white)
    placar_2 = font.render("{}".format(j2_p), True, white)
    text_p1Rect = text_p1.get_rect()
    text_p1Rect.center = (150,20)
    text_p2Rect = text_p2.get_rect()
    text_p2Rect.center = (450,20)
    textRect = text.get_rect()
    textRect.center = (300,220)
    placar_1Rect = text_p1.get_rect()
    placar_1Rect.center = (150,50)
    placar_2Rect = text_p2.get_rect()
    placar_2Rect.center = (450,50)
   ## comando para pausa e print de "PAUSE" ## 
    if pause:
        tela.blit(text,textRect)
        pygame.display.update()       
    for event in pygame.event.get():      
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pause = not pause
        if event.type == pygame.QUIT:
            sair = False
    if pause: continue
    ## linha central ##
    pygame.draw.line(tela, white, (300,0),(300,440),4)
    pygame.display.update()
    pygame.display.flip()
    ## comando de subir e descer ##
    if key[pygame.K_w] and j1_y > 0: j1_y -= 4
    if key[pygame.K_s] and j1_y < 340 : j1_y += 4
    if key[pygame.K_UP] and j2_y > 0 : j2_y -= 4
    if key[pygame.K_DOWN] and j2_y < 340 : j2_y += 4
    ## fundo preto ##
    tela.fill(black)
    ## comandos para colisão ##
    if ball_x >= 580:
        ball_x = 280
        ball_y = 200
        ball_vx *= -1
        
        j1_p += 1
        ball_vx = 3
        ball_vy = 3
        ball_vx *= -1
    if ball_x < 1:
        ball_x = 280
        ball_y = 200
        ball_vx *= -1
        
        j2_p +=1
        ball_vx = 3
        ball_vy = 3
        
    if ball_y > 419:
        ball_vy *= -1
    if ball_y < 1:
        ball_vy *= -1

    ## objetos ##
    j1 = pygame.draw.rect(tela, white, [j1_x,j1_y,20,100])
    j2 = pygame.draw.rect(tela, white, [j2_x,j2_y,20,100])
    ball = pygame.draw.rect(tela, white, [ball_x,ball_y,20,20])
    ## colisão ##
    if j1.colliderect(ball):
        colisao_audio.play()        
        if ball_vx < 0:
            ball_vx -= 0.2
            ball_vy -= 0.2
        else :
            ball_vx += 0.2
            ball_vy += 0.2
        ball_x += 3
        ball_vx *= -1
    if j2.colliderect(ball):
        colisao_audio.play()
        if ball_vx < 0:
            ball_vx -= 0.2
            ball_vy -= 0.2
        else :
            ball_vx += 0.2
            ball_vy += 0.2  
        ball_x -= 3
        ball_vx *= -1   
    ## print textos ##
    tela.blit(text_p1,text_p1Rect)
    tela.blit(text_p2,text_p2Rect)
    tela.blit(placar_1,placar_1Rect)
    tela.blit(placar_2,placar_2Rect)
    ## movimento da bola ##
    ball_x += ball_vx
    ball_y += ball_vy
    clock.tick(100)
pygame.quit()

