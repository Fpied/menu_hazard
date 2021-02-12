import os
import random

entree = ["Salade_de_thon_banane_avocat", "salade_riz_thon_et_haricots", "soupe_de_legumes", "sushis_de_concombre", "Les_bouchées_au_thon"]
plat = ["Bavette_Brocolis.txt", "Blancs_de_dinde_a_la_moutarde_a_l_ancienne", "Omelette_aux_pommes_de_terre", "Saute_de_dinde_a_la_moutarde_et_estragon", "Bulgogi", "Le_navarin_d_agneau"]
dessert = ["Far_breton", "Gateau_au_yaourt", "salade_de_fruits", "Meringue", "Le_choco_fondant"]



boucle = True

while boucle == True:
    first_question = input("Voulez-vous préparer à manger ? O/N ")
    if first_question == "O" or first_question == "o":
        choix_entree = random.choice(entree)
        choix_plat = random.choice(plat)
        choix_dessert = random.choice(dessert)
        print("Nous vous proposons ce choix la :")
        print(choix_entree)
        print(choix_plat)
        print(choix_dessert)
        Voir_recette = input("Voulez-vous voir les recettes ? O/N ")
        if Voir_recette == "O" or Voir_recette == "o":
            # Recette entree
            if choix_entree:
                chemin_entree = "C:\\Users\\piedf\\OneDrive\\Bureau\\developpement_web\\python\\Liste_de_courses\\Menu\\entree\\"
                # print("Salade de thon banane avocat")
                lol_entree = chemin_entree + choix_entree + ".txt"
                with open(lol_entree, "r", encoding="utf-8") as f:
                    contenu_entree = f.read()
                    print(contenu_entree)
            # Recette plat principale
            if choix_plat:
                chemin_plat = "C:\\Users\\piedf\\OneDrive\\Bureau\\developpement_web\\python\\Liste_de_courses\\Menu\\Main\\"
                # print("Bavette Brocolis")
                lol_plat = chemin_plat + choix_plat + ".txt"
                with open(lol_plat, "r", encoding="utf-8") as f:
                    contenu_plat = f.read()
                    print(contenu_plat)
            # recette dessert
            if choix_dessert:
                chemin_dessert = "C:\\Users\\piedf\\OneDrive\\Bureau\\developpement_web\\python\\Liste_de_courses\\Menu\\Dessert\\"
                # print("Far Breton")
                lol_dessert = chemin_dessert + choix_dessert + ".txt"
                with open(lol_dessert, "r", encoding="utf-8") as f:
                    contenu_dessert = f.read()
                    print(contenu_dessert)
        else:
            print("sortir de la boucle")
            boucle = False
            

    else:
        print("sortir de la boucle")
        boucle = False
    














