# Importation de la bibliothèque Python pour lire et écrire des fichiers BMP
from PIL import Image, ImageOps
from PIL.ImageQt import ImageQt

# Importation des bibliothèques pour l'interface graphique
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QFileDialog, QPushButton, QVBoxLayout, QWidget, QDialog, QLineEdit, QToolBar, QSpinBox, QColorDialog
from PyQt6.QtGui import QPixmap, QAction, QImage, QIcon
from PyQt6.QtCore import Qt

import random
import math

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Définition de la fenêtre principale
        self.setWindowTitle("PyPicture")
        self.setGeometry(100, 100, 800, 600)
        self.setWindowIcon(QIcon(r"templates\icon.webp"))

        # Définition des actions de la barre de menu
        ouvrir_action = QAction("Ouvrir", self)
        ouvrir_action.setShortcut("Ctrl+O")
        ouvrir_action.triggered.connect(self.ouvrir_image)

        nouveau_action = QAction("Nouveau", self)
        nouveau_action.setShortcut("Ctrl+N")
        nouveau_action.triggered.connect(self.nouveau_image)

        enregistrer_action = QAction("Enregistrer", self)
        enregistrer_action.setShortcut("Ctrl+S")
        enregistrer_action.triggered.connect(self.enregistrer_image)

        negatif_action = QAction("Négatif", self)
        #negatif_action.setShortcut("")
        negatif_action.triggered.connect(self.inverser_image)

        noir_et_blanc_action = QAction("Noir et Blanc", self)
        noir_et_blanc_action.triggered.connect(self.noir_et_blanc_image)

        sepia_action = QAction("Sépia", self)
        sepia_action.triggered.connect(self.sepia_image)

        gris_action = QAction("Niveaux gris", self)
        #test_action.setShortcut("")
        gris_action.triggered.connect(self.gris_image)

        rsa_action = QAction("Chiffrement RSA", self)
        rsa_action.triggered.connect(self.crypter_image)

        cesar_action = QAction("Code César", self)
        cesar_action.triggered.connect(self.crypter_image)

        cesarPlus_action = QAction("Code César +", self)
        cesarPlus_action.triggered.connect(self.crypter_image)

        dersa_action = QAction("Déchiffrer RSA", self)
        dersa_action.triggered.connect(self.decrypter)

        decesar_action = QAction("Déchiffrer César", self)
        decesar_action.triggered.connect(self.decrypter)

        decesarPlus_action = QAction("Déchiffrer César +", self)
        decesarPlus_action.triggered.connect(self.decrypter)

        afficher_action = QAction("Afficher", self)
        afficher_action.triggered.connect(self.afficher_image)

        # Création de la barre de menu
        menu_bar = self.menuBar()
        
        fichier_menu = menu_bar.addMenu("Fichier")
        fichier_menu.addAction(nouveau_action)
        fichier_menu.addAction(ouvrir_action)
        #TODO ouvre le dernier si un a été ouvert
        #fichier_menu.addAction(ouvrir_recent_action)
        fichier_menu.addAction(enregistrer_action)
        #TODO fermer l'app
        #fichier_menu.addAction(fermer_action)
        
        dessin_menu = menu_bar.addMenu("Dessin")
        #dessin_menu.addAction()

        traitement_menu = menu_bar.addMenu("Traitement")
        traitement_menu.addAction(negatif_action)
        traitement_menu.addAction(gris_action)
        traitement_menu.addAction(noir_et_blanc_action)
        traitement_menu.addAction(sepia_action)
       
        message_menu = menu_bar.addMenu("Message")
        crypter_menu = message_menu.addMenu("Crypter")
        crypter_menu.addAction(rsa_action)
        crypter_menu.addAction(cesar_action)
        crypter_menu.addAction(cesarPlus_action)
        decrypter_menu = message_menu.addMenu("Decrypter")
        decrypter_menu.addAction(dersa_action)
        decrypter_menu.addAction(decesar_action)
        decrypter_menu.addAction(decesarPlus_action)

        debuggage_menu = menu_bar.addMenu("Débuggage")
        debuggage_menu.addAction(afficher_action)

        # Création du label pour l'affichage de l'image
        self.image_label = QLabel(self) #mettre une taille constante pour l affichage de l'image ou alors une var
        #self.image_label.setPixmap(QPixmap(r"samples\shrek-5.bmp"))
        margin = 100
        self.image_label.setMaximumSize(1280+margin, 720+margin)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_label.setMargin(margin)

        # Création du layout vertical pour la fenêtre principale
        layout = QVBoxLayout()
        #layout.addWidget(traitement_bouton)
        layout.addWidget(self.image_label)

        # Création du widget pour la fenêtre principale
        widget = QWidget()
        widget.setLayout(layout)
        widget.setStyleSheet("background-color: lightgray;")

        # Définition du widget principal de la fenêtre
        self.setCentralWidget(widget)

        # Initialisation de l'image
        self.image = None

    def pilToPix(self, image):
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
        pixmap = self.pilToPix(self.image)
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

    def inverser_image(self):
        if not self.image:
            return
        matrice_pixels = self.image.load()
        for y in range(self.image.height):
            for x in range(self.image.width):
                pixel = matrice_pixels[x, y]
                matrice_pixels[x, y] = (255 - pixel[0], 255 - pixel[1], 255 - pixel[2])
        pixmap = self.pilToPix(self.image)
        self.image_label.setPixmap(pixmap.scaled(1280,720, aspectRatioMode= Qt.AspectRatioMode(1)))

    def noir_et_blanc_image(self):
        if not self.image:
            return
        matrice_pixels = self.image.load()
        for y in range(self.image.height):
            for x in range(self.image.width):
                luminance = int(0.2126 * matrice_pixels[x, y][0] + 0.7152 * matrice_pixels[x, y][1] + 0.0722 * matrice_pixels[x, y][2])
                matrice_pixels[x, y] = (luminance, luminance, luminance)
        pixmap = self.pilToPix(self.image)
        self.image_label.setPixmap(pixmap.scaled(1280,720, aspectRatioMode= Qt.AspectRatioMode(1)))


    def sepia_image(self):
        if not self.image:
            return
        #SOON

    def gris_image(self): #TODO mettre en niveaux de gris
        if self.image:
            try:
                
                # Traitement de l'image BMP
                self.image = ImageOps.grayscale(self.image)

                # Affichage de l'image traitée dans le label
                #pixmap = QPixmap.fromImage(ImageQt(self.image))
                pixmap = self.pilToPix(self.image)
                self.image_label.setPixmap(pixmap.scaled(1280,720, aspectRatioMode= Qt.AspectRatioMode(1)))
            except Exception as e:
                print("Erreur lors du traitement de l'image :", e)
    
    def crypter_image(self):
        def binary(x):
            if x <= len(binary_text) - 1:
                return int(binary_text[x])
            else:
                return 0
        if self.image:
            #il faut récupérer le message
            popup = Popup(self)
            if popup.exec():
                texte_saisi = popup.text()
                if len(texte_saisi) == 0:
                    return
                (n, e), d = self.generer_cle()
                popupclee = PopupClees(self, [n, e, d])
                if not popupclee.exec():
                    print("yes")
                texte_chiffre = str(self.chiffrer(texte_saisi, (n, e))) + "§"
                binary_text = ''.join(format(ord(letter), '08b') for letter in texte_chiffre)
            matrice_pixels = self.image.load()
            for y in range(self.image.height):
                for x in range(self.image.width):
                    pixel = matrice_pixels[x, y]
                    #252: 11111100 on enlève les 2 bits les moins significatifs
                    matrice_pixels[x, y] = (pixel[0]&254, pixel[1]&254, pixel[2]&254)
            #il faut mettre le message dans ces bits
            ib = 1
            for y in range(self.image.height):
                for x in range(self.image.width):
                    pixel = matrice_pixels[x, y]
                    matrice_pixels[x, y] = (pixel[0] | binary(ib-1), pixel[1] | binary(ib), pixel[2] | binary(ib+1))
                    ib += 3

    def generer_cle(self):
        # générer deux nombres premiers aléatoires
        p = random.randint(100, 1000)
        while not self.est_premier(p):
            p = random.randint(100, 1000)
        q = random.randint(100, 1000)
        while not self.est_premier(q):
            q = random.randint(100, 1000)
        
        # calculer n et phi(n)
        n = p * q
        phi_n = (p - 1) * (q - 1)
        
        # trouver un entier e tel que 1 < e < phi(n) et e et phi(n) sont premiers entre eux
        e = random.randint(2, phi_n - 1)
        while not self.est_premier_entre_eux(e, phi_n):
            e = random.randint(2, phi_n - 1)
        
        # calculer d tel que d*e ≡ 1 (mod phi(n))
        d = self.trouver_d(e, phi_n)
        
        # retourner la clé publique (n, e) et la clé privée d
        return (n, e), d


    def est_premier(self, n):
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True


    def est_premier_entre_eux(self,a, b):
        while b != 0:
            a, b = b, a % b
        return a == 1


    def trouver_d(self, e, phi_n):
        d = 0
        for i in range(1, phi_n):
            if (i * e) % phi_n == 1:
                d = i
                break
        return d


    def chiffrer(self, message: str, cle_publique: tuple[int, int]):
        n, e = cle_publique
        # chiffrer chaque caractère en utilisant la clé publique
        chiffres = [pow(ord(c), e, n) for c in message]
        
        # retourner les chiffres chiffrés
        return chiffres


    def dechiffrer(self, chiffres: list[int], cle_privee: tuple[int, int]):
        n, d = cle_privee
        
        # déchiffrer chaque chiffre en utilisant la clé privée
        message = "".join([chr(pow(c, d, n)) for c in chiffres])
        
        # retourner le message déchiffré
        return message


    def decrypter(self):
        if not self.image:
            return
        def to_bin(n):
            c = bin(n)[2:]
            if len(c) % 8 != 0:
                for i in range(len(c) % 8):
                    c = '0' + c
            return c
        popupdemande = PopupDemande(self)
        if popupdemande.exec():
            pkey = popupdemande.text()
        matrice_pixels = self.image.load()
        binary_string = ''
        string = ""
        for y in range(self.image.height):
            for x in range(self.image.width): 
                pixel = matrice_pixels[x, y]
                for z in range(len(pixel)):
                    binary_string += to_bin(pixel[z])[-1]
                    if len(binary_string) == 8:
                        if binary_string != "00000000":
                            print(binary_string)
                        char = chr(int(binary_string, 2))
                        if 0 != ord(char):
                            print(char)
                        if char == '§':
                            chiffres = [ord(c) for c in string]
                            string = self.dechiffrer(chiffres, (int(pkey[0]), int(pkey[1])))
                            print(string)
                            popupaffiche = PopupAffiche(string, self)
                            if popupaffiche.exec():
                                print("yes")
                            return string
                        string += char
                        binary_string = ''

    def afficher_image(self):
        if self.image:
            matrice_pixels = self.image.load()
            for y in range(self.image.height):
                for x in range(self.image.width):
                    pixel = matrice_pixels[x, y]
                    print(pixel, end=" ")
            print("---------------------------------------------------------")

