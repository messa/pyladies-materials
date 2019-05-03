'''
"Hádání čísel" - snadno testovatelhá verze.
Testy jsou v test_hadej_upraveno.py.
'''

from random import randint

def main():
    cislo = randint(1, 20)
    print('Zvolil jsem si cislo od 1 do 20 (vcetne), zkus ho uhadnout!')
    while True:
        tip = input('Tvuj tip? ')
        zprava, konec = vyhodnot(tip, cislo)
        print(zprava)
        if konec:
            break

def vyhodnot(tip, cislo):
    '''
    Vrací tuple (zprava, konec).
    Hodnota konec=True znamená, že by se program měl ukončit.
    '''
    tip = int(tip)
    konec = False
    if tip == cislo:
        zprava = 'Uhodl jsi!'
        konec = True
    elif tip < cislo:
        zprava = 'Moc nizko'
    else:
        zprava = 'Moc vysoko'
    return zprava, konec

if __name__ == '__main__':
    main()
    # https://stackoverflow.com/questions/419163/what-does-if-name-main-do
