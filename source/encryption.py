import random
import math

def generer_cle():
    # générer deux nombres premiers aléatoires
    p = random.randint(100, 1000)
    while not est_premier(p):
        p = random.randint(100, 1000)
    q = random.randint(100, 1000)
    while not est_premier(q):
        q = random.randint(100, 1000)
    # calculer n et phi(n)
    n = p * q
    phi_n = (p - 1) * (q - 1)
    # trouver un entier e tel que 1 < e < phi(n) et e et phi(n) sont premiers entre eux
    e = random.randint(2, phi_n - 1)
    while not est_premier_entre_eux(e, phi_n):
        e = random.randint(2, phi_n - 1)
    # calculer d tel que d*e ≡ 1 (mod phi(n))
    d = trouver_d(e, phi_n)
    # retourner la clé publique (n, e) et la clé privée d
    return n, e, d

def est_premier(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def est_premier_entre_eux(a, b):
    while b != 0:
        a, b = b, a % b
    return a == 1

def trouver_d(e, phi_n):
    d = 0
    for i in range(1, phi_n):
        if (i * e) % phi_n == 1:
            d = i
            break
    return d

def chiffrer(message: str, cle_publique: tuple[int, int]) -> list:
    n, e = cle_publique
    # chiffrer chaque caractère en utilisant la clé publique
    chiffres = [pow(ord(c), e, n) for c in message]
    # retourner les chiffres chiffrés
    return chiffres

def dechiffrer(chiffres: list[int], cle_privee: tuple[int, int]):
    n, d = cle_privee
    # déchiffrer chaque chiffre en utilisant la clé privée
    message = "".join([chr(pow(c, d, n)) for c in chiffres])
    # retourner le message déchiffré
    return message