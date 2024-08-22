image alily = Image("lise main frame.png", oversample=2)
image ason = Image("son main frame.png", oversample=2)

image fused_1 = Image("fusion-1.webp", oversample=1)
image fused_2 = Image("fusion-2.webp", oversample=1)

image anim_son:
    parallel:
        xalign 0.9
        yalign 0.4
        pause 1
        linear 5.0 xalign 0.5
    parallel:
        "son main frame.png"

image anim_lily:
    parallel:
        xalign 0.1
        yalign 0.4
        pause 1
        linear 5.0 xalign 0.5
    parallel:
        "lise main frame.png"
#
#
# transform right_to_left:
#     xalign 0.9
#     yalign 0.4
#     pause 1
#     linear 6.0 xalign 0.5
#     hide ason with dissolve

label fuse_faces:
    stop sound
    stop music
    "Le processus de fusion des modèles commence dans 3, 2, 1..."
    "Fusion enclenché!"
    show anim_son
    show anim_lily
    play sound "fusion_sound.mp3"
    pause 5.5
    hide anim_son with dissolve
    hide anim_lily with dissolve

    show fused_1 with flash:
        xalign 0.2
        yalign 0.4

    show fused_2 with flash:
        xalign 0.8
        yalign 0.4

    "Fusion terminée!"
    "Deux compagnons finals ont été obtenus: le compagnon LilySon et le compagnon SonLily"
    "Veuillez choisir votre préféré"
    jump conclusion

