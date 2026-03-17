from utils import roem

def test_roem(zahl):
    if zahl <= 0 or zahl > 3999:
        print("Bitte Zahl zwischen 1 und 3999 eingeben.")
        return

    tausender = zahl // 1000
    hunderter = (zahl % 1000) // 100
    zehner = (zahl % 100) // 10
    einer = zahl % 10

    print(f"Hunderter: {roem(hunderter*100)}", f"tausender: {roem(tausender*1000)}", f"Zehner: {roem(zehner*10)}", f"Einer: {roem(einer)}", f"Gesamt: {roem(zahl)}")
