# Importation de la bibliothèque Python pour lire des fichiers BMP
from PIL import Image

# Chemin vers le fichier BMP à lire
chemin_fichier = r"samples\sample_640×426.bmp"

# Ouverture du fichier BMP
image = Image.open(chemin_fichier)

# Chargement de la matrice de pixels
matrice_pixels = image.load()

# Affichage des informations sur l'image
print("Type de l'image :", image.format)
print("Mode de l'image :", image.mode)
print("Dimensions de l'image :", image.size)

# Affichage de la matrice de pixels
'''
for y in range(image.height):
    for x in range(image.width):
        pixel = matrice_pixels[x, y]
        print(pixel, end=" ")
    print()
'''

# Affichage de l'image
image.show()
