a = input('zadej delenec: ')
b = input('zadej delitel: ')

try:
    print(int(a) / int(b))
except ZeroDivisionError:
    print('Delitel nesmi byt nula')
except ValueError:
    print('Zadej prosim cisla')
except Exception:
    print('Nejaka jina chyba')
else:
    print('Vse probehlo OK')
finally:
    print('Toto se vypise vzdy')
