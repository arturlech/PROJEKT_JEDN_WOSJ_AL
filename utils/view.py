from tkinter import *
import requests
import tkintermapview
from bs4 import BeautifulSoup
from tkinter import messagebox

login_data = {

    "Artur": "Pracownik1",
    "Zuzanna": "Pracownik2",
    "Kamil": "Pracownik3",
    "Mateusz": "Pracownik4",
    "Mariusz": "Pracownik5",
    "Wojciech": "Pracownik6",
    "Kacper": "Pracownik7",
    "Andrzej": "Pracownik8",
    "Konrad": "Pracownik9",
    "Martyna": "Pracownik10"
}



class Pracownik:
    def __init__(self, imie, nazwisko, stanowisko, lokalizacja):
        self.imie = imie
        self.nazwisko = nazwisko
        self.stanowisko = stanowisko
        self.lokalizacja = lokalizacja
        self.wspolrzedne = self.pobierz_wspolrzedne()
        self.marker = None

    def pobierz_wspolrzedne(self) -> list:
        url = f'https://pl.wikipedia.org/wiki/{self.lokalizacja}'
        response = requests.get(url)
        response_html = BeautifulSoup(response.text, 'html.parser')
        return [
            float(response_html.select('.latitude')[1].text.replace(",", ".")),
            float(response_html.select('.longitude')[1].text.replace(",", "."))
        ]

    def usun_marker(self):
        if self.marker:
            self.marker.delete()
            self.marker = None

pracownicy = [
    Pracownik("Artur", "Lech", "Dowódca", "Warszawa"),
    Pracownik("Kamil", "Bednarek", "Oficer", "Grudziądz"),
    Pracownik("Karol", "Mastek", "Dowódca kampanii", "Olsztyn"),
    Pracownik("Julian", "Kochanek", "Radiooperator", "Toruń"),
    Pracownik("Zuzanna", "Orkisz", "Kapral", "Lublin"),
    Pracownik("Kacper", "Trzcina", "Dowódca", "Szczecin"),
    Pracownik("Katarzyna", "Figura", "Kierowca", "Gorzów Wielkopolski"),
    Pracownik("Tomasz", "Karolak", "Strzelec wyborowy", "Zielona Góra"),
    Pracownik("Konrad", "Kowaliski", "Podoficer", "Poznań"),
    Pracownik("Wojciech", "Michalak", "Podporucznik", "Opole"),
    Pracownik("Michał", "Makowski", "Sanitariusz", "Częstochowa"),
    Pracownik("Kinga", "Bartoszewska", "Strzelec", "Wrocław"),
    Pracownik("Andrzej", "Iwniak", "Podoficer", "Kielce"),
    Pracownik("Mateusz", "Skrzypczak", "Chorąży", "Siedlce"),
    Pracownik("Mirosław", "Kowal", "Starszy sierżant kompani", "Kraków"),
    Pracownik("Mateusz", "Kiper", "Oficer Łączności", "Białystok"),
    Pracownik("Mariusz", "Piotruk", "Sierżant", "Bydgoszcz"),
    Pracownik("Martyna", "Tupikowska", "Dowódca", "Tarnów"),
    Pracownik("Mariusz", "Pierożek", "Celowniczy", "Gdańsk"),
    Pracownik("Leon", "Seat", "Oficer medyczny", "Zamość")
]
def lista_uzytkownikow(listbox_lista_pracownikow, map_widget):
    listbox_lista_pracownikow.delete(0, END)
    for idx, pracownik in enumerate(pracownicy):
        listbox_lista_pracownikow.insert(idx,
                                         f'{pracownik.imie} {pracownik.nazwisko} {pracownik.stanowisko} {pracownik.lokalizacja}')
        pracownik.marker = map_widget.set_marker(pracownik.wspolrzedne[0], pracownik.wspolrzedne[1],
                                                 text=f"{pracownik.nazwisko}")


def dodaj_uzytkownika(entry_imie, entry_nazwisko, entry_stanowisko, entry_lokalizacja, listbox_lista_pracownikow,
                      map_widget):
    imie = entry_imie.get()
    nazwisko = entry_nazwisko.get()
    stanowisko = entry_stanowisko.get()
    lokalizacja = entry_lokalizacja.get()
    pracownicy.append(Pracownik(imie, nazwisko, stanowisko, lokalizacja))
    lista_uzytkownikow(listbox_lista_pracownikow, map_widget)

    entry_imie.delete(0, END)
    entry_nazwisko.delete(0, END)
    entry_stanowisko.delete(0, END)
    entry_lokalizacja.delete(0, END)
    entry_imie.focus()


def usun_uzytkownika(listbox_lista_pracownikow, map_widget):
    i = listbox_lista_pracownikow.curselection()[0]
    pracownicy[i].usun_marker()
    pracownicy.pop(i)
    lista_uzytkownikow(listbox_lista_pracownikow, map_widget)


def pokaz_szczegoly_uzytkownikow(listbox_lista_pracownikow, label_imie_szczegoly_obiektu_wartosc,
                                 label_nazwisko_szczegoly_obiektu_wartosc, label_stanowisko_szczegoly_obiektu_wartosc,
                                 label_lokalizacja_szczegoly_obiektu_wartosc, map_widget):
    i = listbox_lista_pracownikow.curselection()[0]
    pracownik = pracownicy[i]
    label_imie_szczegoly_obiektu_wartosc.config(text=pracownik.imie)
    label_nazwisko_szczegoly_obiektu_wartosc.config(text=pracownik.nazwisko)
    label_stanowisko_szczegoly_obiektu_wartosc.config(text=pracownik.stanowisko)
    label_lokalizacja_szczegoly_obiektu_wartosc.config(text=pracownik.lokalizacja)
    map_widget.set_position(pracownik.wspolrzedne[0], pracownik.wspolrzedne[1])
    map_widget.set_zoom(12)


