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



while not game_over:
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            game_over = True
    
    pantalla_principal.fill((0, 0, 0))         #color de fondo de pantalla
    bola.dibujar(pantalla_principal)
    raqueta1.dibujar(pantalla_principal)
    raqueta2.dibujar(pantalla_principal)
    pg.display.flip()                          #pasa la información a la pantalla 

