# https://docs.google.com/document/d/1LTf2-077v4KF1LKgR6tUA68Z6iIHGz-qcLTrs7pF8Js/edit

class Vuz:
    def __init__(self):
        self.kapacita = 10

vozovy_park = [
    Vuz(),
    Vuz(),
    Vuz(),
]

def secti_celkovou_kapacitu(seznam_vozu):
    celkova_kapacita = 0
    for vuz in seznam_vozu:
        celkova_kapacita = celkova_kapacita + vuz.kapacita
    return celkova_kapacita


assert secti_celkovou_kapacitu(vozovy_park) == 30
