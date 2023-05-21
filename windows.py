# pylint: disable=E1101, module=pygame

# Primero, importamos los módulos necesarios.
# "pygame" es el módulo que nos permite crear videojuegos.
# "sys" es un módulo que proporciona acceso a algunas variables y funciones que interactúan con el intérprete de Python.
import pygame
from sys import exit

# "pygame.init()" es como el encendido de un coche. Prepara todas las funcionalidades de pygame para que podamos usarlas.
pygame.init()

# Creamos una "pantalla" para nuestro juego. Esta será la ventana donde se mostrarán todos los elementos del juego.
# El tamaño de la pantalla es de 800 pixeles de ancho y 400 pixeles de alto.
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("El pato corredor")
clock = pygame.time.Clock()

# Este es el bucle principal de nuestro juego. Todo el código dentro de este bucle se ejecutará una y otra vez, lo que nos permitirá mover y actualizar los elementos del juego en tiempo real.
while True:
    # Pygame maneja todos los eventos (como pulsaciones de teclas y movimientos del ratón) en una cola de eventos. Con "pygame.event.get()" podemos gestionar cada uno de estos eventos.
    for event in pygame.event.get():
        # Si el evento es de tipo "QUIT" (por ejemplo, si el jugador cierra la ventana del juego), entonces salimos del juego.
        if event.type == pygame.QUIT:
            # "pygame.quit()" finaliza todos los módulos de pygame. Es como apagar el motor del coche.
            pygame.quit()
            # "exit()" cierra completamente el programa.
            exit()
    # Aquí es donde pondríamos el código para dibujar todos los elementos en la pantalla.
    # Aquí es donde pondríamos el código para actualizar todos los elementos del juego.

    # "pygame.display.update()" actualiza la pantalla con todo lo que hayamos dibujado.
    pygame.display.update()
    clock.tick(60)