def edytuj_uzytkownika(listbox_lista_pracownikow, entry_imie, entry_nazwisko, entry_stanowisko, entry_lokalizacja,
                       button_dodaj_uzytkownika, map_widget):
    i = listbox_lista_pracownikow.curselection()[0]
    pracownik = pracownicy[i]
    pracownik.usun_marker()
    entry_imie.delete(0, END)
    entry_nazwisko.delete(0, END)
    entry_stanowisko.delete(0, END)
    entry_lokalizacja.delete(0, END)

    entry_imie.insert(0, pracownik.imie)
    entry_nazwisko.insert(0, pracownik.nazwisko)
    entry_stanowisko.insert(0, pracownik.stanowisko)
    entry_lokalizacja.insert(0, pracownik.lokalizacja)

    button_dodaj_uzytkownika.config(text="Zapisz zmiany",
                                    command=lambda: aktualizuj_uzytkownika(i, entry_imie, entry_nazwisko,
                                                                           entry_stanowisko, entry_lokalizacja,
                                                                           button_dodaj_uzytkownika,
                                                                           listbox_lista_pracownikow, map_widget))


def aktualizuj_uzytkownika(i, entry_imie, entry_nazwisko, entry_stanowisko, entry_lokalizacja, button_dodaj_uzytkownika,
                           listbox_lista_pracownikow, map_widget):
    pracownik = pracownicy[i]
    pracownik.imie = entry_imie.get()
    pracownik.nazwisko = entry_nazwisko.get()
    pracownik.stanowisko = entry_stanowisko.get()
    pracownik.lokalizacja = entry_lokalizacja.get()
    pracownik.wspolrzedne = pracownik.pobierz_wspolrzedne()
    lista_uzytkownikow(listbox_lista_pracownikow, map_widget)
    button_dodaj_uzytkownika.config(text="Dodaj pracownika",
                                    command=lambda: dodaj_uzytkownika(entry_imie, entry_nazwisko,
                                                                      entry_stanowisko, entry_lokalizacja,
                                                                      listbox_lista_pracownikow, map_widget))

    entry_imie.delete(0, END)
    entry_nazwisko.delete(0, END)
    entry_stanowisko.delete(0, END)
    entry_lokalizacja.delete(0, END)
    entry_imie.focus()


