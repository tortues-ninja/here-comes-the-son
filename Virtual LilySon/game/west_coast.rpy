
image bg west coast = Transform("images/background/bg_west-coast.jpg", size=(1920, 1080), fit="fill")

label west_coast:
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
    jump model_fusion 
