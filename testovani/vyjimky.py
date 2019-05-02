def f1():
    print('f1 A')
    try:
        return 10
        f2()
    except ZeroDivisionError:
        print('Delit nulou neumim')
    except Exception:
        print('Stala se nejaka chyba')
    else:
        print('OK')
    finally:
        print('Toto se vypise pokazde')
    print('f1 B')


def f2():
    print('f2 A')
    print(1 / 0)
    #raise Exception('Chyba')
    print('f2 B')


f1()
