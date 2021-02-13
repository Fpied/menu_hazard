import os
from glob import glob
import shutil
import random

# chemin de mes entrée
chemin_entree = r"C:\Users\piedf\OneDrive\Bureau\developpement_web\python\Liste_de_courses\Menu\entree"

fichiers = glob(os.path.join(chemin_entree, "*"))
choix_entree = random.choice(fichiers)

# Lire le fichier choisi
with open(choix_entree, "r", encoding="utf-8") as f:
    contenu_entree = f.read()
    print(contenu_entree)