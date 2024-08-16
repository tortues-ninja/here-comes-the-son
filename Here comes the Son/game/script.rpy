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

image bg starship deck = Transform("images/bg starship deck.jpg", size=(1920, 1080), fit="fill")
image bg ai face = Transform("images/bg ai face.jpg", size=(1920, 1080), fit="fill")
image bg wedding landing = Transform("images/bg wedding landing.jpg", size=(1920, 1080), fit="fill")
image bg filled gauge = Transform("images/bg filled gauge.jpg", size=(1920, 1080), fit="fill")


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
        scene bg starship deck
        with fade

        show vuong:
            xalign 1.0
            yalign 1.0
        with dissolve

        v "Trời đất ơi, nous sommes touchés !"
        v "Capitaine, quels sont les dégâts ?"

        show phong:
            xalign 0.0
            yalign 1.0
        with dissolve

        p "Le bouclier est hors-service et le réacteur principal est endommagé. C'est la merde."
        v "Qu'est-ce qu'on peut faire pour survivre à tout ça et arriver sains et saufs au mariage ? Si on loupe la cérémonie, Son va avoir le seum et Lise va nous faire son regard noir là..."
        p "Tout sauf ça mon Amiral ! Il nous faut rétablir le bouclier pour se laisser le temps de réparer le réacteur."
        p "Seul problème : il fonctionne à la Force, et les Jedis ne sont plus ce qu'ils étaient depuis que Disney a racheté la license..."
        v "N'y a t-il pas un autre moyen de se procurer de la Force ?"
        p "Si, mais ça ne sera pas facile : à part les Jedi, seuls les Forceurs peuvent produire de la Force."
        p "Il suffit en principe de raconter des histoires de Forceurs à l'intelligence artificielle pilotant le vaisseau, et la jauge de Force montera toute seule. Vous en connaissez vous ?"
        v "Tu plaisantes mon brave ! Au mariage de qui devons nous nous rendre ?"
        p "Lise et Son... ? Ah mais oui bien sûr... Allons vite raconter les histoires à l'IA !"
    
    label ai_story:
        scene bg ai face
        with fade

        show vuong:
            xalign 1.0
            yalign 1.0
        with dissolve

        v "Alors, quelle histoire voulez vous entendre ?"

        menu:
            "Un nouveau hobby ? Et si on y allait mollo...":
                jump ending
            "Pas invité ? Pas grave !":
                jump ending
            "Broneymoon":
                jump ending

    label ending:
        scene bg filled gauge
        with fade

        show phong:
            xalign 0.0
            yalign 1.0
        with dissolve

        p "Mon Amiral, la jauge est remplie ! Le bouclier est fonctionnel !"
        p "Nous allons pouvoir réparer le réacteur principal et reprendre notre route vers le mariage de Lise et Son !"

        show vuong:
            xalign 1.0
            yalign 1.0
        with dissolve

        v "Excellente nouvelle mon brave !"
        v "Je n'aurais pas aimé voir la tête de Lise si les témoins de son mari n'avaient pas pu être là."
        p "Heureusement que ce sont de vrais Forceurs !"
        v "Oui ! Comme l'a dit un grand philosophe, 'Ce qui ne nous tue pas, nous rend plus forceurs'"
        p "Je ne suis pas sûr que ce soit la bonne citation..."
        v "'Qui ne force rien n'a rien' ?"
        p "Allez on arrête là, je crois qu'on approche de la Terre mon Amiral."

        scene bg wedding landing
        with fade

        p "Mon Amiral, j'ai l'impression qu'on a loupé la cérémonie."
        v "Ce n'est pas bien grave mon brave. On arrive pour le mot de la fin !"
        p "À vous l'honneur."
        v "Comme l'a dit un grand philosophe, 'L'Amour, c'est forcer ensemble dans la même direction !'"
        p "Et vive les mariés !"

    return
