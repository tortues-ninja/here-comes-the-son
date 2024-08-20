# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define s = Character("Son", callback = name_callback, cb_name = "son")
define l = Character("Lise", callback = name_callback, cb_name = "lise")
define v = Character("Amiral Vuong", callback = name_callback, cb_name = "vuong")
define p = Character("Capitaine Phong", callback = name_callback, cb_name = "phong")
define pnj = Character("Mec random", callback = name_callback, cb_name = "pnj")

define n = Character(callback = name_callback, cb_name = None)
define config.debug_sound = True 

define flash = Fade(0.1, 0.0, 0.5, color="#fff")

image son = At('son main frame', sprite_highlight('son'))
image lise = At('lise main frame', sprite_highlight('lise'))
image pnj = At('pnj main frame', sprite_highlight('pnj'))

image bg ai face = Transform("images/background/bg ai face.jpg", size=(1920, 1080), fit="fill")


# The game starts here.

label start:

    python:      
        mytho_value = 10
        forceur_value = 40
        squatteur_value = 50
        sportif_value = 90
        joueur_value = 80
        
        plot_values = [
            mytho_value,
            forceur_value,
            squatteur_value,
            sportif_value,
            joueur_value
        ]

        plot_labels = [
            Text('Mytho'), 
            Text('Forceur'), 
            Text('Squatteur'), 
            Text('Sportif'), 
            Text('Joueur')
        ]

    play music "ai-beeping-sound.mp3"
    scene bg ai face

    "Bienvenue dans Companion Creator 1.0"
    "Commençons la création de votre compagnon virtuel"
    "Sur quelle base de compagnon voulez-vous partir ?"
    stop music

    menu:
        "Modèle S":
            jump home
        "Modèle L":
            jump model_validation

    label model_validation:
        scene bg ai face
        "Vous êtes sûrs ?"

        menu: 
            "Non, laisse moi recommencer...":
                jump start

    # Le menu principal pour charger des scénarios
    label home: 
        stop music
        scene bg ai face

        "Choisissez une caractéristique pour votre compagnon"

        menu:
            "Cuisinier":
                jump le_cuistot
            "Compétiteur":
                jump vvd
            "Le squatteur":
                jump lune_de_miel
            "C'est bon j'ai ce qu'il me faut":
                jump companion_validation

    label companion_validation:

        python:
            label_chart = RadarChart(
                size=500,
                values=plot_values,
                max_value=100,
                data_colour=(213, 71, 130, 255),
                line_colour=(0, 0, 0, 255),
                background_colour=(20, 21, 17, 170),
                labels = plot_labels
            )

        play music "ai-beeping-sound.mp3"
        scene bg ai face
        show image label_chart:
            xalign 0.5
            yalign 0.5
        "Est-ce que le compagnon créé vous convient ?"

        menu: 
            "Oui":
                jump companion_revalidation
            "Non, il manque quelque chose...":
                jump model_l

    label companion_revalidation:
        scene bg ai face
        "Vous êtes sûrs ?"

        menu: 
            "Non, en effet il manque quelque chose...":
                jump model_l

    label model_l:
        stop music
        scene bg ai face
        "Je peux vous proposer de fusionner votre compagnon avec le dernier modèle en date, le \"modèle S\""
    
    label model_fusion:
        scene bg ai face
        "Il me faut quelques caractéristiques communes supplémentaires"

        menu: 
            "Forceurs":
                jump west_coast
            "C'est bon j'ai ce qu'il me faut":
                jump fuse_faces 
    return