def tworzenie_pracownicy_root(root):
    global map_widget
    pracownicy_root = Toplevel(root)
    pracownicy_root.title("Pracownicy")
    pracownicy_root.geometry("1100x724")

    # ramki do porządkowania struktury
    ramka_lista_pracownikow = Frame(pracownicy_root)
    ramka_formularz = Frame(pracownicy_root)
    ramka_szczegoly_obiektu = Frame(pracownicy_root)

    ramka_lista_pracownikow.grid(row=0, column=0, padx=50)
    ramka_formularz.grid(row=0, column=1)
    ramka_szczegoly_obiektu.grid(row=1, column=0, columnspan=2)

    # lista_pracownikow
    label_lista_pracownikow = Label(ramka_lista_pracownikow, text="Lista pracowników: ")
    listbox_lista_pracownikow = Listbox(ramka_lista_pracownikow, width=100)
    button_pokaz_szczegoly = Button(ramka_lista_pracownikow, text="Pokaż szczegóły",
                                    command=lambda: pokaz_szczegoly_uzytkownikow(listbox_lista_pracownikow,
                                                                                 label_imie_szczegoly_obiektu_wartosc,
                                                                                 label_nazwisko_szczegoly_obiektu_wartosc,
                                                                                 label_stanowisko_szczegoly_obiektu_wartosc,
                                                                                 label_lokalizacja_szczegoly_obiektu_wartosc,
                                                                                 map_widget))
    button_usun_obiekt = Button(ramka_lista_pracownikow, text='Usuń obiekt',
                                command=lambda: usun_uzytkownika(listbox_lista_pracownikow, map_widget))
    button_edytuj_obiektu = Button(ramka_lista_pracownikow, text='Edytuj obiekt',
                                   command=lambda: edytuj_uzytkownika(listbox_lista_pracownikow, entry_imie,
                                                                      entry_nazwisko, entry_stanowisko,
                                                                      entry_lokalizacja, button_dodaj_uzytkownika,
                                                                      map_widget))

    label_lista_pracownikow.grid(row=0, column=0, columnspan=3)
    listbox_lista_pracownikow.grid(row=1, column=0, columnspan=3)
    button_pokaz_szczegoly.grid(row=2, column=0)
    button_usun_obiekt.grid(row=2, column=1)
    button_edytuj_obiektu.grid(row=2, column=2)

    # formularz
    label_formularz = Label(ramka_formularz, text="Formularz")
    label_imie = Label(ramka_formularz, text="Imię: ")
    label_nazwisko = Label(ramka_formularz, text="Nazwisko: ")
    label_stanowisko = Label(ramka_formularz, text="Stanowisko: ")
    label_lokalizacja = Label(ramka_formularz, text="Miejsce zamieszkania: ")

    entry_imie = Entry(ramka_formularz)
    entry_nazwisko = Entry(ramka_formularz)
    entry_stanowisko = Entry(ramka_formularz)
    entry_lokalizacja = Entry(ramka_formularz)

    label_formularz.grid(row=0, column=0, columnspan=2)
    label_imie.grid(row=1, column=0, sticky=W)
    label_nazwisko.grid(row=2, column=0, sticky=W)
    label_stanowisko.grid(row=3, column=0, sticky=W)
    label_lokalizacja.grid(row=4, column=0, sticky=W)

    entry_imie.grid(row=1, column=1)
    entry_nazwisko.grid(row=2, column=1)
    entry_stanowisko.grid(row=3, column=1)
    entry_lokalizacja.grid(row=4, column=1)

    button_dodaj_uzytkownika = Button(ramka_formularz, text="Dodaj pracownika",
                                      command=lambda: dodaj_uzytkownika(entry_imie, entry_nazwisko, entry_stanowisko,
                                                                        entry_lokalizacja, listbox_lista_pracownikow,
                                                                        map_widget))
    button_dodaj_uzytkownika.grid(row=5, column=1, columnspan=2)

    # szczegoly obiektu
    label_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text="Szczegóły pracownika: ")
    label_imie_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text="Imię: ")
    label_nazwisko_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text="Nazwisko: ")
    label_stanowisko_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text="Stanowisko: ")
    label_lokalizacja_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text="Miejsce zamieszkania: ")

    label_imie_szczegoly_obiektu_wartosc = Label(ramka_szczegoly_obiektu, text="...")
    label_nazwisko_szczegoly_obiektu_wartosc = Label(ramka_szczegoly_obiektu, text="...")
    label_stanowisko_szczegoly_obiektu_wartosc = Label(ramka_szczegoly_obiektu, text="...")
    label_lokalizacja_szczegoly_obiektu_wartosc = Label(ramka_szczegoly_obiektu, text="...")

    label_szczegoly_obiektu.grid(row=0, column=0, sticky=W)
    label_imie_szczegoly_obiektu.grid(row=1, column=0, sticky=W)
    label_imie_szczegoly_obiektu_wartosc.grid(row=1, column=1)
    label_nazwisko_szczegoly_obiektu.grid(row=1, column=2)
    label_nazwisko_szczegoly_obiektu_wartosc.grid(row=1, column=3)
    label_stanowisko_szczegoly_obiektu.grid(row=1, column=4)
    label_stanowisko_szczegoly_obiektu_wartosc.grid(row=1, column=5)
    label_lokalizacja_szczegoly_obiektu.grid(row=1, column=6)
    label_lokalizacja_szczegoly_obiektu_wartosc.grid(row=1, column=7)
    global map_widget
    map_widget = tkintermapview.TkinterMapView(ramka_szczegoly_obiektu, width=900, height=400)
    map_widget.set_position(52.2, 21)
    map_widget.set_zoom(8)
    map_widget.grid(row=2, column=0, columnspan=8)

    lista_uzytkownikow(listbox_lista_pracownikow, map_widget)


class Jednostka:
    def __init__(self, nazwa, pracownicy, lokalizacja_jednostek):
        self.nazwa = nazwa
        self.pracownicy = pracownicy
        self.lokalizacja_jednostek = lokalizacja_jednostek
        self.wspolrzedne = self.pobierz_wspolrzedne()
        self.marker = None

    def pobierz_wspolrzedne(self) -> list:
        url = f'https://pl.wikipedia.org/wiki/{self.lokalizacja_jednostek}'
        response = requests.get(url)
        response_html = BeautifulSoup(response.text, 'html.parser')
        return [
            float(response_html.select('.latitude')[1].text.replace(",", ".")),
            float(response_html.select('.longitude')[1].text.replace(",", "."))
        ]

    def usun_marker(self):
        if self.marker:
            self.marker.delete()
            self.marker = None

jednostki = [
    Jednostka("Sztab Generalny Wojska Polskiego", "Artur Lech", "Warszawa"),
    Jednostka("2 Lubelska Brygada Obrony Terytorialnej", "Zuzanna Orkisz", "Lublin"),
    Jednostka("Wojskowa Komeda Uzupełnień w Szczecinie", "Kacper Trzcina", "Szczecin"),
    Jednostka("2 Skrzydło Lotnictwa Taktycznego", "Konrad Kowaliski", "Poznań"),
    Jednostka("Wojskowa Komeda Uzupełnień we Wrocławiu", "Kinga Bartoszewska", "Wrocław"),
    Jednostka("Wojskowa Komeda Uzupełnień w Białymstoku", "Mateusz Kiper", "Białystok"),
    Jednostka("10 Świętokrzyska Brygada Obrony Terytorialnej", "Andrzej Iwaniak", "Kielce"),
    Jednostka("Jednostka Wojskowa NIL", "Mirosław Kowal", "Kraków"),
    Jednostka("Wojskowa Komeda Uzupełnień w Gdańsku", "Mateusz Skrzypczak", "Gdańsk"),
    Jednostka("Wojskowa Komeda Uzupełnień w Zamościu", "Mateusz Skrzypczak", "Zamość")
]
def lista_jednostek(listbox_lista_jednostek, map_widget):
    listbox_lista_jednostek.delete(0, END)
    for idx, jednostka in enumerate(jednostki):
        listbox_lista_jednostek.insert(idx,
                                       f'{jednostka.nazwa}  {jednostka.pracownicy} {jednostka.lokalizacja_jednostek}')
        jednostka.marker = map_widget.set_marker(jednostka.wspolrzedne[0], jednostka.wspolrzedne[1],
                                                 text=f"{jednostka.nazwa}")


