class Tasse:
    # Attribut de classe
    matière = "céramique"
    
    # Méthode d'initialisation (constructeur)
    def __init__(self, couleur, contenance, marque):
        self.couleur = couleur
        self.contenance = contenance
        self.marque = marque
    
    #méthode de renvoie de l'objet formaté
    def __str__(self):
        return f"La tasse de matière {Tasse.matière}, de couleur {self.couleur} et de marque {self.marque} a une contenance de {self.contenance} ml."
    
    # Méthode pour ajouter un contenu à la tasse
    def ajouter_contenu(self, contenu):
        self.contenu = contenu
        print(f"Contenu ajouté : {self.contenu}")
    
    def boire(self):
        if hasattr(self, 'contenu'):
            print(f"La boisson {self.contenu} a été bue.")
            del self.contenu
        else:
            print("La tasse est déjà vide.")


#Instanciation d'objets de la classe Tasse
tasse1 = Tasse("bleue", 50, "duralex")
tasse2 = Tasse("rouge", 100, "ikea")

# Affichage des objets
print(tasse1)
print(tasse2)

# Utilisation des méthodes
tasse1.ajouter_contenu("café")
tasse2.ajouter_contenu("thé")

# Boire le contenu des tasses
tasse1.boire()
tasse2.boire()

# Essayer de boire encore une fois alors que la tasse est vide
tasse1.boire()