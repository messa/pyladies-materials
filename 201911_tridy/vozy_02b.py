CENA_BENZIN = 32.70
CENA_NAFTA = 32.20

vozy = [
    {'spz': 'AAA1111', 'palivo': 'benzin', 'spotreba': 6},
    {'spz': 'AAA2222', 'palivo': 'nafta', 'spotreba': 5},
]

for v in vozy:
    if v['palivo'] == 'benzin':
        cena_za_km = v['spotreba'] * CENA_BENZIN * 0.01
    elif v['palivo'] == 'nafta':
        cena_za_km = v['spotreba'] * CENA_NAFTA * 0.01
    else:
        raise Exception('Neznamy typ vozu')
    print(v['spz'], cena_za_km)
