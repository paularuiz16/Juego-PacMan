import pygame
import random
from config import *  
from laberinto import es_pared

class fantasma:
    def __init__(self, x, y, color=ROJO):  # Asegúrate de que 'color' se pase al constructor
        self.pos = (x, y)  # Atributo 'pos' como tupla
        self.color = color  # Inicializa el atributo 'color'

    def mover(self):
        direcciones = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        random.shuffle(direcciones)

        for dx, dy in direcciones:
            nuevo_x = self.pos[0] + dx  # Usa self.pos[0] para x
            nuevo_y = self.pos[1] + dy  # Usa self.pos[1] para y
            if not es_pared(nuevo_x, nuevo_y):
                self.pos = (nuevo_x, nuevo_y)  # Actualiza la posición con la tupla

    def dibujar(self, ventana):
        x, y = self.pos 
        pygame.draw.rect(ventana, self.color, 
                         (x * TAM_CELDA, y * TAM_CELDA, TAM_CELDA, TAM_CELDA))
