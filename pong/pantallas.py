from mimetypes import init
from string import punctuation
from tkinter import NE
import pygame as pg
from pong.entidades import Bola, Raqueta
from pong import AMARILLO, ANCHO, ALTO, BLANCO, NARANJA, NEGRO, PUNTUACION_GANADORA, ROJO, FPS, PRIMER_AVISO, SEGUNDO_AVISO, TIEMPO_MAXIMO_PARTIDA
pg.init()

class Partida:
    def __init__(self, pantalla, metronomo):
        self.pantalla_principal = pantalla
        pg.display.set_caption("Pong")
        self.metronomo = metronomo
        self.cronometro = TIEMPO_MAXIMO_PARTIDA

        self.bola = Bola(ANCHO // 2, ALTO //2, color=BLANCO)
        self.raqueta1 = Raqueta(20, ALTO//2, w=30, h=114)
        self.raqueta1.direccion = 'izqda'

        self.raqueta1.vy = 5

        self.raqueta2 = Raqueta(ANCHO - 20, ALTO//2, w=30, h=114)
        self.raqueta2.direccion = 'drcha'
        self.raqueta2.vy = 5

        self.puntuacion1 = 0
        self.puntuacion2 = 0

        self.fuenteMarcador = pg.font.Font("pong/fonts/silkscreen.ttf", 40)
        self.fuenteCronometro = pg.font.Font("pong/fonts/silkscreen.ttf", 20)

        self.contadorFotogramas = 0
        self.fondoPantalla = NEGRO


 #cambiar colores del fondo según el tiempo que falte 
    def fijar_fondo(self):
        self.contadorFotogramas += 1

        if self.cronometro > PRIMER_AVISO:
            self.contadorFotogramas = 0
            self.fondoPantalla = NEGRO
        elif self.cronometro > SEGUNDO_AVISO:
            #cada 10 fotogramas cambia de naranja a negro y viceversa
            if self.contadorFotogramas == 10:
                if self.fondoPantalla == NEGRO:
                    self.fondoPantalla = NARANJA
                else:
                    self.fondoPantalla = NEGRO
                self.contadorFotogramas = 0
        else:
            #cada 5 fotogramas cambia de rojo a negro y viceversa
            if self.contadorFotogramas >= 5:
                if self.fondoPantalla == ROJO:
                    self.fondoPantalla = NEGRO
                else:
                    self.fondoPantalla = ROJO
                self.contadorFotogramas = 0

        return self.fondoPantalla

    def bucle_ppal(self):
        self.bola.vx = 5
        self.bola.vy = -5
        self.puntuacion1 = 0
        self.puntuacion2 = 0
        self.cronometro = TIEMPO_MAXIMO_PARTIDA    #vuelvo a poner el temporizador a 15 segundos


        game_over = False
        self.metronomo.tick()

        while not game_over and \
            self.puntuacion1 < PUNTUACION_GANADORA and \
            self.puntuacion2 < PUNTUACION_GANADORA and \
            self.cronometro > 0:
              
            salto_tiempo = self.metronomo.tick(FPS)
            self.cronometro -= salto_tiempo
            #if self.cronometro < 0:
            #    game_over = True
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    return True

            self.raqueta2.mover(pg.K_UP, pg.K_DOWN)
            self.raqueta1.mover(pg.K_a, pg.K_z)
            #marcadores
            quien = self.bola.mover()
            if quien == "RIGHT":
                self.puntuacion2 += 1
                print(f"{self.puntuacion1} - {self.puntuacion2}")
            elif quien == "LEFT":
                self.puntuacion1 += 1
                print(f"{self.puntuacion1} - {self.puntuacion2}")

            #if self.puntuacion1 > 9 or self.puntuacion2 > 9:
            # game_over = True

            self.bola.comprobar_choque(self.raqueta1, self.raqueta2)

        
            self.pantalla_principal.fill(self.fijar_fondo())
            self.bola.dibujar(self.pantalla_principal)
            self.raqueta1.dibujar(self.pantalla_principal)
            self.raqueta2.dibujar(self.pantalla_principal)

            p1 = self.fuenteMarcador.render(str(self.puntuacion1), True, BLANCO)
            p2 = self.fuenteMarcador.render(str(self.puntuacion2), True, BLANCO)
            contador = self.fuenteCronometro.render(str(self.cronometro / 1000), True, BLANCO)
            self.pantalla_principal.blit(p1,(10,10))
            self.pantalla_principal.blit(p2, (ANCHO - 45, 10))
            self.pantalla_principal.blit(contador, (ANCHO // 2, 10))
            pg.display.flip()

class Menu:
    def __init__(self, pantalla, metronomo):
        self.pantalla_principal = pantalla
        pg.display.set_caption("Menu")
        self.metronomo = metronomo
        self.imagenFondo = pg.image.load("Imagen/pingpong.png")
        self.fuenteComenzar = pg.font.Font("pong/fonts/silkscreen.ttf", 30)
        self.musica = pg.mixer.Sound("pong/sounds/duelo.ogg")

    def bucle_ppal(self):
        game_over = False
        self.musica.play(-1)

        while not game_over:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    return True
                
                if evento.type == pg.KEYDOWN:
                    if evento.key == pg.K_RETURN:
                        game_over = True
                    
            
            #blit para superponer surfaces
            self.pantalla_principal.blit(self.imagenFondo, (0,0))
            menu = self.fuenteComenzar.render("Pulsa ENTER para comenzar", True, AMARILLO)
            self.pantalla_principal.blit(menu, (ANCHO // 7 , ALTO - 200))
            pg.display.flip()
        self.musica.stop()

class Records:

    def __init__(self):
        self.pantalla_principal = pg.display.set_mode((ANCHO, ALTO))
        pg.display.set_caption("Records")
        self.metronomo = pg.time.Clock()
        self.fuenteComenzar = pg.font.Font("pong/fonts/silkscreen.ttf", 50)

    def bucle_ppal(self):
        game_over = False

        while not game_over:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    game_over = True
                
                if evento.type == pg.KEYDOWN:
                    if evento.key == pg.K_RETURN:
                        game_over = True
            
            self.pantalla_principal.fill((0, 0, 250))
            menu = self.fuenteComenzar.render("Ha ganado Pancho", True, NARANJA)
            self.pantalla_principal.blit(menu, (ANCHO // 2, ALTO - 200))
            pg.display.flip()
                    