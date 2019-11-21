CENA_BENZIN = 32.70
CENA_NAFTA = 32.20


class VuzNaBenzin:

    def __init__(self, spz, spotreba):
        self.spz = spz
        self.spotreba = spotreba

    def cena_za_km(self):
        return self.spotreba * CENA_BENZIN * 0.01


class VuzNaNaftu:

    # ...


vozy = [
    VuzNaBenzin('AAA1111', 6),
    VuzNaNaftu('AAA2222', 5),
]

for v in vozy:
    print(v.spz, v.cena_za_km())
