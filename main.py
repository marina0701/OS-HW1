# variablen in römisch

i=1
v=5
x=10
l=50
c=100
d=500
m=1000

def roem(i):
    zif=[(1000,"M"),(900,"CM"),(500,"D"),(400,"CD"),(100,"C"),(90,"XC"),(50,"L"),(40,"XL"),(10,"X"),(9,"IX"),(5,"V"),(4,"IV"),(1,"I")]
    erg=""

    for ZErg, roembuch in zif:
        while i>= ZErg:
           erg+=roembuch
           i-=ZErg
    return erg
zahl=int(input("Bitte gebe eine Zahl ein die als Römische Zahl dargestellt werden soll:"))
print("info: I=5, V=5, X=10, L=50, C=100, D=500, M=1000")
print(roem(zahl))