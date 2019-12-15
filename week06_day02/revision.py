class Obywatel:
    class AdresZameldowania:
        def __init__(self, kod_pocztowy, miejscowosc, ulica, numer_domu, numer_mieszkania):
            self.kod_pocztowy = kod_pocztowy
            self.miejscowosc = miejscowosc
            self.ulica = ulica
            self.numer_domu = numer_domu
            self.numer_mieszkania = numer_mieszkania

        def __repr__(self):
            return f'Adres Zameldowania: {self.miejscowosc}: {self.kod_pocztowy},\n ulica: {self.ulica}, ' \
                   f'dom nr.{self.numer_domu}, mieszkanie nr.{self.numer_mieszkania}'

    def __init__(self, imie, nazwisko, adres_zameldowania):
        self.imie = imie
        self.nazwisko = nazwisko
        self.adres_zameldowania = adres_zameldowania

    def __repr__(self):
        return f'{self.imie} {self.nazwisko},\n{self.adres_zameldowania}'


if __name__ == '__main__':
    jan = Obywatel("Jan", "Kowalski", Obywatel.AdresZameldowania('32-323', 'Krakow', 'Cicha', '123', '2'))
    print(jan)
