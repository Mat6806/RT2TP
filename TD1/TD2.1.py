class MaClasse :
   monAttributClasse : str = " bonjour "
   def __init__ ( self , valeur : int ):
     self . monAttributInstance = valeur

mc = MaClasse (12) 
print (f"{mc} , {mc. monAttributClasse } ,{ mc. monAttributInstance }")
