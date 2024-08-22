
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
        xalign 0.01
        yalign 0.4
    with dissolve
    pnj "C'est qui ce couple de oufs? Ils dansent trop bien je vais aller les voir."

    show lise:
        xalign 0.99
        yalign 0.4
    show son:
        xalign 0.67
        yalign 0.4
    with dissolve
    pause
    pnj "Vous dansez trop bien! ça fait combien de temps que vous faites du West Coast ?"

    l "Un mois !"
    pnj "(surpris) Un... mois ?"

    s "Oui oui mais tu sais, on danse que 5 fois par semaine." 
    l "On a aussi réaménager notre salon pour avoir de l'espace et danser à la maison."
    s "En même temps Lily..."
    s "Tu danses jusqu'à ne plus tenir debout à cause de ta blessure au pied. Tu vas jamais guérir!"
    l "Oh non, t'inquiètes pas Anh Son. Franchement j'aime bien ça hihi"
    pnj "Euh... OK..."
    pnj "Et les inscriptions à la compétition internationale SUPERSTAR à Manchester le mois prochain, c'est vraiment vos noms que j'ai vu?"
    l "C'est bien nous! On s'entraîne à fond cette année."
    s "Carrément! On a un objectif secret..."
    s "On va se marier cet été et on compte bien mettre la misère à tous nos invités sur le dancefloor hahaha"
    jump model_fusion 
