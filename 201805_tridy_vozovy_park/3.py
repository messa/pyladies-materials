# https://docs.google.com/document/d/1LTf2-077v4KF1LKgR6tUA68Z6iIHGz-qcLTrs7pF8Js/edit

'''
Uprav program tak, aby vozy ve vozovém parku měly různou kapacitu.
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

def secti_celkovou_kapacitu(seznam_vozu):
    celkova_kapacita = 0
    for vuz in seznam_vozu:
        celkova_kapacita = celkova_kapacita + vuz.kapacita
    return celkova_kapacita


assert secti_celkovou_kapacitu(vozovy_park) == 10 + 15 + 2 * 63 + 43 + 77
