define oversample_tasse = 4
define tasse_h_g = Image("tasse_haut_gauche.jpg", oversample=oversample_tasse)
define tasse_h_d = Image("tasse_haut_droite.jpg", oversample=oversample_tasse)
define tasse_b_d = Image("tasse_bas_droite.jpg", oversample=oversample_tasse)
define tasse_b_g = Image("tasse_bas_gauche.jpg", oversample=oversample_tasse)
image blily = Image("lise main frame.png", oversample=1)
image bson = Image("son main frame.png", oversample=1)


label tasses:
    stop sound
    stop music
    scene bg salon massy
    show blily:
        xalign 0.1
        yalign 0.4
    show bson:
        xalign 0.9
        yalign 0.4
    "Bienvenue chez nous!"
    "Le rangement c'est important dans la vie!"
    "Comment faut-il ranger les tasses starbucks chez nous???"

    hide blily
    hide bson

    show image tasse_h_d zorder 0:
        xalign 0.2
        yalign 0.8

    show image tasse_h_g:
        xalign 0.4
        yalign 0.8

    show image tasse_b_g:
        xalign 0.6
        yalign 0.8

    show image tasse_b_d:
        xalign 0.8
        yalign 0.8


    menu: 
        "A l'endroit, manche sur la droite":
            jump model_fusion
        "A l'endroit, manche sur la gauche":
            jump model_fusion
        "A l'envers, manche sur la gauche":
            jump model_fusion
        "A l'envers, manche sur la droite":
            jump model_fusion
        "On s'en fout c'est des tasses": 
            jump model_fusion

# Ajouter des images en bas

