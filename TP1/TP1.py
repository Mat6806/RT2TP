import math

class Point:
    """
    Représente un point dans un repère cartésien.

    :ivar x: L'abscisse du point.
    :ivar y: L'ordonnée du point.
    """

    def __init__(self, x=0, y=0):
        """
        Constructeur de la classe Point.

        :param a: L'abscisse du point (par défaut 0).
        :type a: float
        :param b: L'ordonnée du point (par défaut 0).
        :type b: float
        """
        self.x = x
        self.y = y

    def distanceCoord(self, a, b):
        """
        Calcule la distance entre le point actuel et un autre point spécifié par ses coordonnées.

        :param a: L'abscisse de l'autre point.
        :type a: float
        :param b: L'ordonnée de l'autre point.
        :type b: float
        :return: La distance entre les deux points.
        :rtype: float
        """
        return math.sqrt((self.x - a) ** 2 + (self.y - b) ** 2)

    def distancePoint(self, camarade):
        """
        Calcule la distance entre le point actuel et un autre point représenté par un objet Point.

        :param camarade: L'autre point.
        :type camarade: Point
        :return: La distance entre les deux points.
        :rtype: float
        """
        return self.distanceCoord(camarade.x, camarade.y)
    

class Cercle:
    """
    Classe représentant un cercle dans un repère cartésien.
    
    :param centre: Le centre du cercle (un objet Point)
    :param rayon: Le rayon du cercle
    """
    
    def __init__(self, rayon, centre=None):
        """
        Initialise un cercle avec un centre et un rayon.
        Si aucun centre n'est fourni, le centre est à l'origine (0,0).
        :param centre: Centre du cercle (par défaut Point(0, 0))
        :param rayon: Rayon du cercle
        """
        if centre is None:
            centre = Point(0.0, 0.0)
        self.centre = centre
        self.rayon = rayon

    def diametre(self):
        """
        Calcule le diamètre du cercle.
        :return: Le diamètre du cercle
        """
        return 2 * self.rayon

    def perimetre(self):
        """
        Calcule le périmètre du cercle.
        :return: Le périmètre du cercle
        """
        return 2 * math.pi * self.rayon

    def surface(self):
        """
        Calcule la surface du cercle.
        :return: La surface du cercle
        """
        return math.pi * (self.rayon ** 2)

    def intersection(self, autre_cercle):
        """
        Détermine si ce cercle est en intersection avec un autre cercle.
        :param autre_cercle: Un autre objet Cercle
        :return: True si les cercles se croisent, False sinon
        """
        distance = self.centre.distancePoint(autre_cercle.centre)
        return distance <= self.rayon + autre_cercle.rayon

    def contientPoint(self, point):
        """
        Détermine si un point donné est à l'intérieur du cercle.
        :param point: Un objet Point
        :return: True si le point est dans le cercle, False sinon
        """
        return self.centre.distancePoint(point) <= self.rayon


class Rectangle:
    """
    Classe représentant un rectangle dans un repère cartésien.
    
    :param bas_gauche: Le point en bas à gauche du rectangle
    :param longueur: La longueur du rectangle
    :param hauteur: La hauteur du rectangle
    """
    
    def __init__(self, bas_gauche=None, longueur=1.0, hauteur=1.0):
        """
        Initialise un rectangle avec un point bas-gauche, une longueur et une hauteur.
        Par défaut, le rectangle est situé à l'origine (0,0) et a une longueur et hauteur de 1.
        :param bas_gauche: Le point bas-gauche du rectangle (par défaut Point(0, 0))
        :param longueur: La longueur du rectangle
        :param hauteur: La hauteur du rectangle
        """
        if bas_gauche is None:
            bas_gauche = Point(0.0, 0.0)
        self.bas_gauche = bas_gauche
        self.longueur = longueur
        self.hauteur = hauteur

    def surface(self):
        """
        Calcule la surface du rectangle.
        :return: La surface du rectangle
        """
        return self.longueur * self.hauteur

    def perimetre(self):
        """
        Calcule le périmètre du rectangle.
        :return: Le périmètre du rectangle
        """
        return 2 * (self.longueur + self.hauteur)

    def point_bas_droit(self):
        """
        Retourne le point bas-droit du rectangle.
        :return: Le point bas-droit du rectangle
        """
        return Point(self.bas_gauche.x + self.longueur, self.bas_gauche.y)

    def point_haut_gauche(self):
        """
        Retourne le point haut-gauche du rectangle.
        :return: Le point haut-gauche du rectangle
        """
        return Point(self.bas_gauche.x, self.bas_gauche.y + self.hauteur)

    def point_haut_droit(self):
        """
        Retourne le point haut-droit du rectangle.
        :return: Le point haut-droit du rectangle
        """
        return Point(self.bas_gauche.x + self.longueur, self.bas_gauche.y + self.hauteur)

    def contientPoint(self, point):
        """
        Détermine si un point est à l'intérieur du rectangle.
        :param point: Un objet Point
        :return: True si le point est dans le rectangle, False sinon
        """
        return (self.bas_gauche.x <= point.x <= self.point_bas_droit().x and
                self.bas_gauche.y <= point.y <= self.point_haut_gauche().y)

    
    

point1 = Point(2.0,9.0)
cercle1 = Cercle(2.0)
rectangle1 = Rectangle(None,5,3)
print(rectangle1.contientPoint(1))
print(cercle1.diametre())
#print(point1.distanceCoord(2232.0,9.0))
    