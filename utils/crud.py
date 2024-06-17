# crud dla pracownikow
def dodaj_pracownika(lista: list) -> None:
    imie = input("Podaj imie: ")
    nazwisko = input("Podaj nazwisko: ")
    stanowisko = input("Stanowisko: ")
    lokalizacja = input("Lokalizacja: ")
    nowy_pracownik = {"imie": imie, "nazwisko": nazwisko, "stanowisko": stanowisko,"lokalizacja": lokalizacja}
    lista.append(nowy_pracownik)


def usun_pracownika(pracownicy: list):
    imie = input("Podaj imię: ")
    for pracownik in pracownicy:
        if pracownik["imie"] == imie:
            pracownik.remove(pracownik)

def aktualizuj_pracownika(pracownicy: list):
    imie = input("Wprowadź imię użytkownika, którego dane chcesz zmienić:  ")
    for pracownik in pracownicy:
        if pracownik["imie"] == imie:
            pracownik["imie"] = input("Podaj nowe imię: ")
            pracownik["nazwisko"] = input("Podaj nowe nazwisko: ")
            pracownik["stanowisko"] = input("Podaj nowe stanowisko:  ")
            pracownik["lokalizacja"] = input("Podaj nową lokalizację:  ")

# crud dla jednostek
def dodaj_jednostke(lista: list) -> None:
    nazwa = input("Podaj nazwe: ")
    pracownik = input("Podaj pracownika: ")
    lokalizacja = input("Lokalizacja: ")
    nowa_jednostka = {"nazwa": nazwa, "pracownik": pracownik, "lokalizacja": lokalizacja}
    lista.append(nowa_jednostka )


def usun_jednostke(jednostki: list):
    nazwa = input("Podaj nazwe: ")
    for jednostka in jednostki:
        if jednostka["nazwa"] == nazwa:
            jednostka.remove(jednostka)

def aktualizuj_jednostke(jednostki: list):
    nazwa = input("Wprowadź nazwe jednostki, której dane chcesz zmienić:  ")
    for jednostka in jednostki:
        if jednostka["nazwa"] == nazwa:
            jednostka["nazwa"] = input("Podaj nową nazwe: ")
            jednostka["pracownik"] = input("Podaj nowego pracownika: ")
            jednostka["lokalizacja"] = input("Podaj nową lokalizacje:  ")

# crud dla pododdziałów
def dodaj_pododdzial(lista: list) -> None:
    nazwa = input("Podaj nazwe: ")
    nazwa_jednostki = input("Podaj nazwe jednostki: ")
    pracownik = input("Podaj pracownika: ")
    lokalizacja = input("Lokalizacja: ")
    nowa_pododdzial = {"nazwa": nazwa, "pracownik": pracownik, "nazwa_jednostki": nazwa_jednostki, "lokalizacja": lokalizacja}
    lista.append(nowa_pododdzial)


def usun_pododdzial(pododdzialy: list):
    nazwa = input("Podaj nazwe: ")
    for pododdzial in pododdzialy:
        if pododdzial["nazwa"] == nazwa:
            pododdzial.remove(pododdzialy)

def aktualizuj_pododdzial(pododdzialy: list):
    nazwa = input("Wprowadź nazwe pododdziału, którego dane chcesz zmienić:  ")
    for pododdzial in pododdzialy:
        if pododdzial["nazwa"] == nazwa:
            pododdzial["nazwa"] = input("Podaj nową nazwe: ")
            pododdzial["nazwa_jednostki"] = input("Podaj nową nazwe jednostki: ")
            pododdzial["pracownik"] = input("Podaj nowego pracownika: ")
            pododdzial["lokalizacja"] = input("Podaj nową lokalizacje:  ")




