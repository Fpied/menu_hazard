import os

with open("Dessert/far_breton.txt", "r") as g and open("Dessert/Gateau_au_yaourt.py", "r") as f:
    content = f.read() + g.read()
    print(content)