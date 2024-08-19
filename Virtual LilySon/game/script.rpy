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


image son = At('son main frame', sprite_highlight('son'))
image pnj = At('pnj main frame', sprite_highlight('pnj'))

image bg ai face = Transform("images/background/bg ai face.jpg", size=(1920, 1080), fit="fill")


# The game starts here.

label start:

    play music "ai-beeping-sound.mp3"
    scene bg ai face

    "Bienvenue dans Companion Creator 1.0"
    "Commençons la création de votre compagnon virtuel"
    "Sur quelle base de compagnon voulez-vous partir ?"

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
        play music "ai-beeping-sound.mp3"
        scene bg ai face
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
        scene bg ai face
        "Je peux vous proposer de fusionner votre compagnon avec le dernier modèle en date, le \"modèle S\""

        menu: 
            "Oui":
                jump companion_revalidation
            "Non, il manque quelque chose...":
                jump model_l


    # This ends the game.
    return
