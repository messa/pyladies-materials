CENA_BENZIN = 32.70
CENA_NAFTA = 32.20


class VuzNaBenzin:

    def __init__(vuz, spz, spotreba):
        vuz.spz = spz
        vuz.spotreba = spotreba

    def cena_za_km(vuz):
        return vuz.spotreba * CENA_BENZIN * 0.01


class VuzNaNaftu:

    def __init__(vuz, spz, spotreba):
        vuz.spz = spz
        vuz.spotreba = spotreba

    def cena_za_km(vuz):
        return vuz.spotreba * CENA_NAFTA * 0.01


vozy = [
    VuzNaBenzin('AAA1111', 6),
    VuzNaNaftu('AAA2222', 5),
]

for v in vozy:
    print(v.spz, v.cena_za_km())
