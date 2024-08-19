define amar = Character("Maître Amar", callback = name_callback, cb_name = "amar")
image amar = At('amar frame', sprite_highlight('amar'))

label vvd:
    play sound "training.mp3"
    scene bg vvd
    with fade
    with Pause (1)

    show amar: 
        xalign 0.1
        yalign 0.4
    with dissolve

    amar "Demain c'est la finale de la coupe d'Europe de Viêt Vo Dao !"
    amar "Alors, comment est-ce que tu vas te préparer Son ?"

    show son: 
        xalign 0.9
        yalign 0.4
    with dissolve

    s "Hmmm..."

    menu: 
        "J'analyse mes adversaires en regardant des replays des qualifs":
            stop sound
            jump home
        "Je fais 20 pompes viets parce que je suis arrivé en retard":
            stop sound
            jump home
        "Je pars en soirée jusqu'au bout de la nuit avec mes compagnons d'armes":
            stop sound
            jump home
        "Je médite sous la douche":
            stop sound
            jump home