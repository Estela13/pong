from pong import ANCHO, ALTO
import pygame as pg
from pong.pantallas import Menu, Partida, Records


class Controlador:
    def __init__(self):
       pantalla_principal = pg.display.set_mode((ANCHO, ALTO))
       metronomo = pg.time.Clock()

       self.pantallas = [Menu(pantalla_principal, metronomo), Partida(pantalla_principal, metronomo)]

       self.menu = Menu(pantalla_principal, metronomo)
       self.partida = Partida(pantalla_principal, metronomo)
       
    def start(self):
        salida = False
        ix = 0
        while not salida:
            salida = self.pantallas[ix].bucle_ppal()
            ix += 1
            if ix >= len(self.pantallas):
                ix = 0
      
      #es lo mismo que: ix = (ix + 1) % len(self.pantallas)
        
        
            

