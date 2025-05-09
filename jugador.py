import pygame
from config import *
from laberinto import es_pared

class jugador:
    def __init__(self):
        self.pos = (1, 1)  # Define self.pos como una tupla con x y y

    def mover(self, teclas):
        nuevo_x, nuevo_y = self.pos  # Accede a la tupla pos

        if teclas[pygame.K_LEFT]:
            nuevo_x -= 1
        elif teclas[pygame.K_RIGHT]:
            nuevo_x += 1
        elif teclas[pygame.K_UP]:
            nuevo_y -= 1
        elif teclas[pygame.K_DOWN]:
            nuevo_y += 1

        # Verifica colisión con pared
        if not es_pared(nuevo_x, nuevo_y):
            self.pos = (nuevo_x, nuevo_y)  # Actualiza la tupla pos

    def dibujar(self, ventana):
        # Usa self.pos en lugar de self.x y self.y
        x, y = self.pos  # Desempaqueta la tupla
        x = x * TAM_CELDA
        y = y * TAM_CELDA
        pygame.draw.circle(ventana, AMARILLO, (x + TAM_CELDA//2, y + TAM_CELDA//2), TAM_CELDA//2 - 2)

