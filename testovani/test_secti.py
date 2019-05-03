from scitani import secti
import pytest

def test_jedna():
    pass

def test_secti_tri_a_pet():
    vysledek = secti(3, 5)
    if vysledek != 8:
        raise AssertionError('Nefunguje to')

    #vysledek = secti(0, -1)
    #if vysledek != -1:
    #    raise AssertionError('Nefunguje to')
    assert secti(0, -1) == -1
    assert secti(0, -1) == -1, 'Nefunguje to'

def test_secti_cislo_a_retezec():
    try:
        secti(10, 'x')
    except TypeError:
        pass
    else:
        assert False, 'melo to vyhodit TypeError'

def test_secti_cislo_a_retezec_2():
    with pytest.raises(TypeError):
        secti(10, 'x')

def test_tri():
    pass
