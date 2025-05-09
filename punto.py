import pygame
from config import *

class puntos:
    def __init__(self, lab):
        self.lista = [(x, y) for y in range(len(lab)) for x in range(len(lab[0])) if lab[y][x] == 0]
        self.puntaje = 0
        self.fuente = pygame.font.SysFont("Arial", 20)

    def dibujar(self, ventana):
        for x, y in self.lista:
            centro = (x * TAM_CELDA + TAM_CELDA//2, y * TAM_CELDA + TAM_CELDA//2)
            pygame.draw.circle(ventana, ROJO, centro, 4)

    def verificar_colision(self, jugador):
        if tuple(jugador.pos) in self.lista:
            self.lista.remove(tuple(jugador.pos))
            self.puntaje += 1

    def mostrar_puntaje(self, ventana):
        texto = self.fuente.render(f"Puntaje: {self.puntaje}", True, BLANCO)
        ventana.blit(texto, (10, 10))
