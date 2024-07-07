# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("Son")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg osteo

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show son main:
        xalign 1.0
        yalign 1.0

    # These display lines of dialogue.

    s "Bienvenue dans mon cabinet ! Mettez-vous à l'aise, je vous embarque dans mon histoire..."

    # This ends the game.

    return
