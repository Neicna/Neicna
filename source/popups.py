# Importation des bibliothèques pour l'interface graphique
from PyQt6.QtWidgets import QLabel, QPushButton, QVBoxLayout,QDialog, QLineEdit

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