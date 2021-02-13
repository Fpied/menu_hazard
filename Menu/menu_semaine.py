import os
import random
from glob import glob
import shutil

# import des chemins des dossier:
chemin_entree = r"C:\Users\piedf\OneDrive\Bureau\developpement_web\python\Liste_de_courses\Menu\entree"
chemin_plat = r"C:\Users\piedf\OneDrive\Bureau\developpement_web\python\Liste_de_courses\Menu\Main"
chemin_dessert = r"C:\Users\piedf\OneDrive\Bureau\developpement_web\python\Liste_de_courses\Menu\Dessert"

boucle = True

while boucle == True:
    first_question = input("Voulez-vous préparer à manger ? O/N ")
    if first_question == "O" or first_question == "o":
        # choix de l'entree:
        fichiers = glob(os.path.join(chemin_entree, "*"))
        choix_entree = random.choice(fichiers)
        nom_entree = os.path.basename(choix_entree)
        print(nom_entree)
       
        # choix du plat principale:
        fichiers_plat = glob(os.path.join(chemin_plat, "*"))
        choix_plat = random.choice(fichiers_plat)
        nom_plat = os.path.basename(choix_plat)
        print(nom_plat)
        
        # choix du dessert:
        fichiers_dessert = glob(os.path.join(chemin_dessert, "*"))
        choix_dessert = random.choice(fichiers_dessert)
        nom_dessert = os.path.basename(choix_dessert)
        print(nom_dessert)
        
        second_question = input("Voulez vous voir les recettes ? O/N ")
        if second_question == "O" or second_question == "o":
            # affichage de la recette entrée
            with open(choix_entree, "r", encoding="utf-8") as f:
                contenu_entree = f.read()
                print(contenu_entree)
            # affichage du plat principale
            with open(choix_plat, "r", encoding="utf-8") as f:
                contenu_plat = f.read()
                print(contenu_plat)
            #  affichage du dessert
            with open(choix_dessert, "r", encoding="utf-8") as f:
                contenu_dessert = f.read()
                print(contenu_dessert)
        else:
            boucle = False
            print("sorti de la boucle")
    else:
        boucle = False
        print("sorti de la boucle")



        
        
           
    