def dodaj_jednostke(entry_nazwa, entry_pracownicy, entry_lokalizacja_jednostek, listbox_lista_jednostek, map_widget):
    nazwa = entry_nazwa.get()
    pracownicy = entry_pracownicy.get()
    lokalizacja_jednostek = entry_lokalizacja_jednostek.get()
    jednostki.append(Jednostka(nazwa, pracownicy, lokalizacja_jednostek))
    lista_jednostek(listbox_lista_jednostek, map_widget)

    entry_nazwa.delete(0, END)
    entry_pracownicy.delete(0, END)
    entry_lokalizacja_jednostek.delete(0, END)
    entry_nazwa.focus()


def usun_jednostke(listbox_lista_jednostek, map_widget):
    i = listbox_lista_jednostek.curselection()[0]
    jednostki[i].usun_marker()
    jednostki.pop(i)
    lista_jednostek(listbox_lista_jednostek, map_widget)


def pokaz_szczegoly_jednoski(listbox_lista_jednostek, label_nazwa_szczegoly_obiektu_wartosc,
                             label_pracownicy_szczegoly_obiektu_wartosc, label_lokalizacja_jednostek_szczegoly_obiektu_wartosc, map_widget):
    i = listbox_lista_jednostek.curselection()[0]
    jednostka = jednostki[i]
    label_nazwa_szczegoly_obiektu_wartosc.config(text=jednostka.nazwa)
    label_pracownicy_szczegoly_obiektu_wartosc.config(text=jednostka.pracownicy)
    label_lokalizacja_jednostek_szczegoly_obiektu_wartosc.config(text=jednostka.lokalizacja_jednostek)
    map_widget.set_position(jednostka.wspolrzedne[0], jednostka.wspolrzedne[1])
    map_widget.set_zoom(12)


def edytuj_jednostke(listbox_lista_jednostek, entry_nazwa, entry_pracownicy, entry_lokalizacja_jednostek, button_dodaj_jednostke, map_widget):
    i = listbox_lista_jednostek.curselection()[0]
    jednostka = jednostki[i]
    jednostka.usun_marker()

    entry_nazwa.delete(0, END)
    entry_pracownicy.delete(0, END)
    entry_lokalizacja_jednostek.delete(0, END)

    entry_nazwa.insert(0, jednostka.nazwa)
    entry_pracownicy.insert(0, jednostka.pracownicy)
    entry_lokalizacja_jednostek.insert(0, jednostka.lokalizacja_jednostek)

    button_dodaj_jednostke.config(text="Zapisz zmiany",
                                  command=lambda: aktualizuj_jednostke(i, entry_nazwa, entry_pracownicy, entry_lokalizacja_jednostek, button_dodaj_jednostke, listbox_lista_jednostek, map_widget))


def aktualizuj_jednostke(i, entry_nazwa, entry_pracownicy, entry_lokalizacja_jednostek, button_dodaj_jednostke, listbox_lista_jednostek, map_widget):
    jednostka = jednostki[i]
    jednostka.nazwa = entry_nazwa.get()
    jednostka.pracownicy = entry_pracownicy.get()
    jednostka.lokalizacja_jednostek = entry_lokalizacja_jednostek.get()
    jednostka.wspolrzedne = jednostka.pobierz_wspolrzedne()
    lista_jednostek(listbox_lista_jednostek, map_widget)

    button_dodaj_jednostke.config(text="Dodaj jednostke",
                                  command=lambda: dodaj_jednostke(entry_nazwa, entry_pracownicy, entry_lokalizacja_jednostek,
                                                                  listbox_lista_jednostek, map_widget))
    entry_nazwa.delete(0, END)
    entry_pracownicy.delete(0, END)
    entry_lokalizacja_jednostek.delete(0, END)
    entry_nazwa.focus()


