class Velo:
    """
    Classe représentant un vélo avec ses caractéristiques et des méthodes pour changer de vitesse.

    :param marque: La marque du vélo
    :param taille_pneu: La taille des pneus en pouces
    :param couleur: La couleur du vélo
    :param nb_vitesses: Le nombre de vitesses que possède le vélo
    """
    
    def __init__(self, marque, taille_pneu, couleur, nb_vitesses):
        """
        Initialise les attributs de la classe Velo.
        """
        self.marque = marque
        self.taille_pneu = taille_pneu
        self.couleur = couleur
        self.nb_vitesses = nb_vitesses
        self.vitesse_courante = 1  # La vitesse commence à 1 par défaut
    
    def gear_up(self):
        """
        Augmente la vitesse courante d'une unité, sans dépasser le nombre maximal de vitesses.
        
        :return: La vitesse courante après l'augmentation.
        """
        if self.vitesse_courante < self.nb_vitesses:
            self.vitesse_courante += 1
        return self.vitesse_courante
    
    def gear_down(self):
        """
        Diminue la vitesse courante d'une unité, sans descendre en dessous de 1.
        
        :return: La vitesse courante après la diminution.
        """
        if self.vitesse_courante > 1:
            self.vitesse_courante -= 1
        return self.vitesse_courante

