from math import * #importi parandamine
print("Ruudu karakteristikud")
try:
    a=int(input('Sisesta ruudu külje pikkus => ')) #oli vaja lisada int
    if type(a)== int and a>0:
        print("Õige number"
        S=a**2
    else:
        print("kirjutage number mitte taht")
except:
    print("valed andmed")
print("Ruudu pindala", S)
P=4*a
print("Ruudu ümbermõõt", P) #oli kirjutatud valesti juttumargid
di=a*sqrt(2) #math oli vaja kustutada ja oigesti kirjutada sqrt
print("Ruudu diagonaal", round(di,2))
print()
print("Ristküliku karakteristikud") #ekstra sulg 
try:
    b=int(input("Sisesta ristküliku 1. külje pikkus => ")) #oli vaja lisada int 
    c=int(input("Sisesta ristküliku 2. külje pikkus => ")) #oli vaja lisada int 
    if type(b)== int and b>0 and type(c)== int and c>0:
        print("Õige number")
        S=b*c
        print("Ristküliku pindala", S) #lisada sulud ja vahetada juttumargid
        P=2*(b+c) #puudus korrutamismärk
        print("Ristküliku ümbermõõt", P)
        di=sqrt(b**2+c**2) #math oli vaja kustutada
        print("Ristküliku diagonaal", round(di,2)) # lisame 2
        print()
    else:
        print("kirjutage number mitte taht")
except:
    print("valed andmed")

print("Ringi karakteristikud")
r=float(input("Sisesta ringi raadiusi pikkus => ")) #valesti pandud juttumargid ja lisame float
d=2*r #kirjutame korrutamismärgi
print("Ringi läbimõõt", d) #polnud koma märki
S=pi*r**2 #kustutame sulud ja lisame astme märgi
print("Ringi pindala", round(S))
C=2*pi*r #kustutame sulud ja lisame korrutis märgi
print("Ringjoone pikkus", round(C)) #ei olnud viimast sulgu
