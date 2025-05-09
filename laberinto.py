import pygame
from config import *

laberinto = [
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,1,0,0,0,0,1],
    [1,0,1,0,0,0,1,0,0,1],
    [1,0,1,0,1,0,1,1,0,1],
    [1,0,1,0,1,0,0,1,0,1],
    [1,0,1,0,1,1,0,1,0,1],
    [1,0,0,0,0,0,0,1,0,1],
    [1,1,1,1,1,1,1,1,1,1],
]

def dibujar_laberinto(ventana):
    for y, fila in enumerate(laberinto):
        for x, celda in enumerate(fila):
            if celda == 1:
                pygame.draw.rect(ventana, AZUL, (x*TAM_CELDA, y*TAM_CELDA, TAM_CELDA, TAM_CELDA))

def es_pared(x, y):
    return laberinto[y][x] == 1
