
# image patagonie = Image("patagonie.jpg")
image patagonie = Image("patagonie.jpg", oversample=2.5)

label lune_de_miel:
    play sound "drama.mp3" 
    scene black
    with fade
    "Pour ce panel nous avons invité un expert"
    "Cette personne a été victime d'un squatteur compulsif"
    show patagonie
    "\"Lune de miel\" en Patagonie"
    stop sound
    python: 
        S_FORCEUR_VALUE += 30
        S_SQUATTEUR_VALUE += 50
        S_COOL_VALUE -= 20
        
    jump companion_stats 
    

    # Vuong fait le tour et se "change"
    # Dialogue: 
    # P: "Alors vous avez été victime d'un squatteur?"
    #    
    # V: "C'est un épisode assez traumatisant de ma vie, au début j'ai eu beaucoup de mal à en parler...
    # Aujourd'hui ça va mieux mais en effet j'ai été victime d'un squatteur compulsif. C'était un très bon ami 
    # mais derrière ces allures de gars sympa se cachait un énorme squatteur"
    

    # P: "Comment c'est arrivé"
    #
    # V: "Ca s'est passé il y a quelques années, je me suis marié avec ma femme Olivia qui est dans le public
    # On voulait partir en Patagonie pour notre lune de miel. Le genre de voyage nature, romantique et intime quoi.
    # J'en ai parlé à un super ami qui s'appelle Son. Je lui disais la Patagonie ça va être trop bien on va faire de 
    # la randonnée... On est parti en voyage et voilà ce qui s'est passé"
    # 
    # P: "C'est dramatique comme situation... Comment vous avez fait pour vous en remettre?"
    #
    # V: "Je pense qu'il y a une solution différente pour chaque personne mais pour moi le mieux que j'ai trouvé 
    #   c'est la vengeance. J'ai appris que Son allait se marier bientôt et je compte bien squatter sa lune de miel. 
    #   et pour bien profiter de ma vengeance je vais même inviter un autre couple d'amis. Je connais déjà les dates
    #   et la destination, ils ne savent pas ce qui vont leur arriver"
    # 
    # P: "Merci beaucoup pour votre témoignage, ça aidera beaucoup de gens dans votre situation. Un applaudissement 
    # pour encourager la victime"


     

  

