# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define s = Character("Son", callback = name_callback, cb_name = "son")
define l = Character("Lise", callback = name_callback, cb_name = "lise")
define v = Character("Amiral Vuong", callback = name_callback, cb_name = "vuong")
define p = Character("Capitaine Phong", callback = name_callback, cb_name = "phong")
define pnj = Character("Mec random", callback = name_callback, cb_name = "pnj")

define ai = Character(callback = name_callback, cb_name = "ai")
image ai = At('ai frame', sprite_highlight('ai'))

define n = Character(callback = name_callback, cb_name = None)
define config.debug_sound = True 

define flash = Fade(0.1, 0.0, 0.5, color="#fff")

image son = At('son main frame', sprite_highlight('son'))
image lise = At('lise main frame', sprite_highlight('lise'))
image pnj = At('pnj main frame', sprite_highlight('pnj'))

image bg ai face = Transform("images/background/bg ai face.jpg", size=(1920, 1080), fit="fill")
image bg main = Transform("images/background/bg retrofuture.jpg", size=(1920, 1080), fit="fill")

define COOL_VALUE = 50
define SPORTIF_VALUE = 50
define FORCEUR_VALUE = 50
define MYTHO_VALUE = 50
define SQUATTEUR_VALUE = 50

define extension = False
define first_show_stats = True
define scenar_choisi = ""
define son_still_training = True

define plot_labels = [
        Text('Cool'), 
        Text('Sportif'), 
        Text('Forceur'), 
        Text('Mytho'), 
        Text('Squatteur')
    ]

define label_chart = RadarChart(
        size=500,
        values=[
                COOL_VALUE,
                SPORTIF_VALUE,
                FORCEUR_VALUE,
                MYTHO_VALUE,
                SQUATTEUR_VALUE
            ],
        max_value=100,
        data_colour=(213, 71, 130, 255),
        line_colour=(0, 0, 0, 255),
        background_colour=(20, 21, 17, 170),
        labels = plot_labels
    )


# The game starts here.
label start:
    play music "ai-beeping-sound.mp3"
    scene bg main

    show ai:
        xalign 0.5
        yalign 0.4

    ai "Bienvenue dans Companion Creator 1.0."
    ai "Commençons la création de votre compagnon virtuel."
    ai "Sur quelle base de compagnon voulez-vous partir ?"
    stop music

    hide ai
    
    call model_choice 

    jump companion_stats

    # Le menu principal pour charger des scénarios
    label home: 
        stop music
        scene bg main

        menu:
            ai "Choisissez un scénario d'entraînement."
            "Scénario: Le Cuisinier":
                $ scenar_choisi = "Le Cuisinier"
                jump le_cuistot
            "Scénario: Le Compétiteur":
                $ scenar_choisi = "Le Compétiteur"
                jump vvd
            "Scénario: Le Squatteur":
                $ scenar_choisi = "Le Squatteur"
                jump lune_de_miel
            "C'est bon j'ai ce qu'il me faut":
                $ son_still_training = False 
                jump companion_stats

    label companion_stats:
        python:
            plot_values = [
                COOL_VALUE,
                SPORTIF_VALUE,
                FORCEUR_VALUE,
                MYTHO_VALUE,
                SQUATTEUR_VALUE
            ]
            label_chart.values = plot_values

        play music "ai-beeping-sound.mp3"
        scene bg main
        with dissolve

        show image label_chart:
            xalign 0.7
            yalign 0.4

        show ai:
            xalign 0.2
            yalign 0.4

        if first_show_stats: 
            ai "Voici la base du compagnon virtuel que l'on va créer."
            ai "Passons à l'entraînement du modèle."
            $ first_show_stats = False
            jump home 
        else:
            if son_still_training:
                ai "Merci d'avoir terminé le scénario \"[scenar_choisi]\". Regardons l'avancement de notre modèle..."
            else: 
                ai "Voici l'état actuel du compagnon virtuel"
            menu: 
                ai "Est-ce que le compagnon créé vous convient ?"
                "Oui, je suis pleinement satisfait":
                    show screen text_je_ne_crois_pas 
                    pause
                    hide screen text_je_ne_crois_pas 
                    jump companion_stats
                "Non, je souhaite continuer à entraîner le modèle":
                    $ son_still_training = True 
                    jump home
                "Non, je souhaite acheter une extension (promo)":
                    jump extension


    label extension:
        stop music
        scene bg main

        
        show ai:
            xalign 0.5
            yalign 0.4

        ai "Quelle extension souhaitez vous installer ?"

        $ extension = True

        hide ai
        call model_choice

        show ai:
            xalign 0.5
            yalign 0.4

        "Très bon choix! Vous avez sélectionné le modèle Lily."
        menu:
            "Entraînons le modèle Lily."
            "scénario 1":
                jump conclusion
            "scénario 2":
                jump conclusion
            "Le modèle Lily est prêt":
                jump model_fusion

    
    label model_fusion:
        scene bg main
        show ai:
            xalign 0.5
            yalign 0.4
        with dissolve
        ai "Merci d'avoir compléter le scénario \"[scenar_choisi]\"! Continuons l'entraînement."
        hide ai
        jump menu_fusion

    label menu_fusion:
        menu: 
            ai "Entraînons nos deux modèles en simultané."
            "Scénario: Les Forceurs":
                $ scenar_choisi = "Les Forceurs"
                jump west_coast
            "Scénario: Maniaques":
                $ scenar_choisi = "Les Maniaques"
                jump tasses
            "C'est bon, les modèles sont prêts":
                jump mix_models_stats 


    label conclusion:
        "Merci d'avoir utilisé notre logiciel "
        scene family
        pause
        pause
        pause
        pause


    return

screen text_je_ne_crois_pas:
    frame: 
        # background white 
        xpadding 40
        ypadding 20
        xalign 0.5
        yalign 0.5
        text "Je ne crois pas..."


