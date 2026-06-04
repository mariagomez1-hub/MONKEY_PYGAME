
import random
import pygame

from settings import *
from src.mono import MONO
from src.banano import BANANO
from src.hud import VER_MARCADOR

def main() -> None:
    pygame.mixer.init()
    pygame.init()


    screen = pygame.display.set_mode((ANCHURA, ALTURA))
    pygame.display.set_caption('El juego del mono y el banano')

    
    lista_mono = pygame.sprite.Group()
    lista_banano = pygame.sprite.Group()
    lista_global = pygame.sprite.Group()

    
    sfx_perdido = pygame.mixer.Sound("assets/sounds/PERDER.wav")
    sfx_perdido.set_volume(1.0)


    # Pasamos los grupos correspondientes al constructor del MONO
    mono = MONO(lista_banano, lista_global)
    lista_global.add(mono)
    lista_mono.add(mono)

    # Creamos el primer banano al iniciar
    banano_inicial = BANANO(lista_global)
    lista_global.add(banano_inicial)
    lista_banano.add(banano_inicial)

    reloj = pygame.time.Clock()
    termina = False
    print("Empezamos...")

    # --- Bucle principal ---
    while not termina:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                termina = True

            

        
        lista_global.update()

        
        screen.fill(BLANCO)
        lista_global.draw(screen)

    
        VER_MARCADOR(screen, mono.PUNTOS)

        
        if mono.TERMINA:
            sfx_perdido.play()
            pygame.time.wait(5000)
            termina = True

        pygame.display.flip()
        reloj.tick(FPS)

    print(f"Su marcador: {mono.PUNTOS} puntos")
    pygame.quit()

if __name__ == "__main__":
    main()