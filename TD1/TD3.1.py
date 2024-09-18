def bonjour ( nom : str ) -> None :
    """fonction permettant de dire bonjour \‘a une personne dont
    le nom est pass \ ’e en argument
    """
    print (f" bonjour { nom }")
if __name__ == " __main__ ":
    bonjour (" Arnauld ")
    print (f" documentation fonction bonjour { bonjour . __doc__ }")    