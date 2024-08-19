# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define s = Character("Son", callback = name_callback, cb_name = "son")
define l = Character("Lise", callback = name_callback, cb_name = "lise")
define v = Character("Amiral Vuong", callback = name_callback, cb_name = "vuong")
define p = Character("Capitaine Phong", callback = name_callback, cb_name = "phong")
define pnj = Character("Mec random", callback = name_callback, cb_name = "pnj")
define n = Character(callback = name_callback, cb_name = None)



image son = At('son main frame', sprite_highlight('son'))
image pnj = At('pnj main frame', sprite_highlight('pnj'))
image steakguez = Image("steakguez frame.webp", oversample=1.4)


# The game starts here.

label start:

    "Commençons la création de votre compagnon virtuel"

    # Le menu principal pour charger des scénarios
    label home: 
        scene black
        with fade
        menu:

            "Cuisinier":
                jump le_cuistot
            "le guerrier de l'espace":
                jump command_deck


    # Scène du steakguez
    label le_cuistot: 
        
        play sound "bbq.mp3"
        scene bg_barbecue
        with fade
        with Pause (3)

        show pnj: 
            xalign 0.1
            yalign 0.4
        with dissolve

        pnj "Son, Son! Je vais te montrer une recette que j'ai créer c'est de la bombe"

        show son:
            xalign 0.9
            yalign 0.4
        with dissolve
        
        s "Yo! Que pasa en la casa?"
        pnj "Mec! je te présente le Steakguez, goûte ça"

        show steakguez:
            xalign 0.5
            yalign 0.4
        with dissolve

        s "Oh purée, c'est tellement bon"

        stop sound
        scene black
        with fade

        "Le weekend suivant..."

        scene bg salon massy
        with fade

        show son:
            xalign 0.1
            yalign 0.4
        with dissolve
        s "Bienvenue à mon barbecue d'anniversaire!"
        s "Venez goûter à cette tuerie, c'est un steakguez"

        menu: 
            "C'est une recette que j'ai inventée":
                jump home
            "C'est la recette d'un pote qui fait des supers barbecues":
                jump home
            "Rajoutez du nuoc mam c'est vraiment incroyable":
                jump home
            "C'est la recette de ma mère, elle fait les meilleurs steakguez":
                jump home

    label command_deck:

        # scene bg starship deck
        s "toto"


    # This ends the game.
    return
