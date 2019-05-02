from random import randint

def main(input=input, print=print):
    cislo = randint(1, 20)
    print('Zvolil jsem si cislo od 1 do 20 (vcetne), zkus ho uhadnout!')

    while True:
        tip = input('Tvuj tip? ')
        tip = int(tip)
        if tip == cislo:
            print('Uhadl jsi!')
            break
        elif tip < cislo:
            print('Moc nizko')
        else:
            print('Moc vysoko')

if __name__ == '__main__':
    main()
