define coach = Character("Mec random", callback = name_callback, cb_name = "coach")
image coach = At('coach frame', sprite_highlight('coach'))
image steakguez = Image("steakguez frame.webp", oversample=1.4)

label le_cuistot: 
    stop music
    
    play sound "bbq.mp3"
    scene bg_barbecue
    with fade
    with Pause (3)

    show coach: 
        xalign 0.1
        yalign 0.4
    with dissolve

    coach "Son, Son! Je vais te montrer une recette que j'ai créé c'est de la bombe"

    show son:
        xalign 0.9
        yalign 0.4
    with dissolve
    
    s "Yo! Que pasa en la casa?"
    coach "Mec! je te présente le Steakguez, goûte ça"

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
            $ S_MYTHO_VALUE += 30
            $ S_COOL_VALUE -= 40
        "C'est la recette d'un pote qui fait des supers barbecues":
            $ S_COOL_VALUE += 30
        "Rajoutez du nuoc mam c'est vraiment incroyable":
            $ S_FORCEUR_VALUE += 20
        "C'est la recette de ma mère, elle fait les meilleurs steakguez":
            $ S_FORCEUR_VALUE += 30
            $ S_COOL_VALUE -= 30
            $ S_MYTHO_VALUE += 20

    jump companion_stats
