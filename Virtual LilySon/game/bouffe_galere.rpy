label bouffe_galere:
    scene bg salon massy
    show image "lise main frame":
        xalign 0.5
        yalign 0.4
    l "Hmmmm j'ai bien faim..."
    l "Qu'est ce que j'ai à la maison qui est bien galère à manger?"
    l "J'aime tellement la nourriture difficile à manger!"
    l "Plus c'est chiant à manger plus je trouve ça bon 🥰"
    menu: 
        "Quel va être mon dîner d'aujourd'hui?"
        "3kg noix pour retirer la coque mais aussi retirer la peau": 
            jump model_lily
        "1 crabe entier pour avoir 1g de chair pour 10 minutes de travail":
            jump model_lily
        "2kg amandes fraîches pour le plaisir d'enlever 3 couches":
            jump model_lily
        "1 filet de poisson avec beaucoup d'arêtes s'il vous plaît!":
            jump model_lily
        
