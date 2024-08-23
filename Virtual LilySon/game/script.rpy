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

define ai_son = Character(callback = name_callback, cb_name = "ai_son")
# image ai_son = At(IMAGES_SON[COUNT_SCENARIO_SON], sprite_highlight('ai'))


define n = Character(callback = name_callback, cb_name = None)
define config.debug_sound = True 

define flash = Fade(0.1, 0.0, 0.5, color="#fff")

image son = At('son main frame', sprite_highlight('son'))
image lise = At('lise main frame', sprite_highlight('lise'))
image pnj = At('bruno mars', sprite_highlight('pnj'))

image bg ai face = Transform("images/background/bg ai face.jpg", size=(1920, 1080), fit="fill")
image bg main = Transform("images/background/bg retrofuture.jpg", size=(1920, 1080), fit="fill")

# Stats Son
define S_COOL_VALUE = 50
define S_SPORTIF_VALUE = 50
define S_FORCEUR_VALUE = 50
define S_MYTHO_VALUE = 50
define S_SQUATTEUR_VALUE = 50
define IMAGES_SON = ["ai frame.png", "ai-son-1.png", "ai-son-2.png", "ai-son-3.png"]
define COUNT_SCENARIO_SON = 0

image ai_son = ConditionSwitch(
    "COUNT_SCENARIO_SON == 0", "ai frame.png",
    "COUNT_SCENARIO_SON == 1", "ai-son-1.png",
    "COUNT_SCENARIO_SON == 2", "ai-son-2.png",
    "COUNT_SCENARIO_SON >= 3", "ai-son-3.png")


# Stats Lily
define L_COOL_VALUE = 50
define L_SPORTIF_VALUE = 50
define L_FORCEUR_VALUE = 50
define L_MYTHO_VALUE = 50
define L_SQUATTEUR_VALUE = 50

define extension = False
define first_show_stats = True
define first_model_fusion = True
define first_model_lily = True
define scenar_choisi = ""
define son_still_training = True

define plot_labels = [
    Text('Cool'), 
    Text('Sportif'), 
    Text('Mytho'), 
    Text('Forceur'), 
    Text('Squatteur')
]

define label_chart = RadarChart(
    size=500,
    values=[
            S_COOL_VALUE,
            S_SPORTIF_VALUE,
            S_MYTHO_VALUE,
            S_FORCEUR_VALUE,
            S_SQUATTEUR_VALUE
        ],
    max_value=100,
    data_colour=(213, 71, 130, 255),
    line_colour=(0, 0, 0, 255),
    background_colour=(20, 21, 17, 170),
    labels = plot_labels
)


