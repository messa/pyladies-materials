from hadej_upraveno import vyhodnot

def test_vyhodnot_trefa():
    assert vyhodnot('5', 5) == ('Uhodl jsi!', True)

def test_vyhodnot_nizko():
    assert vyhodnot('-1', 5) == ('Moc nizko', False)
    assert vyhodnot('0', 5) == ('Moc nizko', False)
    assert vyhodnot('1', 5) == ('Moc nizko', False)
    assert vyhodnot('2', 5) == ('Moc nizko', False)
    assert vyhodnot('4', 5) == ('Moc nizko', False)

def test_vyhodnot_vysoko():
    assert vyhodnot('6', 5) == ('Moc vysoko', False)
    assert vyhodnot('9999', 5) == ('Moc vysoko', False)

def test_vyhodnot_neplatny_typ():
    assert vyhodnot('', 5) == ('Zadej prosim cele cislo', False)
    assert vyhodnot('asdf', 5) == ('Zadej prosim cele cislo', False)
    assert vyhodnot('3.14', 5) == ('Zadej prosim cele cislo', False)
