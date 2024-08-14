# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("Son", callback = name_callback, cb_name = "son")
define l = Character("Lise", callback = name_callback, cb_name = "lise")
define v = Character("Amiral Vuong", callback = name_callback, cb_name = "vuong")
define p = Character("Capitaine Phong", callback = name_callback, cb_name = "phong")
define n = Character(callback = name_callback, cb_name = None)

image vuong = At('vuong main', sprite_highlight('vuong'))
image phong = At('phong main', sprite_highlight('phong'))

init python:
    def check_sound():
        if renpy.music.is_playing("sound"):
            remaining_duration = renpy.music.get_duration(channel='sound') - renpy.music.get_pos(channel='sound')
            renpy.pause(remaining_duration, hard=True)


# The game starts here.

label start:

    stop music

    play sound "space-battle.mp3"
    queue sound "explosion.mp3"
    scene bg space battle
    with fade
    with Pause (7)

    label command_deck:
        play music "starship-music.mp3"
        scene bg command deck
        with fade

        show vuong:
            xalign 1.0
            yalign 1.0

        v "Troi doc oi, nous sommes touchés !"
        v "Capitaine, quels sont les dégâts ?"

        show phong:
            xalign 0.0
            yalign 1.0

        p "Le bouclier est hors-service et le réacteur principal est endommagé. C'est la merde."
        v "Qu'est-ce qu'on peut faire pour survivre à tout ça et arriver sains et saufs au mariage ? Si on loupe la cérémonie, Son va avoir le seum et Lise va nous faire son regard noir là..."
        p "Tout sauf ça mon Amiral ! Il nous faut rétablir le bouclier pour se laisser le temps de réparer le réacteur. Seul problème : il fonctionne à la Force, et les Jedis ne sont plus ce qu'ils étaient depuis que Disney a racheté la license..."
        v "N'y a t-il pas un autre moyen de se procurer de la Force ?"
        p "Si, mais ça ne sera pas facile : à part les Jedi, seuls les Forceurs peuvent produire de la Force. Il suffit en principe de raconter des histoires de Forceurs à l'intelligence artificielle pilotant le vaisseau, et la jauge de Force montera toute seule. Vous en connaissez vous ?"
        v "Tu plaisantes mon brave ! Au mariage de qui devons nous nous rendre ?"
        p "Lise et Son... ? Ah mais oui bien sûr... Allons vite raconter les histoires à l'IA !"

    return
