define lily_trombi = Image("lise main frame.png", oversample=2)
define poisson_trombi = Image("poisson.jpg", oversample=5)
define son_trombi = Image("son main.png", oversample=2)
define nemo_trombi = Image("nemo.png", oversample=5)
define the_rock_trombi = Image("the rock.png", oversample=6)
define vuong_trombi = Image("vuong main.png", oversample=2)
define phong_trombi = Image("phong main.png", oversample=2)
define artanis_trombi = Image("artanis.jpg", oversample=3.5)
define baloo_trombi = Image("baloo.jpg", oversample=4)


label model_choice: 
    show screen trombi
    pause
    pause
    pause
    pause
    pause
    pause
    pause
    pause
    pause

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
            imagebutton: 
                idle son_trombi 
                action Jump("clear_trombi")
        frame:
            xalign 0.5 
            yalign 0.5
            imagebutton: 
                idle lily_trombi
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
    jump home
    

