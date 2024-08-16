# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("Son", callback = name_callback, cb_name = "son")
define l = Character("Lise", callback = name_callback, cb_name = "lise")
define v = Character("Amiral Vuong", callback = name_callback, cb_name = "vuong")
define p = Character("Capitaine Phong", callback = name_callback, cb_name = "phong")
define pnj = Character("Mec random", callback = name_callback, cb_name = "pnj")
define n = Character(callback = name_callback, cb_name = None)

image vuong = At('vuong main frame', sprite_highlight('vuong'))
image phong = At('phong main frame', sprite_highlight('phong'))
image lise = At('lise main frame', sprite_highlight('lise'))
image son = At('son main frame', sprite_highlight('son'))
image pnj = At('pnj main frame', sprite_highlight('pnj'))

image bg starship deck = Transform("images/bg starship deck.jpg", size=(1920, 1080), fit="fill")
image bg ai face = Transform("images/bg ai face.jpg", size=(1920, 1080), fit="fill")
image bg wedding landing = Transform("images/bg wedding landing.jpg", size=(1920, 1080), fit="fill")
image bg filled gauge = Transform("images/bg filled gauge.jpg", size=(1920, 1080), fit="fill")
image bg west coast = Transform("images/west-coast.jpg", size=(1920, 1080), fit="fill")



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
        stop sound
        play music "starship-music.mp3"
        scene bg starship deck
        with fade

        show vuong:
            xalign 0.9
            yalign 0.4
        with dissolve

        v "Trời đất ơi, nous sommes touchés !"
        v "Capitaine, quels sont les dégâts ?"

        show phong:
            xalign 0.1
            yalign 0.4
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
        stop music
        play music "ai-beeping-sound.mp3"
        scene bg ai face
        with fade

        show vuong:
            xalign 0.9
            yalign 0.4
        with dissolve

        v "Alors, quelle histoire voulez vous entendre ?"

        hide vuong

        menu:
            "Un nouveau hobby ? Et si on y allait mollo...":
                jump hobby
            "Pas invité ? Pas grave !":
                jump ending
            "Broneymoon":
                jump ending
            "On a écouté toutes les histoires !":
                jump ending

    label hobby:
        stop music
        play sound "persona.mp3"
        scene bg salon massy
        with fade
        with Pause(0.5)

        show lise:
            xalign 0.9
            yalign 0.4
        with dissolve

        l "Anh Son j'ai trop envie qu'on fasse du West Coast Swing ensemble !"

        show son:
            xalign 0.1
            yalign 0.4
        with dissolve

        s "Du quoi ?"
        l "C'est une danse à deux de style swing, issue du Lindy Hop dont les mouvements ont été adoucis tout au long du XXe siècle."
        l "Elle est caractérisée par des mouvements très fluides et élastiques des partenaires et laisse une grande place à l'humour et au fun."
        s "Merci Wikilily, trop chaud !"
        l "Ok, alors, je cherche, \"cours débutants\"..."

        scene bg west coast
        with fade

        show pnj:
            xalign 0.1
            yalign 0.4
        with dissolve

        pnj "Vous dansez trop bien, ça fait combien de temps que vous faites du West Coast ?"

        show lise:
            xalign 0.9
            yalign 0.4
        with dissolve

        l "Un mois !"
        pnj "(surpris) Un... mois ?"

        hide lise
        show son:
            xalign 0.9
            yalign 0.4
        with dissolve

        s "Oui oui, mais en vrai c'est plus facile quand t'as fait du Viet Vo Dao, du tennis et de l'escalade avant, c'est un peu les mêmes moves."
        pnj "Euh... OK. Et les inscriptions à la compétition internationale à Manchester le mois prochain, c'est des homonymes ou bien... ?"

        hide son
        show lise:
            xalign 0.9
            yalign 0.4
        with dissolve

        l "C'est bien nous !"

        stop music
        play music "ai-beeping-sound.mp3"
        scene bg ai face
        with fade

        show phong:
            xalign 0.1
            yalign 0.4
        with dissolve

        p "Ah effectivement mon Amiral, une belle histoire de Forceurs !"

        show vuong:
            xalign 0.9
            yalign 0.4
        with dissolve

        v "Attends, tu ne sais pas tout. Ils font 5 entraînements par semaine, parfois jusqu'à 2h du matin."
        v "Et ça fait trois mois que Lise danse avec des pieds pourris et endoloris, et la seule raison qui l'a mise au repos c'est la perspective du mariage."
        p "Ça ne m'étonne pas, c'était pareil avec le chant et l'escalade..."
        v "En tout cas, merci les Forceurs, ça nous fait une jauge de Force de plus !"

        jump ai_story

    label ending:
        stop music
        play sound "loading-bar-sound.mp3"
        scene bg filled gauge
        with fade
        with Pause(1.5)

        play music "congratulations.mp3"

        show phong:
            xalign 0.1
            yalign 0.4
        with dissolve

        p "Mon Amiral, la jauge est remplie ! Le bouclier est fonctionnel !"
        p "Nous allons pouvoir réparer le réacteur principal et reprendre notre route vers le mariage de Lise et Son !"

        show vuong:
            xalign 0.9
            yalign 0.4
        with dissolve

        v "Excellente nouvelle mon brave !"
        v "Je n'aurais pas aimé voir la tête de Lise si les témoins de son mari n'avaient pas pu être là."
        p "Heureusement que ce sont de vrais Forceurs !"
        v "Oui ! Comme l'a dit un grand philosophe, \"Ce qui ne nous tue pas, nous rend plus forceurs\""
        p "Je ne suis pas sûr que ce soit la bonne citation..."
        v "\"Qui ne force rien n'a rien\" ?"
        p "Allez on arrête là, je crois qu'on approche de la Terre mon Amiral."

        stop music
        play music "wedding-applause.mp3"
        scene bg wedding landing
        with fade

        show phong:
            xalign 0.1
            yalign 0.4
        with dissolve

        p "Mon Amiral, j'ai l'impression qu'on a loupé la cérémonie."

        show vuong:
            xalign 0.9
            yalign 0.4
        with dissolve

        v "Ce n'est pas bien grave mon brave. On arrive pour le mot de la fin !"
        p "À vous l'honneur."
        v "Comme l'a dit un grand philosophe, \"L'Amour, c'est forcer ensemble dans la même direction !\""
        p "Et vive les mariés !"

    return
