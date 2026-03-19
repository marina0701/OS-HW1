"""function to convert arabic numbers to roman number format."""
def roem(i):
    """function for converting"""

    zif=[(1000,"M"),
         (900,"CM"),
         (500,"D"),
         (400,"CD"),
         (100,"C"),
         (90,"XC"),
         (50,"L"),
         (40,"XL"),
         (10,"X"),
         (9,"IX"),
         (5,"V"),
         (4,"IV"),
         (1,"I")]
    erg=""

    for erg2, roembuch in zif:
        while i>= erg2:
            erg+=roembuch
            i-=erg2
    return erg
