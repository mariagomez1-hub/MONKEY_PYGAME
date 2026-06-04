import pygame
import random

class Banana:
    def __init__(self, ancho_pantalla):
        self.ancho_pantalla = ancho_pantalla
        self.imagen  = pygame.image.load("assets/images/BANANO.png")
        self.imagen = pygame.transform.scale(self.imagen, (40, 40))

        self.rect = self.imagen.get_rect()
        self.velocidad = 5
        self.reiniciar() 

    def reiniciar(self):
        self.rect.x = random.randint(0, self.ancho_pantalla - self.rect.width)
        self.rect.y = -self.rect.height

    def actualizar(self):
        self.rect.y += self.velocidad

    def dibuujar(self,superficie):
        superficie.blit(self.imagen, self.rect)        