def tworzenie_jednostki_wojskowe_root(root):
    global map_widget
    jednostki_wojskowe_root = Toplevel(root)
    jednostki_wojskowe_root.title("Jednostki Wojskowe")
    jednostki_wojskowe_root.geometry("1100x724")

    # ramki do porządkowania struktury
    ramka_lista_jednostki_wojskowe = Frame(jednostki_wojskowe_root)
    ramka_formularz = Frame(jednostki_wojskowe_root)
    ramka_szczegoly_obiektu = Frame(jednostki_wojskowe_root)

    ramka_lista_jednostki_wojskowe.grid(row=0, column=0, padx=50)
    ramka_formularz.grid(row=0, column=1)
    ramka_szczegoly_obiektu.grid(row=1, column=0, columnspan=2)

    # lista jednostek wojskowych
    label_lista_jednostki_wojskowe = Label(ramka_lista_jednostki_wojskowe, text="Lista jednostek wojskowych: ")
    listbox_lista_jednostki_wojskowe = Listbox(ramka_lista_jednostki_wojskowe, width=100)
    button_pokaz_szczegoly_jedn = Button(ramka_lista_jednostki_wojskowe, text="Pokaż szczegóły",
                                         command=lambda: pokaz_szczegoly_jednoski(listbox_lista_jednostki_wojskowe,
                                                                                  label_nazwa_szczegoly_obiektu_jedn_wartosc,
                                                                                  label_pracownicy_szczegoly_obiektu_jedn_wartosc,
                                                                                  label_lokalizacja_jednostki_szczegoly_obiektu_jedn_wartosc, map_widget))
    button_usun_obiekt_jedn = Button(ramka_lista_jednostki_wojskowe, text='Usuń obiekt', command=lambda: usun_jednostke(listbox_lista_jednostki_wojskowe, map_widget))
    button_edytuj_obiektu_jedn = Button(ramka_lista_jednostki_wojskowe, text='Edytuj obiekt',
                                        command=lambda: edytuj_jednostke(listbox_lista_jednostki_wojskowe, entry_nazwa,
                                                                         entry_pracownicy, entry_lokalizacja_jednostki,
                                                                         button_dodaj_jednostke, map_widget))

    label_lista_jednostki_wojskowe.grid(row=0, column=0, columnspan=3)
    listbox_lista_jednostki_wojskowe.grid(row=1, column=0, columnspan=3)
    button_pokaz_szczegoly_jedn.grid(row=2, column=0)
    button_usun_obiekt_jedn.grid(row=2, column=1)
    button_edytuj_obiektu_jedn.grid(row=2, column=2)

    # formularz
    label_formularz = Label(ramka_formularz, text="Formularz")
    label_nazwa = Label(ramka_formularz, text="Nazwa jednostki: ")
    label_pracownicy = Label(ramka_formularz, text="Pracownik: ")
    label_lokalizacja_jednostki = Label(ramka_formularz, text="Lokalizacja jednostki wojskowej")

    entry_nazwa = Entry(ramka_formularz)
    entry_pracownicy = Entry(ramka_formularz)
    entry_lokalizacja_jednostki = Entry(ramka_formularz)

    label_formularz.grid(row=0, column=0, columnspan=2)
    label_nazwa.grid(row=1, column=0, sticky=W)
    label_pracownicy.grid(row=2, column=0, sticky=W)
    label_lokalizacja_jednostki.grid(row=3, column=0, sticky=W)

    entry_nazwa.grid(row=1, column=1)
    entry_pracownicy.grid(row=2, column=1)
    entry_lokalizacja_jednostki.grid(row=3, column=1)

    button_dodaj_jednostke = Button(ramka_formularz, text="Dodaj jednostke", command=lambda: dodaj_jednostke(entry_nazwa, entry_pracownicy, entry_lokalizacja_jednostki, listbox_lista_jednostki_wojskowe, map_widget))
    button_dodaj_jednostke.grid(row=5, column=1, columnspan=2)

    # szczegoly obiektu

    label_szczegoly_obiektu_jedn = Label(ramka_szczegoly_obiektu, text="Szczegóły jednostki wojskowej: ")
    label_nazwa_szczegoly_obiektu_jedn = Label(ramka_szczegoly_obiektu, text="Nazwa jednostki: ")
    label_pracownicy_szczegoly_obiektu_jedn = Label(ramka_szczegoly_obiektu, text="Pracownik: ")
    label_lokalizacja_jednostki_szczegoly_obiektu_jedn = Label(ramka_szczegoly_obiektu, text="Lokalizacja jednostki wojskowej: ")

    label_nazwa_szczegoly_obiektu_jedn_wartosc = Label(ramka_szczegoly_obiektu, text="...")
    label_pracownicy_szczegoly_obiektu_jedn_wartosc = Label(ramka_szczegoly_obiektu, text="...")
    label_lokalizacja_jednostki_szczegoly_obiektu_jedn_wartosc = Label(ramka_szczegoly_obiektu, text="...")

    label_szczegoly_obiektu_jedn.grid(row=0, column=0, sticky=W)
    label_nazwa_szczegoly_obiektu_jedn.grid(row=1, column=0, sticky=W)
    label_nazwa_szczegoly_obiektu_jedn_wartosc.grid(row=1, column=1)
    label_pracownicy_szczegoly_obiektu_jedn.grid(row=1, column=2)
    label_pracownicy_szczegoly_obiektu_jedn_wartosc.grid(row=1, column=3)
    label_lokalizacja_jednostki_szczegoly_obiektu_jedn.grid(row=1, column=4)
    label_lokalizacja_jednostki_szczegoly_obiektu_jedn_wartosc.grid(row=1, column=5)

    global map_widget
    map_widget = tkintermapview.TkinterMapView(ramka_szczegoly_obiektu, width=900, height=400)
    map_widget.set_position(52.2, 21)
    map_widget.set_zoom(8)
    map_widget.grid(row=2, column=0, columnspan=8)

    lista_jednostek(listbox_lista_jednostki_wojskowe, map_widget)



class Pododdzial:
    def __init__(self, nazwa_pododdzialu, nazwa_jednostki, pracownicy, lokalizacja_pododdzialu):
        self.nazwa_pododdzialu = nazwa_pododdzialu
        self.nazwa_jednostki = nazwa_jednostki
        self.pracownicy = pracownicy
        self.lokalizacja_pododdzialu = lokalizacja_pododdzialu
        self.wspolrzedne = self.pobierz_wspolrzedne()
        self.marker = None

    def pobierz_wspolrzedne(self) -> list:
        url = f'https://pl.wikipedia.org/wiki/{self.lokalizacja_pododdzialu}'
        response = requests.get(url)
        response_html = BeautifulSoup(response.text, 'html.parser')
        return [
            float(response_html.select('.latitude')[1].text.replace(",", ".")),
            float(response_html.select('.longitude')[1].text.replace(",", "."))
        ]

    def usun_marker(self):
        if self.marker:
            self.marker.delete()
            self.marker = None

