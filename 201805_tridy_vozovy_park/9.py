# https://docs.google.com/document/d/1LTf2-077v4KF1LKgR6tUA68Z6iIHGz-qcLTrs7pF8Js/edit

'''
Zkus program upravit tak, aby v něm cena paliva (nafty, elektřiny...) nebyla
pevně zabudovaná, ale aby šla zadat při běhu programu.
'''

class Vuz:

    def __init__(self, spz):
        self.spz = spz


class VuzNaNaftu (Vuz):

    def vzdalenost_je_ok(self, vzdalenost):
        return True

    def spocitej_naklady(self, vzdalenost, cenik):
        return vzdalenost * self.spotreba_za_km * cenik['nafta']


class IrizaPB (VuzNaNaftu):

    kapacita = 63
    spotreba_za_km = 2


class IrisbusArwayShort (VuzNaNaftu):

    kapacita = 43
    spotreba_za_km = 1.333


class IrisbusArwayLong (VuzNaNaftu):

    kapacita = 77
    spotreba_za_km = 1.833


class VuzNaElektrinu (Vuz):

    def vzdalenost_je_ok(self, vzdalenost):
        return vzdalenost <= self.dojezd

    def spocitej_naklady(self, vzdalenost, cenik):
        return vzdalenost * self.spotreba_za_km * cenik['elektrina']


class TeslaBus (VuzNaElektrinu):

    kapacita = 62
    spotreba_za_km = 0.6
    dojezd = 150


class HybridniVuz (Vuz):

    def vzdalenost_je_ok(self, vzdalenost):
        return True

    def spocitej_naklady(self, vzdalenost, cenik):
        vzdalenost_elektrina = min(vzdalenost, self.dojezd_elektrina)
        vzdalenost_nafta = vzdalenost - vzdalenost_elektrina
        return vzdalenost_elektrina * self.spotreba_za_km_elektrina * cenik['elektrina'] \
            + vzdalenost_nafta * self.spotreba_za_km_nafta * cenik['nafta']


class LeafBus (HybridniVuz):

    kapacita = 65
    spotreba_za_km_elektrina = 0.7
    spotreba_za_km_nafta = 2.166
    dojezd_elektrina = 80


vozovy_park = [
    IrizaPB('1A11111'),
    IrizaPB('1A12222'),
    IrisbusArwayShort('1A13333'),
    IrisbusArwayLong('1A14444'),
    TeslaBus('1A15555'),
    LeafBus('1A16666'),
]

def najit_vhodny_autobus(seznam_vozu, pozadovana_kapacita, vzdalenost, cenik):
    vhodne_vozy = []
    for vuz in seznam_vozu:
        if vuz.kapacita < pozadovana_kapacita:
            continue
        if not vuz.vzdalenost_je_ok(vzdalenost):
            continue
        vhodne_vozy.append(vuz)
    if not vhodne_vozy:
        return None
    return min(vhodne_vozy, key=lambda vuz: vuz.spocitej_naklady(vzdalenost, cenik))

cenik = {
    'nafta': 30,
    'elektrina': 50,
}

assert najit_vhodny_autobus(vozovy_park, 60, 250, cenik).spz == '1A14444'
assert najit_vhodny_autobus(vozovy_park, 60, 200, cenik).spz == '1A16666'
assert najit_vhodny_autobus(vozovy_park, 60, 100, cenik).spz == '1A15555'
