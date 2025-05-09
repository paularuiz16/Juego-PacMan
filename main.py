import pygame
from jugador import jugador
from fantasma import fantasma
from laberinto import laberinto, dibujar_laberinto, es_pared
from punto import puntos
from config import *

pygame.init()
pygame.display.set_caption("PacMan")
ventana = pygame.display.set_mode((ANCHO, ALTO))
reloj = pygame.time.Clock()

jugador = jugador()
fantasma = fantasma(5,5)
puntos = puntos(laberinto)

ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    teclas=pygame.key.get_pressed()
    jugador.mover(teclas)
    fantasma.mover()

    if jugador.pos == fantasma.pos:
        ejecutando = False
        print("Game Over")

    puntos.verificar_colision(jugador)

    ventana.fill(NEGRO)
    dibujar_laberinto(ventana)
    puntos.dibujar(ventana)
    jugador.dibujar(ventana)
    fantasma.dibujar(ventana)
    puntos.mostrar_puntaje(ventana)

    pygame.display.flip()
    reloj.tick(5)

pygame.quit()
