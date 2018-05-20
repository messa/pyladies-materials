# https://docs.google.com/document/d/1LTf2-077v4KF1LKgR6tUA68Z6iIHGz-qcLTrs7pF8Js/edit

'''
Ve vozovém parku jsou různé druhy vozů - na naftu a elektřinu.
Autobus na elektřinu bude zřejmě nejlevnější varianta, ale asi jím nechceme
poslat školu na školní výlet, pokud by vzdálenost byla delší, než dojezd
autobusu, protože autobus by se musel po cestě na několik hodin zastavit
kvůli nabití. Naopak zastavit s autobusem na naftu kvůli tankování nafty
není problém. Zkus to zohlednit v té funkci, která hledá optimální autobus
pro školní výlet. (Zřejmě bude potřeba přidat argument, jak dlouhý ten výlet
bude.)
'''

class Vuz:

    def __init__(self, spz):
        self.spz = spz


class VuzNaNaftu (Vuz):

    def vzdalenost_je_ok(self, vzdalenost):
        return True


class VuzNaElektrinu (Vuz):

    def vzdalenost_je_ok(self, vzdalenost):
        return vzdalenost <= self.dojezd


class IrizaPB (VuzNaNaftu):

    kapacita = 63
    naklady_za_km = 60


class IrisbusArwayShort (VuzNaNaftu):

    kapacita = 43
    naklady_za_km = 40


class IrisbusArwayLong (VuzNaNaftu):

    kapacita = 77
    naklady_za_km = 55


class TeslaBus (VuzNaElektrinu):

    kapacita = 62
    naklady_za_km = 52
    dojezd = 150


vozovy_park = [
    IrizaPB('1A11111'),
    IrizaPB('1A12222'),
    IrisbusArwayShort('1A13333'),
    IrisbusArwayLong('1A14444'),
    TeslaBus('1A15555'),
]

def najit_vhodny_autobus(seznam_vozu, pozadovana_kapacita, vzdalenost):
    vhodne_vozy = []
    for vuz in seznam_vozu:
        if vuz.kapacita < pozadovana_kapacita:
            continue
        if not vuz.vzdalenost_je_ok(vzdalenost):
            continue
        vhodne_vozy.append(vuz)
    if not vhodne_vozy:
        return None
    return min(vhodne_vozy, key=lambda vuz: vuz.naklady_za_km)

assert najit_vhodny_autobus(vozovy_park, 60, 200).spz == '1A14444'
assert najit_vhodny_autobus(vozovy_park, 60, 100).spz == '1A15555'
