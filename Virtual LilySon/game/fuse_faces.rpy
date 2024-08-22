image alily = Image("lise main frame.png", oversample=1)
image ason = Image("son main frame.png", oversample=1)

image fused_1 = Image("fusion-1.webp", oversample=1)
image fused_2 = Image("fusion-2.webp", oversample=1)

image anim_son:
    parallel:
        xalign 0.99
        yalign 0.4
        pause 1
        linear 4.0 xalign 0.5
    parallel:
        "son main frame.png"

image anim_lily:
    parallel:
        xalign 0.01
        yalign 0.4
        pause 1
        linear 4.0 xalign 0.5
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

label mix_models_stats:
    stop sound
    stop music
    show ai:
        xalign 0.5
        yalign 0.4
    with dissolve
    ai "Voyons les stats actuelles de votre compagnon virtuel"
    python: 
        COOL_VALUE = 100
        SPORTIF_VALUE = 95   
        FORCEUR_VALUE = 110  
        MYTHO_VALUE = 40     
        SQUATTEUR_VALUE = 60 

        label_chart.values = [
                COOL_VALUE,
                SPORTIF_VALUE,
                FORCEUR_VALUE,
                MYTHO_VALUE,
                SQUATTEUR_VALUE
            ]
        label_chart.labels = [
        Text('Cools'), 
        Text('Sportifs'), 
        Text('Forceurs'), 
        Text('Mythos'), 
        Text('Squatteurs')
    ]

    hide ai
    show image label_chart:
        xalign 0.5
        yalign 0.4
    with dissolve
    show alily:
        xalign 0.01
        yalign 0.4
    with dissolve
    show ason:
        xalign 0.99
        yalign 0.4
    with dissolve


    "C'est pas mal non?"
    menu: 
        "Fusionner les modèles":
            hide label_chart with dissolve
            jump fuse_faces
        "Annuler":
            hide image label_chart
            jump mix_models_stats

label fuse_faces:
    "Le processus de fusion des modèles commence dans 3, 2, 1..."
    "Fusion enclenché!"
    hide ason
    hide alily 
    show anim_son
    show anim_lily
    play sound "fusion_sound.mp3"
    pause 4.5
    hide anim_son with dissolve
    hide anim_lily with dissolve

    show fused_2 with flash:
        xalign 0.2
        yalign 0.4

    show fused_1 with flash:
        xalign 0.8
        yalign 0.4

    "Fusion terminée!"
    "Deux compagnons finals ont été obtenus: le compagnon LilySon et le compagnon SonLily."
    "Veuillez choisir votre préféré."
    jump conclusion