pododdzialy = [
    Pododdzial("Kompania Transportowa Sztabu Generalnego", "Sztab Generalny Wojska Polskiego","Kamil Bednarek", "Warszawa"),
    Pododdzial("21. Batalion Lekkiej Piechoty w Lublinie", "2 Lubelska Brygada Obrony Terytorialnej", "Mateusz Skrzypczak", "Lublin"),
    Pododdzial("Kompania Saperów 14. Batalionu Ułanów Jazłowieckich", "Wojskowa Komeda Uzupełnień w Szczecinie", "Martyna Tupikowska", "Szczecin"),
    Pododdzial("Pluton Łączności 31. Bazy Lotnictwa Taktycznego", "2 Skrzydło Lotnictwa Taktycznego", "Katarzyna Figura", "Poznań"),
    Pododdzial("Drużyna Strzelecka Kompanii Ochrony 10. Wrocławskiego Pułku Dowodzenia", "Wojskowa Komeda Uzupełnień we Wrocławiu", "Karol Mostek", "Wrocław"),
    Pododdzial("15. Mazowiecka Brygada Obrony Terytorialnej", "Wojewódzki Sztab Wojskowy w Białymstoku", "Michał Makowski", "Białystok"),
    Pododdzial("Drużyna Medyczna 102. Batalionu Lekkiej Piechoty ", "10 Świętokrzyska Brygada Obrony Teeytorialnej", "Julian Kochanowski", "Kielce"),
    Pododdzial("Batalion Wsparcia Bojowego", "Jednostka Wojskowa NIL", "Tomasz Karolak", "Kraków"),
    Pododdzial("7. Pomorska Brygada Obrony Terytorialnej", "Wojskowa Komeda Uzupełnień w Gdańsku", "Wojciech Michalak", "Gdańsk"),
    Pododdzial("Kompania Dowodzenia 25. Batalionu Lekkiej Piechoty", "Wojskowa Komeda Uzupełnień w Zamościu", "Mariusz Piotruk", "Zamość")
]
def lista_pododdzialow(listbox_lista_pododdzialow, map_widget):
    listbox_lista_pododdzialow.delete(0, END)
    for idx, pododdzial in enumerate(pododdzialy):
        listbox_lista_pododdzialow.insert(idx,
                                          f'{pododdzial.nazwa_pododdzialu} {pododdzial.nazwa_jednostki} {pododdzial.pracownicy} {pododdzial.lokalizacja_pododdzialu}')
        pododdzial.marker = map_widget.set_marker(pododdzial.wspolrzedne[0], pododdzial.wspolrzedne[1],
                                                  text=f"{pododdzial.nazwa_pododdzialu}")

def dodaj_pododdzial(entry_nazwa_pododdzialu, entry_nazwa_jednostki, entry_pracownicy, entry_lokalizacja_pododdzialu,
                     listbox_lista_pododdzialow, map_widget):
    nazwa_pododdzialu = entry_nazwa_pododdzialu.get()
    nazwa_jednostki = entry_nazwa_jednostki.get()
    pracownicy = entry_pracownicy.get()
    lokalizacja_pododdzialu = entry_lokalizacja_pododdzialu.get()
    print(nazwa_pododdzialu, pracownicy, lokalizacja_pododdzialu)
    pododdzialy.append(Pododdzial(nazwa_pododdzialu, nazwa_jednostki, pracownicy, lokalizacja_pododdzialu))
    lista_pododdzialow(listbox_lista_pododdzialow, map_widget)

    entry_nazwa_pododdzialu.delete(0, END)
    entry_nazwa_jednostki.delete(0, END)
    entry_pracownicy.delete(0, END)
    entry_lokalizacja_pododdzialu.delete(0, END)

    entry_nazwa_pododdzialu.focus()

def usun_pododdzial(listbox_lista_pododdzialow, map_widget):
    i = listbox_lista_pododdzialow.curselection()[0]
    pododdzialy[i].usun_marker()
    pododdzialy.pop(i)
    lista_pododdzialow(listbox_lista_pododdzialow, map_widget)

def pokaz_szczegoly_pododdzialu(listbox_lista_pododdzialow, label_nazwa_pododdzialu_szczegoly_obiektu_wartosc,
                                label_nazwa_jednostki_szczegoly_obiektu_wartosc,
                                label_pracownicy_szczegoly_obiektu_wartosc,
                                label_lokalizacja_pododdzialu_szczegoly_obiektu_wartosc, map_widget):
    i = listbox_lista_pododdzialow.curselection()[0]
    pododdzial = pododdzialy[i]
    label_nazwa_pododdzialu_szczegoly_obiektu_wartosc.config(text=pododdzial.nazwa_pododdzialu)
    label_nazwa_jednostki_szczegoly_obiektu_wartosc.config(text=pododdzial.nazwa_jednostki)
    label_pracownicy_szczegoly_obiektu_wartosc.config(text=pododdzial.pracownicy)
    label_lokalizacja_pododdzialu_szczegoly_obiektu_wartosc.config(text=pododdzial.lokalizacja_pododdzialu)
    map_widget.set_position(pododdzial.wspolrzedne[0], pododdzial.wspolrzedne[1])
    map_widget.set_zoom(12)

