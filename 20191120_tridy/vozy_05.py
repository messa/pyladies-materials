CENA_BENZIN = 32.70
CENA_NAFTA = 32.20

def cena_za_km_benzin(vuz):
    return vuz['spotreba'] * CENA_BENZIN * 0.01

def cena_za_km_nafta(vuz):
    return vuz['spotreba'] * CENA_NAFTA * 0.01

def init_vuz_benzin(spz, spotreba):
    return {
        'spz': spz,
        'spotreba': spotreba,
        'cena_za_km': cena_za_km_benzin,
    }

def init_vuz_nafta(spz, spotreba):
    return {
        'spz': spz,
        'spotreba': spotreba,
        'cena_za_km': cena_za_km_nafta,
    }

vozy = [
    init_vuz_benzin('AAA1111', 6),
    init_vuz_nafta('AAA2222', 5),
]

for v in vozy:
    print(v['spz'], v['cena_za_km'](v))
