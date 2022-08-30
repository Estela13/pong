from curses import KEY_DOWN
import pygame as pg
import random
from entidades import Bola, Raqueta

pg.init()

pantalla_principal = pg.display.set_mode((800, 600))
pg.display.set_caption("pong")

game_over = False
bola = Bola(400, 300)
raqueta1 = Raqueta(20, 300, w=20, h=120, color = (0, 0, 255))
raqueta2 = Raqueta(780, 300, w=20, h=120, color = (0, 0, 255))
raqueta2.vy = 5


while not game_over:
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            game_over = True
        elif evento.type == pg.KEYDOWN:
            if evento.key == pg.K_DOWN:
                raqueta2.center_y += raqueta2.vy
            elif evento.key == pg.K_UP:
                raqueta2.center_y -= raqueta2.vy

    
    estado_teclas = pg.key.get_pressed()
    if estado_teclas[pg.K_UP] == True:
        raqueta2.center_y -= raqueta2.vy
    if estado_teclas[pg.K_DOWN] == True:
        raqueta2.center_y += raqueta2.vy
    
    pantalla_principal.fill((0, 0, 0))         #color de fondo de pantalla
    bola.dibujar(pantalla_principal)
    raqueta1.dibujar(pantalla_principal)
    raqueta2.dibujar(pantalla_principal)
    pg.display.flip()                          #pasa la información a la pantalla 

