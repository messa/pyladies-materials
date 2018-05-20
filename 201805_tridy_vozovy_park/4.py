# https://docs.google.com/document/d/1LTf2-077v4KF1LKgR6tUA68Z6iIHGz-qcLTrs7pF8Js/edit

'''
Vytvoř (další) funkci, které lze zadat požadovanou minimální kapacitu, a ta
funkce najde vůz, který má tuto nebo vyšší kapacitu.
Například: školní výlet si potřebuje objednat autobus pro 20 lidí a my chceme
nějaký takový ve vozovém parku najít. Zavolej tuto funkci a vypiš její
výsledek (návratovou hodnotu).
'''

class Vuz:

    def __init__(self, kapacita):
        self.kapacita = kapacita

class IrizaPB:

    def __init__(self):
        self.kapacita = 63

class IrisbusArwayShort:

    def __init__(self):
        self.kapacita = 43

class IrisbusArwayLong:

    def __init__(self):
        self.kapacita = 77

vozovy_park = [
    Vuz(10),
    Vuz(15),
    IrizaPB(),
    IrizaPB(),
    IrisbusArwayShort(),
    IrisbusArwayLong(),
]

def najit_vhodny_autobus(seznam_vozu, pozadovana_kapacita):
    for vuz in seznam_vozu:
        if vuz.kapacita >= pozadovana_kapacita:
            return vuz
    return None

assert najit_vhodny_autobus(vozovy_park, 50).kapacita >= 50
