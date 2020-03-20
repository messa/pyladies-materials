Zápisky z on-line konzultace PyLadies 18. března 2020
=====================================================

if, elif
--------

```python
if a:
    ...
elif b:
    ...
elif c:
    ...
else:
    ...
```

Je to samé jako

```python
if a:
    ...
else:
    if b:
        ...
    else:
        if c:
            ...
        else:
            ...
```

Jakmile "to" do nějaké větve "spadne", tak další elify už se ani nekontrolují a běh programu pokračuje až za koncem toho celého if-elif-else.


Jednoduché vs. dvojité uvozovky
-------------------------------

```python
>>> print("Ahoj dvojita: \" jednoducha: ' ")
Ahoj dvojita: " jednoducha: '
>>> print('Ahoj dvojita: " jednoducha: \' ')
Ahoj dvojita: " jednoducha: '
>>>
>>>
>>> print("""Ahoj dvojita: " jednoducha: ' """)
Ahoj dvojita: " jednoducha: '
>>> print('''Ahoj dvojita: " jednoducha: ' ''')
Ahoj dvojita: " jednoducha: '
>>>
>>> ukazka = '''1
... 2
... 3'''
>>> print(ukazka)
1
2
3
```

https://naucse.python.cz/2019/pyladies-brno-podzim-st/beginners/str/


Vizualizace průběhu Python kódu
-------------------------------

http://pythontutor.com/visualize.html


Pořadí spouštění funkcí
-----------------------

```python
y = a(b(x))
```

Je ekvivalentní k

```python
mezivysledek = b(x)
y = a(mezivysledek)
```


Windows konzole
---------------

Jak kopírovat z/do Windows cmd: https://www.facebook.com/groups/1884194371898460/permalink/2535282723456285/

Alternativní konzole: [Cmder](https://cmder.net/)


Float vs. int
-------------

|          | int        | float           |
|----------|------------|-----------------|
| Co to je: | celé číslo | desetinné číslo |
| Anglicky: | integer | floating point number |
| Rozsah: | libovolně veliké kladné nebo záporné celé čislo | [IEEE-754 double precision](https://en.wikipedia.org/wiki/Double-precision_floating-point_format#IEEE_754_double-precision_binary_floating-point_format:_binary64) |

Neplatí, že by `float` byla nadmnožina `int`.
Existují čísla typu `int`, která nelze vyjádřit typem `float` (např. pokud jsou zcela mimo rozsah `float`). 

Dokumentace: [Floating Point Arithmetic: Issues and Limitations](https://docs.python.org/3.8/tutorial/floatingpoint.html)

Typ `float` slouží k vyjádření přibližné hodnoty hodně malých i hodně velkých čísel pro inženýrské účely.
Pro přesné vyjadřování desetinných čísel např. pro peněžní částky viz [Decimal](https://docs.python.org/3/library/decimal.html).

Další odkazy:

- https://realpython.com/python-data-types/

Jinak k zaokrouhlení čísel slouží funkce [round](https://docs.python.org/3/library/functions.html#round) (není ji ani potřeba odnikud importovat).


Formátování čísel
-----------------

```python
>>> cislo = 3.14159
>>> print(f'cislo je: {cislo} konec')
cislo je: 3.14159 konec
>>> print(f'cislo je: {cislo:.2f} konec')
cislo je: 3.14 konec
>>> print(f'cislo je: {cislo:7.2f} konec')
cislo je:    3.14 konec
>>> print(f'cislo je: {cislo:<7.2f} konec')
cislo je: 3.14    konec
```

https://naucse.python.cz/lessons/beginners/fstring/


Kámen nůžky papír
-----------------

```python
tah_cloveka = 'kamen'
tah_pocitace = 'papir'

if tah_cloveka == 'kamen':
    if tah_pocitace == 'kamen':
        print('Plichta')
    elif tah_pocitace == 'nuzky':
        print('Clovek vyhral')
    elif tah_pocitace == 'papir':
        print('Pocitac vyhral')
elif tah_cloveka == 'nuzky':
    if tah_pocitace == 'kamen':
        print('Pocitac vyhral')
    # ...
# ..

# To same, ale jinak strukturovane
if tah_cloveka == 'kamen' and tah_pocitace == 'kamen':
    print('Plichta')
elif tah_cloveka == 'kamen' and tah_pocitace == 'nuzky':
    print('Clovek vyhral')
elif tah_cloveka == 'kamen' and tah_pocitace == 'papir':
    print('Pocitac vyhral')
elif tah_cloveka == 'nuzky' and tah_pocitace == 'kamen':
    print('Pocitac vyhral')
# ...

# kazdy z moznych vysledku hry zachytim jednim dlouhym if-em
if (tah_cloveka == 'kamen' and tah_pocitace == 'papir') \
  or (tah_cloveka == 'nuzky' and tah_pocitace == 'kamen'):
    print('Pocitac vyhral')
elif zde_budou_podminky_pro_vyhru_cloveka:
    print('Clovek vyhral')
elif zde_budou_podminky_pro_plichtu:
    print('Plichta')

```


Přiřazení do více proměnných najednou
-------------------------------------

```python
>>> a, b = 1, 2
>>> print(a)
1
>>> print(b)
2
```

Toto se bude v kurzu ještě dělat později.



Dokumentace
-----------

Standardní knihovna Pythonu: https://docs.python.org/3/library/

Např. zde je přehled matematických funkcí: https://docs.python.org/3/library/math.html

[DevDocs.io](https://devdocs.io/) je stránka s rychlým vyhledáváním funkcí apod. v různých
programovacích jazycích a jejich knihovnách - viz např. https://devdocs.io/python~3.7/library/math#math.sqrt

Pokročilé materiály o Pythonu: https://naucse.python.cz/course/mi-pyt/


Funkce dir()
------------

Dokumentace: https://docs.python.org/3/library/functions.html#dir

```python
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']
>>> import math
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'math']
>>> dir(math)
['__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'pi', 'pow', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']
```


Curses
------

Curses je knihovna (nejen pro Python) pro "malování" v textovém terminálu.
Např. pohyb kurzoru nahoru, umisťování textu na specifickou pozici, simulace "okýnek"...

Jedná se o už dost pokročilé téma, mimo rámec tohoto kurzu.

Python: https://docs.python.org/3/howto/curses.html


Různé
-----

Pyvo :) https://pyvo.cz/praha-pyvo/

