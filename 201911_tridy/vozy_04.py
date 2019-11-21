CENA_BENZIN = 32.70
CENA_NAFTA = 32.20

def cena_za_km_benzin(vuz):
    return v['spotreba'] * CENA_BENZIN * 0.01

def cena_za_km_nafta(vuz):
    return v['spotreba'] * CENA_NAFTA * 0.01

vozy = [
    {'spz': 'AAA1111', 'spotreba': 6, 'cena_za_km': cena_za_km_benzin},
    {'spz': 'AAA2222', 'spotreba': 5, 'cena_za_km': cena_za_km_nafta},
]

for v in vozy:
    print(v['spz'], v['cena_za_km'](v))
