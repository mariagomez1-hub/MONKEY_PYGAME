import pygame
from settings import *

# CLASE MONO
class MONO(pygame.sprite.Sprite):
    def __init__(self, lista_banano, lista_global):
        pygame.sprite.Sprite.__init__(self)

        self.lista_banano = lista_banano
        self.lista_global = lista_global

        self.SONIDO_MONO = pygame.mixer.Sound("assets/sounds/MONO.mp3")
        self.SONIDO_MONO.set_volumen(1.0)

        self.image = pygame.image.load("assets/images/MONO.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (MONO_ANCHO, MONO_ALTO))
        self.rect = self.image.get_rect()

        self.rect.x = (ANCHO_PANTALLA // 2) - (MONO_ANCHO // 2)
        self.rect.y = ALTO_PANTALLA - MONO_ALTO - 15  

        self.PUNTOS = 0
        self. TERMINA = False

    def update(self):
        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= MONO_VELOCIDAD

        if teclas[pygame.K_RIGHT] and self.rect.x < ANCHO_PANTALLA - MONO_ANCHO:
            self.rect.x += MONO_VELOCIDAD

        LISTA_COLISION = pygame.sprite.spritecollide(self,self.lista_banano, False)

        for banano in LISTA_COLISION_BANANO:
            self.PUNTOS += PUNTO_MONO
            self.SONIDO_MONO.play()
            banano.REINICIAR_POSICION()
            banano.VELOCIDAD += 0.5

        for banano in self.lista_banano:
            if banano.rect.y > ALTO_PANTALLA:
                print("Perdido: La banana toco el suelo")
                self.TERMINA= True
