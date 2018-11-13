# Lekce 4, priklady 9.-13.
# https://projekty.pyladies.cz/lesson?course=pyladies-2018-praha-podzim-ntk&lesson=4-funkce-a-retezce


'''
9. Napiš funkci vyhodnot, která dostane řetězec s herním polem 1-D piškvorek a
vrátí jednoznakový řetězec podle stavu hry:

"x" – Vyhrál hráč s křížky (pole obsahuje "xxx")
"o" – Vyhrál hráč s kolečky (pole obsahuje "ooo")
"!" – Remíza (pole neobsahuje "-", a nikdo nevyhrál)
"-" – Ani jedna ze situací výše (t.j. hra ještě neskončila)
'''


def vyhodnot(herni_pole):
    if 'xxx' in herni_pole:
        return 'x'
    if 'ooo' in herni_pole:
        return 'o'
    if '-' not in herni_pole:
        return '!'
    return '-'


def test_vyhodnot():
    assert vyhodnot('----') == '-'
    assert vyhodnot('o---') == '-'
    assert vyhodnot('oo--') == '-'
    assert vyhodnot('ooo-') == 'o'
    assert vyhodnot('x---') == '-'
    assert vyhodnot('xx--') == '-'
    assert vyhodnot('xxx-') == 'x'
    assert vyhodnot('xoxo') == '!'


'''
10. Napiš funkci tah, která dostane řetězec s herním polem, číslo políčka (0-19),
a symbol (x nebo o) a vrátí herní pole (t.j. řetězec) s daným symbolem umístěným na danou pozici.

Hlavička funkce by tedy měla vypadat nějak takhle:

def tah(pole, cislo_policka, symbol):
    "Vrátí herní pole s daným symbolem umístěným na danou pozici"
    ...

Můžeš využít nějakou funkci, kterou jsme napsaly už na sraze?
'''


def tah(herni_pole, cislo_policka, symbol):
    return herni_pole[:cislo_policka] + symbol + herni_pole[cislo_policka+1:]


def test_tah_umisti_symbol():
    assert tah('----', 0, 'x') == 'x---'
    assert tah('----', 1, 'x') == '-x--'
    assert tah('----', 2, 'x') == '--x-'
    assert tah('----', 3, 'x') == '---x'
    assert tah('----', 0, 'o') == 'o---'
    # jeste vyzkousime neprazdne herni pole
    assert tah('xo-xo', 2, 'o') == 'xooxo'


'''
11. Napiš funkci tah_hrace, která dostane řetězec s herním polem, zeptá se hráče,
na kterou pozici chce hrát, a vrátí herní pole se zaznamenaným tahem hráče.
Funkce by měla odmítnout záporná nebo příliš velká čísla a tahy na obsazená políčka.
Pokud uživatel zadá špatný vstup, funkce mu vynadá a zeptá se znova.
'''


def tah_hrace(herni_pole):
    while True:
        pozice = input('Na ktere pozici chces hrat? ')
        if not pozice.isdigit():
            print('Zadej prosim cislo')
            continue
        pozice = int(pozice)
        if pozice < 1 or pozice > len(herni_pole):
            print(f'Zadej prosim cislo v rozsahu 1 - {len(herni_pole)}')
            continue
        pozice0 = pozice - 1 # ve zbytku programu indexujeme od nuly
        if herni_pole[pozice0] != '-':
            print('Toto policko je jiz obsazene')
            continue
        return tah(herni_pole, pozice0, 'x')


'''
12. Napiš funkci tah_pocitace, která dostane řetězec s herním polem, vybere pozici,
na kterou hrát, a vrátí herní pole se zaznamenaným tahem počítače.

Použij jednoduchou náhodnou „strategii”:

Vyber číslo od 0 do 19.
Pokud je dané políčko volné, hrej na něj.
Pokud ne, opakuj od bodu 1.
Hlavička funkce by tedy měla vypadat nějak takhle:

def tah_pocitace(pole):
    "Vrátí herní pole se zaznamenaným tahem počítače"
    ...
'''

from random import randrange


def tah_pocitace(herni_pole):
    cislo_policka = najdi_policko_pro_tah_pocitace(herni_pole)
    return tah(herni_pole, cislo_policka, 'o')


def najdi_policko_pro_tah_pocitace(herni_pole):
    if '-oo' in herni_pole:
        return herni_pole.index('-oo')
    if 'o-o' in herni_pole:
        return herni_pole.index('o-o') + 1
    if 'oo-' in herni_pole:
        return herni_pole.index('oo-') + 2
    return najdi_nahodne_volne_policko(herni_pole)


def najdi_nahodne_volne_policko(herni_pole):
    while True:
        nahodna_pozice = randrange(len(herni_pole))
        if herni_pole[nahodna_pozice] == '-':
            return nahodna_pozice


def test_tah_pocitace_udela_nejaky_nahodny_tah():
    herni_pole = tah_pocitace('---')
    assert herni_pole.count('-') == 2
    assert herni_pole.count('o') == 1


def test_tah_pocitace_udela_tah_do_jedineho_zbyvajiciho_policka():
    assert tah_pocitace('xx-xx') == 'xxoxx'


def test_tah_pocitace_dokonci_viteznou_sekvenci():
    assert tah_pocitace('---oo--') == '--ooo--'
    assert tah_pocitace('--o-o--') == '--ooo--'
    assert tah_pocitace('---oo--') == '--ooo--'


'''
13. Napiš funkci piskvorky1d, která vytvoří řetězec s herním polem a střídavě
volá funkce tah_hrace a tah_pocitace, dokud někdo nevyhraje nebo nedojde k remíze.

Nezapomeň kontrolovat stav hry po každém tahu.
'''


def piskvorky1d():
    herni_pole = 20 * '-'
    while True:
        print()
        print(herni_pole)
        print()
        herni_pole = tah_hrace(herni_pole)
        if vyhodnot(herni_pole) != '-':
            break
        herni_pole = tah_pocitace(herni_pole)
        if vyhodnot(herni_pole) != '-':
            break
    vysledek = vyhodnot(herni_pole)
    if vysledek == 'x':
        print('Vyhral hrac')
    if vysledek == 'o':
        print('Vyhral pocitac')
    if vysledek == '!':
        print('Remiza')


if __name__ == '__main__':
    piskvorky1d()