# The game starts here.
label start:
    play music "<from 0 to 3>ai-beeping-sound.mp3" noloop
    scene bg main

    show ai:
        xalign 0.5
        yalign 0.4
        
    pause 3.0

    play sound "01.mp3"
    ai "Bienvenue dans Companion Creator 1.0."


    stop sound
    play sound "02.mp3"
    ai "Commençons la création de votre compagnon virtuel."
    stop sound
    play sound "03.mp3"
    ai "Sur quelle base de compagnon voulez-vous partir ?"

    stop music

    hide ai
    
    call model_choice from _call_model_choice 

    jump companion_stats

    # Le menu principal pour charger des scénarios
    label home: 

        stop music
        scene bg main

        stop sound
        play sound "04.mp3"

        menu:
            ai_son "Choisissez un scénario d'entraînement."
            "Scénario: Le Cuisinier":
                $ scenar_choisi = "Le Cuisinier"
                $ COUNT_SCENARIO_SON += 1
                jump le_cuistot
            "Scénario: Le Compétiteur":
                $ scenar_choisi = "Le Compétiteur"
                $ COUNT_SCENARIO_SON += 1
                jump vvd
            "Scénario: Le Squatteur":
                $ scenar_choisi = "Le Squatteur"
                $ COUNT_SCENARIO_SON += 1
                jump lune_de_miel
            "C'est bon j'ai ce qu'il me faut":
                $ son_still_training = False 
                jump companion_stats

    label companion_stats:

        python:
            plot_values = [
                S_COOL_VALUE,
                S_SPORTIF_VALUE,
                S_MYTHO_VALUE,
                S_FORCEUR_VALUE,
                S_SQUATTEUR_VALUE
            ]
            label_chart.values = plot_values

        scene bg main
        with dissolve

        show image label_chart:
            xalign 0.7
            yalign 0.4

        show ai_son:
            xalign 0.2
            yalign 0.4

        if first_show_stats: 
            stop sound
            play sound "05.mp3"
            ai_son "Voici la base du compagnon virtuel que l'on va créer."
            stop sound
            play sound "06.mp3"
            ai_son "Passons à l'entraînement du modèle."
            $ first_show_stats = False
            jump home 
        else:
            if son_still_training:
                stop sound
                play sound "07.mp3"
                ai_son "Merci d'avoir terminé le scénario \"[scenar_choisi]\". Regardons l'avancement de notre modèle..."
            else: 
                stop sound
                play sound "08.mp3"
                ai_son "Voici l'état actuel du compagnon virtuel."

            stop sound
            play sound "09.mp3"
            menu: 
                ai_son "Est-ce que le compagnon créé vous convient ?"
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

        stop sound
        play sound "10.mp3"
        ai "Quelle extension de modèles souhaitez vous ajouter ?"

        $ extension = True

        hide ai
        call model_choice from _call_model_choice_1

        jump model_lily

    label model_lily:
        scene bg main
        show ai:
            xalign 0.5
            yalign 0.4
        with dissolve
        if first_model_lily: 
            stop sound
            play sound "11.mp3"
            ai "Très bon choix! Vous avez sélectionné le modèle Lily."
            $ first_model_lily = False
        else: 
            stop sound
            stop music
            play sound "12.mp3"
            ai "Merci d'avoir complété le scénario: \"[scenar_choisi]\". Continuons..."
        stop sound
        play sound "13.mp3"
        menu:
            "Choisissez un scénario d'entraînement pour le modèle Lily."
            "Scénario: La Fine Gourmet": 
                $ scenar_choisi = "La Fine Gourmet"
                jump bouffe_galere
            "Scénario: La Guerrière":
                $ scenar_choisi = "La Guerrière"
                jump guerriere
            "Le modèle Lily est prêt":
                jump stats_lily 

    
    label model_fusion:
        scene bg main
        show ai:
            xalign 0.5
            yalign 0.4
        with dissolve
        if first_model_fusion:
            stop sound
            play sound "14.mp3"
            ai "Les modèles Lily et Son sont prêts, il est temps de les synchroniser." 
        else: 
            stop sound
            play sound "18.mp3"
            ai "Merci d'avoir complété le scénario \"[scenar_choisi]\"! Continuons l'entraînement."
        hide ai
        jump menu_fusion

    label menu_fusion:
        stop sound
        play sound "15.mp3"
        menu: 
            ai "Synchronisons nos deux modèles."
            "Scénario: Les Forceurs":
                $ scenar_choisi = "Les Forceurs"
                jump west_coast
            "Scénario: Maniaques":
                $ scenar_choisi = "Les Maniaques"
                jump tasses
            "C'est bon, les modèles sont prêts":
                jump mix_models_stats 


    label conclusion:
        stop sound
        play sound "16.mp3"
        "Merci d'avoir utilisé notre logiciel."
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

label stats_lily:
    python:
        plot_values = [
            L_COOL_VALUE,
            L_SPORTIF_VALUE,
            L_MYTHO_VALUE,
            L_FORCEUR_VALUE,
            L_SQUATTEUR_VALUE
        ]
        label_chart.values = plot_values

    scene bg main
    with dissolve

    show image label_chart:
        xalign 0.7
        yalign 0.4

    show ai:
        xalign 0.2
        yalign 0.4

    stop sound
    play sound "17.mp3"
    ai "Est-ce que le compagnon créé vous convient ?"
    menu: 
        "Oui, je suis pleinement satisfait":
            jump model_fusion 
        "Non, je souhaite continuer à entraîner le modèle":
            $ first_model_lily = True
            jump model_lily


