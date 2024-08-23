define sommet_torres = Image("sommet_torres.jpg", oversample=4)
label guerriere:
    scene bg_montagne
    play music "persona.mp3"

    show pnj:
        xalign 0.1
        yalign 0.4
    with dissolve
    "Bon pour la randonnée de demain il y a juste 22km à faire et 1600m de dénivelé."
    show lise:
        xalign 0.9
        yalign 0.4
    with dissolve
    l "(Je me suis blessé au pied la veille. Pas sûre que je suis en état de marcher...)"
    "Ah oui, il faut qu'on parte à 3h du matin sinon on risque de louper le level du soleil sur le sommet."
    "Aussi j'ai oublié de vous dire: il risque de pleuvoir en bas et neiger en haut hahaha"
    l "(... gloups)"
    menu:
        "Quelle décision vais-je prendre?"
        "\"No pain, no gain\"! Je suis pas une faible comme Anh Son. Let's go! ":
            $ L_FORCEUR_VALUE += 40
            $ L_COOL_VALUE += 30
            $ L_SPORTIF_VALUE += 30
        "Pfff trop facile... Je vais mettre mes chaussures pas imperméables pour avoir les pieds trempés en plus":
            $ L_FORCEUR_VALUE += 50
            $ L_SPORTIF_VALUE += 30
        "Je suis sûre que la vue en haut sera inoubliable. Je vais marcher en pensant au Pisco Sour du retour et ça va le faire":
            $ L_FORCEUR_VALUE += 40
            $ L_SPORTIF_VALUE += 30
        "Je vais leur dire que c'est une petite douleur. Ils s'inquièteront moins quitte à casser mon pied pour les prochains mois":
            $ L_FORCEUR_VALUE += 30
            $ L_MYTHO_VALUE += 20
            $ L_SPORTIF_VALUE += 30
            
    scene black
    show image sommet_torres:
        xalign 0.5
        yalign 0.8
    with dissolve
    "Un couple au sommet! (elle est montée 😱)"
    
    jump model_lily
    
        
