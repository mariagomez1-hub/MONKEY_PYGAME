# --- Colores ---
import os


NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)


BALDOSA_TAMANIO = 32
BALDOSA_NUMERO  = 15
MARCADOR_ANCHURA = 32

ALTURA  = BALDOSA_TAMANIO * BALDOSA_NUMERO
ANCHURA = BALDOSA_TAMANIO * BALDOSA_NUMERO + MARCADOR_ANCHURA


MONO_ANCHO = 80
MONO_ALTO  = 80
BANANO_ANCHO = 32
BANANO_ALTO  = 32


PUNTO_UNIDAD = 1
FPS = 60                       
BANANO_VELOCIDAD_INICIAL = 4   
MONO_VELOCIDAD = 8             


BASE_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")


RUTA_MONO    = os.path.join(BASE_DIR, "images", "MONO.png")
RUTA_BANANO  = os.path.join(BASE_DIR, "images", "BANANO.png")


RUTA_SFX_MONO  = os.path.join(BASE_DIR, "sounds", "MONO.mp3")
RUTA_SFX_PERDER = os.path.join(BASE_DIR, "sounds", "PERDER.mp3")
