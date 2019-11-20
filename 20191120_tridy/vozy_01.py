CENA_BENZIN = 32.70
CENA_NAFTA = 32.20

vozy = [
    {'spz': 'AAA1111', 'palivo': 'benzin', 'spotreba': 6},
    {'spz': 'AAA2222', 'palivo': 'nafta', 'spotreba': 5},
]

for v in vozy:
    cena_za_km = '???'
    print(v['spz'], cena_za_km)

