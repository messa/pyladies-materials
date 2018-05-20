# https://docs.google.com/document/d/1LTf2-077v4KF1LKgR6tUA68Z6iIHGz-qcLTrs7pF8Js/edit

'''
Zřejmě by bylo fajn vozy nějak jednoznačně identifikovat - přidej jim atribut spz.
Uprav program z předchozího bodu, aby vypisoval SPZ nalezeného vozu.
'''

class IrizaPB:

    def __init__(self, spz):
        self.spz = spz
        self.kapacita = 63

class IrisbusArwayShort:

    def __init__(self, spz):
        self.spz = spz
        self.kapacita = 43

class IrisbusArwayLong:

    def __init__(self, spz):
        self.spz = spz
        self.kapacita = 77

vozovy_park = [
    IrizaPB('1A11111'),
    IrizaPB('1A12222'),
    IrisbusArwayShort('1A13333'),
    IrisbusArwayLong('1A14444'),
]

def najit_vhodny_autobus(seznam_vozu, pozadovana_kapacita):
    for vuz in seznam_vozu:
        if vuz.kapacita >= pozadovana_kapacita:
            return vuz
    return None

assert najit_vhodny_autobus(vozovy_park, 60).spz in ['1A11111', '1A12222']
