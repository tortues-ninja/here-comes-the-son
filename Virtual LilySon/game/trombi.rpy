define lily_trombi = Image("lise main frame.png", oversample=1.7)
define poisson_trombi = Image("poisson.jpg", oversample=1.7)
define son_trombi = Image("son main frame.png", oversample=1.7)
define nemo_trombi = Image("nemo.png", oversample=1.7)
define the_rock_trombi = Image("the rock.png", oversample=1.7)
define vuong_trombi = Image("vuong main frame.png", oversample=1.7)
define phong_trombi = Image("phong main frame.png", oversample=1.7)
define artanis_trombi = Image("artanis.png", oversample=1.7)
define baloo_trombi = Image("baloo.jpg", oversample=1.7)
define son_barre_trombi = Image("son main frame barred.png", oversample=1.7)


label model_choice: 
    window hide
    show screen trombi
    "Choisissez un modèle à entraîner"
    "Choisissez un modèle à entraîner"
    "Choisissez un modèle à entraîner"
    "Choisissez un modèle à entraîner"
    "Choisissez un modèle à entraîner"
    "Choisissez un modèle à entraîner"
    "Choisissez un modèle à entraîner"
    "Choisissez un modèle à entraîner"
    "Choisissez un modèle à entraîner"
    "Choisissez un modèle à entraîner"
    "Choisissez un modèle à entraîner"
    "Choisissez un modèle à entraîner"
   
screen trombi:
    grid 3 3:
        xalign 0.5
        yalign 0.2
        frame:
            xalign 0.5 
            yalign 0.5
            imagebutton: 
                idle baloo_trombi 
                action Jump("modele_non_disponible")
        frame:
            xalign 0.5 
            yalign 0.5
            imagebutton: 
                idle the_rock_trombi
                action Jump("modele_non_disponible")
        frame:
            xalign 0.5 
            yalign 0.5
            if extension:
                image son_barre_trombi
            else:
                imagebutton: 
                    idle son_trombi 
                    action Jump("clear_trombi")
        frame:
            xalign 0.5 
            yalign 0.5
            imagebutton: 
                idle lily_trombi
                if extension:
                    action Jump("clear_trombi")
                else:
                    action Jump("modele_non_disponible")
        frame:
            xalign 0.5 
            yalign 0.5
            imagebutton:
                idle phong_trombi 
                action Jump("modele_non_disponible")
        frame:
            xalign 0.5 
            yalign 0.5
            imagebutton:
                idle artanis_trombi 
                action Jump("modele_non_disponible")

screen trombi_error:
    grid 3 3:
        xalign 0.5
        yalign 0.2
        frame:
            xalign 0.5 
            yalign 0.5
            image baloo_trombi
        frame:
            xalign 0.5 
            yalign 0.5
            image the_rock_trombi
        frame:
            xalign 0.5 
            yalign 0.5
            if extension: 
                image son_barre_trombi
            else:
                image son_trombi 
        frame:
            xalign 0.5 
            yalign 0.5
            image lily_trombi
        frame:
            xalign 0.5 
            yalign 0.5
            image phong_trombi
        frame:
            xalign 0.5 
            yalign 0.5
            image artanis_trombi 

screen text_non_dispo:
    frame: 
        # background white 
        xpadding 40
        ypadding 20
        xalign 0.5
        yalign 0.5
        if extension:
            text "Je crois qu'il y a un meilleur modèle à choisir."
        else:
            text "Modèle non disponible dans la version gratuite. Veuillez choisir le modèle de base."

label modele_non_disponible:
    hide screen trombi
    show screen trombi_error
    show screen text_non_dispo
    pause
    hide screen trombi_error
    hide screen text_non_dispo
    jump model_choice 

label clear_trombi: 
    hide screen trombi
    return
    # if extension:
    #     jump model_lily
    # else: 
    #     jump home
    