def edytuj_pododdzial(listbox_lista_pododdzialow, entry_nazwa_pododdzialu, entry_nazwa_jednostki, entry_pracownicy,
                      entry_lokalizacja_pododdzialu, button_dodaj_pododdzial, map_widget):
    i = listbox_lista_pododdzialow.curselection()[0]
    pododdzial = pododdzialy[i]
    pododdzial.usun_marker()
    entry_nazwa_pododdzialu.delete(0, END)
    entry_nazwa_jednostki.delete(0, END)
    entry_pracownicy.delete(0, END)
    entry_lokalizacja_pododdzialu.delete(0, END)
    entry_nazwa_pododdzialu.insert(0, pododdzial.nazwa_pododdzialu)
    entry_nazwa_jednostki.insert(0, pododdzial.nazwa_jednostki)
    entry_pracownicy.insert(0, pododdzial.pracownicy)
    entry_lokalizacja_pododdzialu.insert(0, pododdzial.lokalizacja_pododdzialu)

    button_dodaj_pododdzial.config(text="Zapisz zmiany",
                                   command=lambda: aktualizuj_pododdzial(i, entry_nazwa_pododdzialu, entry_nazwa_jednostki, entry_pracownicy,
                                                                         entry_lokalizacja_pododdzialu, button_dodaj_pododdzial,
                                                                         listbox_lista_pododdzialow, map_widget))

def aktualizuj_pododdzial(i, entry_nazwa_pododdzialu, entry_nazwa_jednostki, entry_pracownicy,
                          entry_lokalizacja_pododdzialu, button_dodaj_pododdzial, listbox_lista_pododdzialow, map_widget):
    pododdzial = pododdzialy[i]
    pododdzial.nazwa_pododdzialu = entry_nazwa_pododdzialu.get()
    pododdzial.nazwa_jednostki = entry_nazwa_jednostki.get()
    pododdzial.pracownicy = entry_pracownicy.get()
    pododdzial.lokalizacja_pododdzialu = entry_lokalizacja_pododdzialu.get()
    pododdzial.wspolrzedne = pododdzial.pobierz_wspolrzedne()  # Update coordinates

    lista_pododdzialow(listbox_lista_pododdzialow, map_widget)

    button_dodaj_pododdzial.config(text="Dodaj pododdział",  # Reset button text
                                   command=lambda: dodaj_pododdzial(entry_nazwa_pododdzialu, entry_nazwa_jednostki, entry_pracownicy,
                                                                    entry_lokalizacja_pododdzialu, listbox_lista_pododdzialow, map_widget))

    entry_nazwa_pododdzialu.delete(0, END)
    entry_nazwa_jednostki.delete(0, END)
    entry_pracownicy.delete(0, END)
    entry_lokalizacja_pododdzialu.delete(0, END)
    entry_nazwa_pododdzialu.focus()

