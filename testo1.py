def carre(x) :
    return  x**2
x = float(input("Donner un réel pour calculer son carré :"))
if x >= 0 :
    print(f"Le carré du nombre {x} est : {carre(x)}")
else :
    print ("valeur_erronée !!")
  

