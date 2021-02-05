import os
import random

entree = ["Salade de thon banane avocat", "salade de riz thon et haricots", "soupe de legumes"]
plat = ["Bavette Brocolis", "Blancs de dinde a la moutarde a l'ancienne", "Omelette aux pommes de terre"]
dessert = ["Far breton", "Gateau au yaourt", "salade de fruits"]

boucle = True

while boucle == True:
    first_question = input("Voulez-vous préparer à manger ? O/N ")
    if first_question == "O":
        choix_entree = random.choice(entree)
        choix_plat = random.choice(plat)
        choix_dessert = random.choice(dessert)
        print("Nous vous proposons ce choix la :")
        print(choix_entree)
        print(choix_plat)
        print(choix_dessert)
        Voir_recette = input("Voulez-vous voir les recettes ? O/N ")
        if Voir_recette == "O":
            if choix_entree == "Salade de thon banane avocat":
                chemin_salade_de_thon_banane_avocat = r"C:\Users\piedf\OneDrive\Bureau\developpement_web\python\Liste_de_courses\Menu\entree\salade_de_thon_banane_avocat.txt"
                print("Salade de thon banane avocat")
                with open(chemin_salade_de_thon_banane_avocat, "r", encoding="utf-8") as f:
                    contenu_salade_de_thon_banane_avocat = f.read()
                    print(contenu_salade_de_thon_banane_avocat)
            
            if choix_entree == "salade de riz thon et haricots":
                chemin_salade_de_riz_thon_et_haricots = r"C:\Users\piedf\OneDrive\Bureau\developpement_web\python\Liste_de_courses\Menu\entree\Salade_riz_thon_et_haricots.py"
                print("Salade de riz thon et haricots")
                with open(chemin_salade_de_riz_thon_et_haricots, "r", encoding="utf-8") as f:
                    contenu_salade_de_riz_thon_et_haricots = f.read()
                    print(contenu_salade_de_riz_thon_et_haricots)
            
            if choix_entree == "soupe de legumes":
                chemin_soupe_de_legume = r"C:\Users\piedf\OneDrive\Bureau\developpement_web\python\Liste_de_courses\Menu\entree\soupe_de_legumes.py"
                print("Soupe de legumes")
                with open(chemin_soupe_de_legume, "r", encoding="utf-8") as f:
                    contenu_soupe_de_legume = f.read()
                    print(contenu_soupe_de_legume)

            if choix_plat == "Bavette Brocolis":
                chemin_Bavette_Brocolis = r"C:\Users\piedf\OneDrive\Bureau\developpement_web\python\Liste_de_courses\Menu\Main\Bavette_Brocolis.txt"
                print("Bavette Brocolis")
                with open(chemin_Bavette_Brocolis, "r", encoding="utf-8") as f:
                    contenu_Bavette_Brocolis = f.read()
                    print(contenu_Bavette_Brocolis)
                
            if choix_plat == "Blancs de dinde a la moutarde a l'ancienne":
                chemin_Blancs_de_dinde_a_la_moutarde_a_l_ancienne = r"C:\Users\piedf\OneDrive\Bureau\developpement_web\python\Liste_de_courses\Menu\Main\Blancs_de_dinde_a_la_moutarde_a_l_ancienne.py"
                print("Blancs de dinde a la moutarde a l'ancienne")
                with open(chemin_Blancs_de_dinde_a_la_moutarde_a_l_ancienne, "r", encoding="utf-8") as f:
                    contenu_Blancs_de_dinde_a_la_moutarde_a_l_ancienne = f.read()
                    print(contenu_Blancs_de_dinde_a_la_moutarde_a_l_ancienne)
            
            if choix_plat == "Omelette aux pommes de terre":
                chemin_Omelette_aux_pommes_de_terre = r"C:\Users\piedf\OneDrive\Bureau\developpement_web\python\Liste_de_courses\Menu\Main\Omelette_aux_pommes_de_terre.py"
                print("Omelette aux pommes de terre")
                with open(chemin_Omelette_aux_pommes_de_terre, "r", encoding="utf-8") as f:
                    contenu_Omelette_aux_pommes_de_terre = f.read()
                    print(contenu_Omelette_aux_pommes_de_terre)
            
            if choix_dessert == "Far breton":
                chemin_Far_breton = r"C:\Users\piedf\OneDrive\Bureau\developpement_web\python\Liste_de_courses\Menu\Dessert\far_breton.txt"
                print("Far Breton")
                with open(chemin_Far_breton, "r", encoding="utf-8") as f:
                    contenu_Far_breton = f.read()
                    print(contenu_Far_breton)
            
            if choix_dessert == "Gateau au yaourt":
                chemin_Gateau_au_yaourt = r"C:\Users\piedf\OneDrive\Bureau\developpement_web\python\Liste_de_courses\Menu\Dessert\Gateau_au_yaourt.py"
                print("Gateau au yaourt")
                with open(chemin_Gateau_au_yaourt, "r", encoding="utf-8") as f:
                    contenu_Gateau_au_yaourt = f.read()
                    print(contenu_Gateau_au_yaourt)
            
            if choix_dessert == "salade de fruits":
                chemin_salade_de_fruits = r"C:\Users\piedf\OneDrive\Bureau\developpement_web\python\Liste_de_courses\Menu\Dessert\salade_de_fruits.py"
                print("Salade de fruits")
                with open(chemin_salade_de_fruits, "r", encoding="utf-8") as f:
                    contenu_salade_de_fruits = f.read()
                    print(contenu_salade_de_fruits)
            
        else:
            print("sortir de la boucle")
            boucle = False
            

    else:
        print("sortir de la boucle")
        boucle = False
    














