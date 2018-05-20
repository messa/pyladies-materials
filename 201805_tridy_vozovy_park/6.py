# https://docs.google.com/document/d/1LTf2-077v4KF1LKgR6tUA68Z6iIHGz-qcLTrs7pF8Js/edit

'''
Každý vůz má jiné náklady za kilometr.
Zkus toto v programu nějak zohlednit - ideálně aby funkce, která hledá autobus
pro ten školní výlet, našla co nejekonomičtější variantu.
'''

class Vuz:

    def __init__(self, spz):
        self.spz = spz

class IrizaPB (Vuz):

    kapacita = 63
    naklady_za_km = 60

class IrisbusArwayShort (Vuz):

    kapacita = 43
    naklady_za_km = 40

class IrisbusArwayLong (Vuz):

    kapacita = 77
    naklady_za_km = 55

vozovy_park = [
    IrizaPB('1A11111'),
    IrizaPB('1A12222'),
    IrisbusArwayShort('1A13333'),
    IrisbusArwayLong('1A14444'),
]

def najit_vhodny_autobus(seznam_vozu, pozadovana_kapacita):
    vhodne_vozy = [vuz for vuz in seznam_vozu if vuz.kapacita >= pozadovana_kapacita]
    if not vhodne_vozy:
        return None
    return min(vhodne_vozy, key=lambda vuz: vuz.naklady_za_km)

assert najit_vhodny_autobus(vozovy_park, 60).spz == '1A14444'
