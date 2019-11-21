CENA_BENZIN = 32.70
CENA_NAFTA = 32.20

vozy = [
    {'spz': 'AAA1111', 'palivo': 'benzin', 'spotreba': 6},
    {'spz': 'AAA2222', 'palivo': 'nafta', 'spotreba': 5},
]

def cena_za_km(vuz):
    if v['palivo'] == 'benzin':
        return v['spotreba'] * CENA_BENZIN * 0.01
    elif v['palivo'] == 'nafta':
        return v['spotreba'] * CENA_NAFTA * 0.01
    else:
        raise Exception('Neznamy typ vozu')

for v in vozy:
    print(v['spz'], cena_za_km(v))
