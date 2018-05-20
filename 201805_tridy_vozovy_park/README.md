Zadání
======

1. Vytvoř si (prozatím) jednoduchý program, který reprezentuje vozový park fiktivního dopravního podniku - mohl by vypadat nějak takto:

    ```python
    class Vuz:
        def __init__(self):
            self.kapacita = 10

    vozovy_park = [
        Vuz(),
        Vuz(),
        Vuz(),
    ]
    ```

2. Vytvoř funkci, která __spočítá celkovou kapacitu všech vozů ve vozovém parku__ - mohla by vypadat např. takto:

    ```python
    def secti_celkovou_kapacitu(seznam_vozu):
        celkova_kapacita = 0
        for vuz in seznam_vozu:
            celkova_kapacita = celkova_kapacita + vuz.kapacita
        return celkova_kapacita
    ```

3. Uprav program tak, aby __vozy ve vozovém parku měly různou kapacitu__. Kód v bodě 1. je jen ukázka, můžeš to udělat klidně i úplně jinak :)

4. To byla jen rozcvička, teď už bez napovídání :) __Vytvoř (další) funkci__, které lze zadat požadovanou minimální kapacitu, a ta funkce __najde vůz__, který má tuto nebo vyšší __kapacitu__. Například: školní výlet si potřebuje objednat autobus pro 20 lidí a my chceme nějaký takový ve vozovém parku najít. Zavolej tuto funkci a vypiš její výsledek (návratovou hodnotu).

5. Zřejmě by bylo fajn vozy nějak jednoznačně identifikovat - přidej jim __atribut `spz`__. Uprav program z předchozího bodu, aby vypisoval SPZ nalezeného vozu.

6. Každý vůz má jiné __náklady za kilometr__. Zkus toto v programu nějak zohlednit - ideálně aby funkce, která hledá autobus pro ten školní výlet, našla co __nejekonomičtější variantu__.

    (Pro jednoduchost budeme počítat s tím, že i kdyby autobus musel tankovat po cestě, tak cena dotyčného druhu paliva bude vždy a všude stejná.)

7. Ve vozovém parku jsou různé druhy vozů - na __naftu a elektřinu__. Autobus na elektřinu bude zřejmě nejlevnější varianta, ale asi jím nechceme poslat školu na školní výlet, pokud by vzdálenost byla delší, než __dojezd autobusu__, protože autobus by se musel po cestě na několik hodin zastavit kvůli nabití. Naopak zastavit s autobusem na naftu kvůli tankování nafty není problém. Zkus to zohlednit v té funkci, která hledá optimální autobus pro školní výlet. (Zřejmě bude potřeba přidat argument, jak dlouhý ten výlet bude.)

8. Ve vozovém parku jsou i __hybridní vozy__. To znamená, že určitou vzdálenost jedou levně, dokud se nevybijí baterky, a pak jedou dál na naftu, ale o něco dráž. Zkus to nějak zohlednit při výběru optimálního autobusu pro školní výlet :)

9. Zkus program upravit tak, aby v něm __cena paliva__ (nafty, elektřiny...) nebyla pevně zabudovaná, ale aby šla zadat při běhu programu.