def tworzenie_pododdzialy_root(root):
    global map_widget
    pododdzialy_root = Toplevel(root)
    pododdzialy_root.title("Pododdziały")
    pododdzialy_root.geometry("1200x724")

    # ramki do porządkowania struktury
    ramka_lista_pododdzialy = Frame(pododdzialy_root)
    ramka_formularz = Frame(pododdzialy_root)
    ramka_szczegoly_obiektu = Frame(pododdzialy_root)

    ramka_lista_pododdzialy.grid(row=0, column=0, padx=50)
    ramka_formularz.grid(row=0, column=1)
    ramka_szczegoly_obiektu.grid(row=1, column=0, columnspan=2)

    # lista_pododdzialow
    label_lista_pododdzialy = Label(ramka_lista_pododdzialy, text="Lista pododziałów: ")
    listbox_lista_pododdzialy = Listbox(ramka_lista_pododdzialy, width=120)
    button_pokaz_szczegoly_pododdzialu = Button(ramka_lista_pododdzialy, text="Pokaż szczegóły",
                                                command=lambda: pokaz_szczegoly_pododdzialu(listbox_lista_pododdzialy,
                                                                                            label_nazwa_pododzialu_szczegoly_obiektu_wartosc,
                                                                                            label_nazwa_jednostki_szczegoly_obiektu_wartosc,
                                                                                            label_pracownicy_szczegoly_obiektu_wartosc,
                                                                                            label_lokalizacja_pododdzialu_szczegoly_obiektu_wartosc, map_widget))
    button_usun_obiekt = Button(ramka_lista_pododdzialy, text='Usuń obiekt', command=lambda: usun_pododdzial(listbox_lista_pododdzialy, map_widget))
    button_edytuj_obiektu = Button(ramka_lista_pododdzialy, text='Edytuj obiekt',
                                   command=lambda: edytuj_pododdzial(listbox_lista_pododdzialy, entry_nazwa_pododdzialu, entry_nazwa_jednostki,
                                                                     entry_pracownicy, entry_lokalizacja_pododdzialu,
                                                                     button_dodaj_pododdzial, map_widget))
    label_lista_pododdzialy.grid(row=0, column=0, columnspan=3)
    listbox_lista_pododdzialy.grid(row=1, column=0, columnspan=3)
    button_pokaz_szczegoly_pododdzialu.grid(row=2, column=0)
    button_usun_obiekt.grid(row=2, column=1)
    button_edytuj_obiektu.grid(row=2, column=2)

    # formularz
    label_formularz = Label(ramka_formularz, text="Formularz")
    label_nazwa_pododzialu = Label(ramka_formularz, text="Nazwa pododdziału: ")
    label_nazwa_jednostki = Label(ramka_formularz, text="Nazwa jednostki wojskowej: ")
    label_pracownicy = Label(ramka_formularz, text="Pracownik: ")
    label_lokalizacja_pododdzialu = Label(ramka_formularz, text="Lokalizacja pododdziału:")

    entry_nazwa_pododdzialu = Entry(ramka_formularz)
    entry_nazwa_jednostki = Entry(ramka_formularz)
    entry_pracownicy = Entry(ramka_formularz)
    entry_lokalizacja_pododdzialu = Entry(ramka_formularz)

    label_formularz.grid(row=0, column=0, columnspan=2)
    label_nazwa_pododzialu.grid(row=1, column=0, sticky=W)
    label_nazwa_jednostki.grid(row=2, column=0, sticky=W)
    label_pracownicy.grid(row=3, column=0, sticky=W)
    label_lokalizacja_pododdzialu.grid(row=4, column=0, sticky=W)

    entry_nazwa_pododdzialu.grid(row=1, column=1)
    entry_nazwa_jednostki.grid(row=2, column=1)
    entry_pracownicy.grid(row=3, column=1)
    entry_lokalizacja_pododdzialu.grid(row=4, column=1)

    button_dodaj_pododdzial = Button(ramka_formularz, text="Dodaj pododdział",
                                     command=lambda: dodaj_pododdzial(entry_nazwa_pododdzialu, entry_nazwa_jednostki,
                                                                      entry_pracownicy, entry_lokalizacja_pododdzialu,
                                                                      listbox_lista_pododdzialy, map_widget))
    button_dodaj_pododdzial.grid(row=5, column=1, columnspan=2)

    # szczegoly obiektu
    label_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text="Szczegóły pododdziału: ")
    label_nazwa_pododzialu_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text="Nazwa pododdziału: ")
    label_nazwa_jednostki_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text="Nazwa jednostki wojskowej: ")
    label_pracownicy_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text="Pracownik: ")
    label_lokalizacja_pododdzialu_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text="Lokalizacja pododdziału: ")

    label_nazwa_pododzialu_szczegoly_obiektu_wartosc = Label(ramka_szczegoly_obiektu, text="...")
    label_nazwa_jednostki_szczegoly_obiektu_wartosc = Label(ramka_szczegoly_obiektu, text="...")
    label_pracownicy_szczegoly_obiektu_wartosc = Label(ramka_szczegoly_obiektu, text="...")
    label_lokalizacja_pododdzialu_szczegoly_obiektu_wartosc = Label(ramka_szczegoly_obiektu, text="...")

    label_szczegoly_obiektu.grid(row=0, column=0, sticky=W)
    label_nazwa_pododzialu_szczegoly_obiektu.grid(row=1, column=0, sticky=W)
    label_nazwa_pododzialu_szczegoly_obiektu_wartosc.grid(row=1, column=1)
    label_nazwa_jednostki_szczegoly_obiektu.grid(row=1, column=2)
    label_nazwa_jednostki_szczegoly_obiektu_wartosc.grid(row=1, column=3)
    label_pracownicy_szczegoly_obiektu.grid(row=1, column=4)
    label_pracownicy_szczegoly_obiektu_wartosc.grid(row=1, column=5)
    label_lokalizacja_pododdzialu_szczegoly_obiektu.grid(row=1, column=6)
    label_lokalizacja_pododdzialu_szczegoly_obiektu_wartosc.grid(row=1, column=7)

    global map_widget
    map_widget = tkintermapview.TkinterMapView(ramka_szczegoly_obiektu, width=900, height=400)
    map_widget.set_position(52.2, 21)
    map_widget.set_zoom(8)
    map_widget.grid(row=2, column=0, columnspan=8)

    lista_pododdzialow(listbox_lista_pododdzialy, map_widget)
def logowanie():
    login_window = Tk()
    login_window.title("Panel logowania")
    login_window.geometry("400x300")

    label_login = Label(login_window, text="Wprowadź login:")
    label_login.pack(pady=5)
    entry_login = Entry(login_window)
    entry_login.pack(pady=5)

    label_haslo = Label(login_window, text="Wprowadź hasło:")
    label_haslo.pack(pady=5)
    entry_haslo = Entry(login_window, show="*")
    entry_haslo.pack(pady=5)

    def validate_login(event=None):
        login = entry_login.get()
        haslo = entry_haslo.get()
        print(f"Login: {login}, Hasło: {haslo}")
        if login in login_data and login_data[login] == haslo:
            print("Zalogowano pomyślnie")
            login_window.destroy()
            okno_glowne()
        else:
            print("Błędne dane logowania. Spróbuj ponownie.")
            messagebox.showerror("Błąd logowania", "Błędne dane logowania. Spróbuj ponownie.")

    button_login = Button(login_window, text="Zaloguj", command=validate_login)
    button_login.pack(pady=20)
    entry_haslo.bind("<Return>", validate_login)
    login_window.mainloop()

def okno_glowne():

            root = Tk()
            root.title("Menu główne")
            root.geometry("800x500")

            label = Label(root, text="Wybierz opcję:")
            label.grid(row=0, column=0, columnspan=3)

            button1 = Button(root, text="Jednostki wojskowe",
                             command=lambda: tworzenie_jednostki_wojskowe_root(root))
            button1.grid(row=1, column=0)

            button2 = Button(root, text="Pracownicy",
                             command=lambda: tworzenie_pracownicy_root(root))
            button2.grid(row=1, column=1)

            button3 = Button(root, text="Pododdziały w jednostce",
                             command=lambda: tworzenie_pododdzialy_root(root))
            button3.grid(row=1, column=2)

            root.mainloop()

logowanie()
