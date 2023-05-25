# Importation des bibliothèques pour l'interface graphique
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtCore import Qt

from steganography import *
from masks import *
from utils import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Définition de la fenêtre principale
        self.setWindowTitle("PyPicture")
        self.setGeometry(100, 100, 800, 600)
        self.setWindowIcon(QIcon(r"templates\icon.webp"))

        # Création du label pour l'affichage de l'image
        self.image_label = QLabel(self)
        margin = 100
        self.image_label.setMaximumSize(1280+margin, 720+margin)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_label.setMargin(margin)

        # Initialisation de l'image
        self.image = None

        # Définition des actions de la barre de menu
        ouvrir_action = QAction("Ouvrir", self)
        ouvrir_action.setShortcut("Ctrl+O")
        ouvrir_action.triggered.connect(lambda: ouvrir_image(self))

        nouveau_action = QAction("Nouveau", self)
        nouveau_action.setShortcut("Ctrl+N")
        nouveau_action.triggered.connect(lambda: nouveau_image(self))

        enregistrer_action = QAction("Enregistrer", self)
        enregistrer_action.setShortcut("Ctrl+S")
        enregistrer_action.triggered.connect(lambda: enregistrer_image(self))

        negatif_action = QAction("Négatif", self)
        negatif_action.triggered.connect(lambda: inverser_image(self.image, self.image_label))

        noir_et_blanc_action = QAction("Noir et Blanc", self)
        noir_et_blanc_action.triggered.connect(lambda: noir_et_blanc_image(self.image, self.image_label))

        sepia_action = QAction("Sépia", self)
        sepia_action.triggered.connect(lambda: sepia_image(self.image))

        gris_action = QAction("Niveaux gris", self)
        gris_action.triggered.connect(gris_image)

        rsa_action = QAction("Chiffrement RSA", self)
        rsa_action.triggered.connect(lambda: crypter_image(self))

        cesar_action = QAction("Code César", self)
        cesar_action.triggered.connect(lambda: crypter_image(self))

        cesarPlus_action = QAction("Code César +", self)
        cesarPlus_action.triggered.connect(lambda: crypter_image(self))

        dersa_action = QAction("Déchiffrer RSA", self)
        dersa_action.triggered.connect(lambda: decrypter(self))

        decesar_action = QAction("Déchiffrer César", self)
        decesar_action.triggered.connect(lambda: decrypter(self))

        decesarPlus_action = QAction("Déchiffrer César +", self)
        decesarPlus_action.triggered.connect(lambda: decrypter(self))

        afficher_action = QAction("Afficher", self)
        afficher_action.triggered.connect(lambda: afficher_image(self))

        # Création de la barre de menu
        menu_bar = self.menuBar()
        
        #création du menu "ficher"
        fichier_menu = menu_bar.addMenu("Fichier")
        fichier_menu.addAction(nouveau_action)
        fichier_menu.addAction(ouvrir_action)
        fichier_menu.addAction(enregistrer_action)
        
        #création du menu "dessin"
        dessin_menu = menu_bar.addMenu("Dessin")

        #création du menu "traitement"
        traitement_menu = menu_bar.addMenu("Traitement")
        traitement_menu.addAction(negatif_action)
        traitement_menu.addAction(gris_action)
        traitement_menu.addAction(noir_et_blanc_action)
        traitement_menu.addAction(sepia_action)
       
        #création du menu "message" avec les sous-menus "crypter" et "décrypter"
        message_menu = menu_bar.addMenu("Message")
        crypter_menu = message_menu.addMenu("Crypter")
        crypter_menu.addAction(rsa_action)
        crypter_menu.addAction(cesar_action)
        crypter_menu.addAction(cesarPlus_action)
        decrypter_menu = message_menu.addMenu("Decrypter")
        decrypter_menu.addAction(dersa_action)
        decrypter_menu.addAction(decesar_action)
        decrypter_menu.addAction(decesarPlus_action)

        #création du menu "débuggage"
        debuggage_menu = menu_bar.addMenu("Débuggage")
        debuggage_menu.addAction(afficher_action)

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

if __name__ == "__main__":
    # Initialisation de l'application PyQt
    app = QApplication([])

    # Création de la fenêtre principale
    window = MainWindow()
    window.show()

    # Exécution de l'application PyQt
    app.exec()