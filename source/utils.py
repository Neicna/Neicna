# Importation des bibliothèques pour l'interface graphique
from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtCore import Qt

# Importation de la bibliothèque Python pour lire et écrire des fichiers BMP
from PIL import Image

def pilToPix(image):
    try:
        image = image.convert("RGBA")
        data = image.tobytes("raw","RGBA")
        qim = QImage(data, image.size[0], image.size[1], QImage.Format.Format_RGBA8888)
        pix = QPixmap.fromImage(qim)
        return pix
    except Exception as e:
        print("Erreur lors de la transformation de l'image :", e)

def nouveau_image(self):
    self.image = Image.new("RGB", (1080, 720), (255, 255, 255))
    pixmap = pilToPix(self.image)
    self.image_label.setPixmap(pixmap.scaled(1080,720, aspectRatioMode= Qt.AspectRatioMode(1)))

def ouvrir_image(self): 
    # Ouverture de la boîte de dialogue pour la sélection du fichier
    chemin_fichier, _ = QFileDialog.getOpenFileName(self, "Ouvrir une image", "", "Images (*.bmp)")

    if chemin_fichier:
        try:
            # Changement de l'affichage
            pixmap = QPixmap(chemin_fichier)
            self.image_label.setPixmap(pixmap.scaled(1280,720, aspectRatioMode= Qt.AspectRatioMode(1)))

            # Chargement de l'image BMP
            self.image = Image.open(chemin_fichier)
            
            if self.image.mode != "RGB":
                self.image = self.image.convert('RGB')
        except Exception as e:
            print("Erreur lors du chargement de l'image :", e)

def enregistrer_image(self):
    if self.image:
        # Ouverture de la boîte de dialogue pour la sélection du fichier de destination
        chemin_fichier, _ = QFileDialog.getSaveFileName(self, "Enregistrer l'image", "", "Images (*.bmp)")

        if chemin_fichier:
            # Enregistrement de l'image BMP
            self.image.save(chemin_fichier)

def afficher_image(self):
    if self.image:
        matrice_pixels = self.image.load()
        for y in range(self.image.height):
            for x in range(self.image.width):
                pixel = matrice_pixels[x, y]
                print(pixel, end=" ")
        print("---------------------------------------------------------")