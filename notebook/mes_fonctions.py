def compter_mots(texte: str, seuil: int = 4):
    """
    Calculer la proportion de mots de plus de [seuil] lettres
    """
    liste_mots = texte.split(" ")
    nombre_mots = len(liste_mots)
    longueur_phrase = len(texte)
    if  longueur_phrase == 0: 
        return None    
    else:
        compteur = 0
        for i in liste_mots:
            if len(i) >= seuil:
                compteur+=1    
        proportion = round(100*compteur/nombre_mots,2)
        return proportion