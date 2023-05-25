from PIL import ImageOps

# Importation des bibliothèques pour l'interface graphique
from PyQt6.QtCore import Qt
from utils import *

def inverser_image(img, label):
    if not img:
        return
    matrice_pixels = img.load()
    for y in range(img.height):
        for x in range(img.width):
            pixel = matrice_pixels[x, y]
            matrice_pixels[x, y] = (255 - pixel[0], 255 - pixel[1], 255 - pixel[2])
    pixmap = pilToPix(img)
    label.setPixmap(pixmap.scaled(1280,720, aspectRatioMode= Qt.AspectRatioMode(1)))

def noir_et_blanc_image(img, label):
    if not img:
        return
    matrice_pixels = img.load()
    for y in range(img.height):
        for x in range(img.width):
            luminance = int(0.2126 * matrice_pixels[x, y][0] + 0.7152 * matrice_pixels[x, y][1] + 0.0722 * matrice_pixels[x, y][2])
            matrice_pixels[x, y] = (luminance, luminance, luminance)
    pixmap = pilToPix(img)
    label.setPixmap(pixmap.scaled(1280,720, aspectRatioMode= Qt.AspectRatioMode(1)))

def gris_image(img, label): #TODO mettre en niveaux de gris
    if img:
        try:
            
            # Traitement de l'image BMP
            img = ImageOps.grayscale(img)

            # Affichage de l'image traitée dans le label
            #pixmap = QPixmap.fromImage(ImageQt(img))
            pixmap = pilToPix(img)
            label.setPixmap(pixmap.scaled(1280,720, aspectRatioMode= Qt.AspectRatioMode(1)))
        except Exception as e:
            print("Erreur lors du traitement de l'image :", e)
            
def sepia_image(img):
    if not img:
        return
    #SOON