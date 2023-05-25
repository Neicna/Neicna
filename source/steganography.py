from popups import *
from encryption import *

def get_text(self):
    if self.image:
        #il faut récupérer le message
        popup = Popup(self)
        popup.exec()
        return popup.text()

def rsa(self, text:str) -> list[int]:
    n, e, d = generer_cle()
    popupclee = PopupClees(self, [n, e, d])
    popupclee.exec()
    return chiffrer(text, (n, e)) + [ord("§")]

def crypter_image(self):
    texte_saisi = self.get_text()
    if texte_saisi == "":
        return
    text_unicode = self.rsa(texte_saisi)
    binary_text = ''.join(format(n, '08b') for n in text_unicode)
    matrice_pixels = self.image.load()
    ib = 1
    for y in range(self.image.height):
        for x in range(self.image.width):
            #il faut mettre le message dans ces bits
            pixel = matrice_pixels[x, y]
            matrice_pixels[x, y] = (pixel[0] | int(binary_text[ib-1]), pixel[1] | int(binary_text[ib]), pixel[2] | int(binary_text[ib+1]))
            ib += 3

def get_keys(self) -> tuple[int, int]:
    if not self.image:
        return
    popupdemande = PopupDemande(self)
    popupdemande.exec()
    t = popupdemande.text()
    return (int(t[0]), int(t[1]))

def decrypter(self):
    pkey = self.get_keys()
    matrice_pixels = self.image.load()
    binary_string = ''
    chiffres = []
    for x in range(self.image.height):
        for y in range(self.image.width): 
            pixel = matrice_pixels[x, y]
            for bit in range(len(pixel)):
                binary_string += pixel[bit][-1]
                if len(binary_string) == 8:
                    char = int(binary_string, 2)
                    if char == ord('§'):
                        resultat = dechiffrer(chiffres, pkey)
                        print(resultat)
                        popupaffiche = PopupAffiche(resultat, self)
                        popupaffiche.exec()
                        return resultat
                    chiffres.append(char)
                    binary_string = ''