class PopupClees(QDialog):
    def __init__(self, parent=None, keys = [0, 0, 0]): #n, e, d
        super().__init__(parent)
        self.setWindowTitle("Clées RSA")
        self.keys = keys

        self.button_ok = QPushButton("OK", self)
        self.button_ok.clicked.connect(self.accept)

        # Création des labels pour les variables
        label1 = QLabel(f"Clée publique : ("+ str(self.keys[0])+ ","+  str(self.keys[1])+ ")", self)
        label2 = QLabel(f"Clée privée : ("+ str(self.keys[0])+ ","+  str(self.keys[2])+ ")", self)

        # Ajout des labels à la fenêtre pop-up
        layout = QVBoxLayout(self)
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(self.button_ok)

class PopupDemande(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Rentrer clée privée")

        # Création du champ de texte et du bouton "OK"
        self.text_edit = QLineEdit(self) #d
        self.text_edit2 = QLineEdit(self) #e
        self.button_ok = QPushButton("OK", self)
        self.button_ok.clicked.connect(self.accept)

        # Ajout des widgets à la fenêtre pop-up
        layout = QVBoxLayout(self)
        layout.addWidget(self.text_edit)
        layout.addWidget(self.text_edit2)
        layout.addWidget(self.button_ok)

    def text(self):
        # Renvoie le texte saisi dans le champ de texte
        return (self.text_edit.text(), self.text_edit2.text())

class PopupAffiche(QDialog):
    def __init__(self, message, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Texte déchiffré")

        self.button_ok = QPushButton("OK", self)
        self.button_ok.clicked.connect(self.accept)

        # Création des labels pour les variables
        label = QLabel(f"Texte déchiffré: {message}", self)

        # Ajout des labels à la fenêtre pop-up
        layout = QVBoxLayout(self)
        layout.addWidget(label)
        layout.addWidget(self.button_ok)

class Popup(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Entrer un texte")

        # Création du champ de texte et du bouton "OK"
        self.text_edit = QLineEdit(self)
        self.button_ok = QPushButton("OK", self)
        self.button_ok.clicked.connect(self.accept)

        # Ajout des widgets à la fenêtre pop-up
        layout = QVBoxLayout(self)
        layout.addWidget(self.text_edit)
        layout.addWidget(self.button_ok)

    def text(self):
        # Renvoie le texte saisi dans le champ de texte
        return self.text_edit.text()

if __name__ == "__main__":
    # Initialisation de l'application PyQt
    app = QApplication([])

    # Création de la fenêtre principale
    window = MainWindow()
    window.show()

    # Exécution de l'application PyQt
    app.exec()