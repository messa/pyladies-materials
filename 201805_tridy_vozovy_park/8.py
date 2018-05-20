# https://docs.google.com/document/d/1LTf2-077v4KF1LKgR6tUA68Z6iIHGz-qcLTrs7pF8Js/edit

'''
Ve vozovém parku jsou i hybridní vozy. To znamená, že určitou vzdálenost jedou
levně, dokud se nevybijí baterky, a pak jedou dál na naftu, ale o něco dráž.
Zkus to nějak zohlednit při výběru optimálního autobusu pro školní výlet :)
'''

class Vuz:

    def __init__(self, spz):
        self.spz = spz


class VuzNaNaftu (Vuz):

    def vzdalenost_je_ok(self, vzdalenost):
        return True

    def spocitej_naklady(self, vzdalenost):
        return vzdalenost * self.naklady_za_km


class IrizaPB (VuzNaNaftu):

    kapacita = 63
    naklady_za_km = 60


class IrisbusArwayShort (VuzNaNaftu):

    kapacita = 43
    naklady_za_km = 40


class IrisbusArwayLong (VuzNaNaftu):

    kapacita = 77
    naklady_za_km = 55


class VuzNaElektrinu (Vuz):

    def vzdalenost_je_ok(self, vzdalenost):
        return vzdalenost <= self.dojezd

    def spocitej_naklady(self, vzdalenost):
        return vzdalenost * self.naklady_za_km


class TeslaBus (VuzNaElektrinu):

    kapacita = 62
    naklady_za_km = 30
    dojezd = 150


class HybridniVuz (Vuz):

    def vzdalenost_je_ok(self, vzdalenost):
        return True

    def spocitej_naklady(self, vzdalenost):
        vzdalenost_elektrina = min(vzdalenost, self.dojezd_elektrina)
        vzdalenost_nafta = vzdalenost - vzdalenost_elektrina
        return vzdalenost_elektrina * self.naklady_za_km_elektrina + vzdalenost_nafta * self.naklady_za_km_nafta


class LeafBus (HybridniVuz):

    kapacita = 65
    naklady_za_km_elektrina = 35
    naklady_za_km_nafta = 65
    dojezd_elektrina = 80


vozovy_park = [
    IrizaPB('1A11111'),
    IrizaPB('1A12222'),
    IrisbusArwayShort('1A13333'),
    IrisbusArwayLong('1A14444'),
    TeslaBus('1A15555'),
    LeafBus('1A16666'),
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
    return min(vhodne_vozy, key=lambda vuz: vuz.spocitej_naklady(vzdalenost))

assert najit_vhodny_autobus(vozovy_park, 60, 250).spz == '1A14444'
assert najit_vhodny_autobus(vozovy_park, 60, 200).spz == '1A16666'
assert najit_vhodny_autobus(vozovy_park, 60, 100).spz == '1A15555'
