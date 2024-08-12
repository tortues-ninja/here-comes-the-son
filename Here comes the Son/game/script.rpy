# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("Son")
define l = Character("Lise")
define v = Character("Amiral Vuong")
define p = Character("Capitaine Phong")

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

        show vuong main:
            xalign 1.0
            yalign 1.0

        v "Troi doc oi, nous sommes touchés !"
        v "Capitaine, quels sont les dégâts ?"

        show phong main:
            xalign 0.0
            yalign 1.0

        p "Le bouclier est hors-service et le réacteur principal est endommagé. C'est la merde."

    return
