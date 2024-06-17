jednostki: list = [
    {"nazwa": "Sztab Generalny Wojska Polskiego", "pracownik": "Artur Lech", "lokalizacja_jednsotki": "Warszawa"},
    {"nazwa": "2 Lubelska Brygada Obrony Terytorialnej", "pracownik": "Zuzanna Orkisz",
     "lokalizacja_jednsotki": "Lublin"},
    {"nazwa": "Wojskowa Komeda Uzupełnień w Szczecinie", "pracownik": "Kacper Trzcina",
     "lokalizacja_jednsotki": "Szczecin"},
    {"nazwa": "2 Skrzydło Lotnictwa Taktycznego", "pracownik": "Konrad Kowaliski", "lokalizacja_jednsotki": "Poznań"},
    {"nazwa": "Wojskowa Komeda Uzupełnień we Wrocławiu", "pracownik": "Kinga Bartoszewska",
     "lokalizacja_jednsotki": "Wrocław"},
    {"nazwa": "Wojskowa Komeda Uzupełnień w Białymstoku", "pracownik": "Mateusz Kiper",
     "lokalizacja_jednsotki": "Białystok"},
    {"nazwa": "10 Świętokrzyska Brygada Obrony Terytorialnej", "pracownik": "Andrzej Iwaniak",
     "lokalizacja_jednsotki": "Kielce"},
    {"nazwa": "Jednostka Wojskowa NIL", "pracownik": "Mirosław Kowal", "lokalizacja_jednsotki": "Kraków"},
    {"nazwa": "Wojskowa Komeda Uzupełnień w Gdańsku", "pracownik": "Mateusz Skrzypczak",
     "lokalizacja_jednsotki": "Gdańsk"},
    {"nazwa": "Wojskowa Komeda Uzupełnień w Zamościu", "pracownik": "Mateusz Skrzypczak",
     "lokalizacja_jednsotki": "Zamość"}
]

pracownicy: list = [

    {"imie": "Artur", "nazwisko": "Lech", "stanowisko": "Dowódca", "lokalizacja": "Warszawa"},
    {"imie": "Kamil", "nazwisko": "Bednarek", "stanowisko": "Oficer", "lokalizacja": "Grudziądz"},
    {"imie": "Karol", "nazwisko": "Mastek", "stanowisko": "Dowódca kampanii", "lokalizacja": "Olsztyn"},
    {"imie": "Julian", "nazwisko": "Kochanek", "stanowisko": "Radiooperator", "lokalizacja": "Toruń"},
    {"imie": "Zuzanna", "nazwisko": "Orkisz", "stanowisko": "Kapral", "lokalizacja": "Lublin"},
    {"imie": "Kacper", "nazwisko": "Trzcina", "stanowisko": "Dowódca", "lokalizacja": "Szczecin"},
    {"imie": "Katarzyna", "nazwisko": "Figura", "stanowisko": "Kierowca", "lokalizacja": "Gorzów Wielkopolski"},
    {"imie": "Tomasz", "nazwisko": "Karolak", "stanowisko": "Strzelec wyborowy", "lokalizacja": "Zielona Góra"},
    {"imie": "Konrad", "nazwisko": "Kowaliski", "stanowisko": "Podoficer", "lokalizacja": "Poznań"},
    {"imie": "Wojciech", "nazwisko": "Michalak", "stanowisko": "Podporucznik", "lokalizacja": "Opole"},
    {"imie": "Michał", "nazwisko": "Makowski", "stanowisko": "Sanitariusz", "lokalizacja": "Częstochowa"},
    {"imie": "Kinga", "nazwisko": "Bartoszewska", "stanowisko": "Strzelec", "lokalizacja": "Wrocław"},
    {"imie": "Andrzej", "nazwisko": "Iwniak", "stanowisko": "Podoficer", "lokalizacja": "Kielce"},
    {"imie": "Mateusz", "nazwisko": "Skrzypczak", "stanowisko": "Chorąży", "lokalizacja": "Siedlce"},
    {"imie": "Mirosław", "nazwisko": "Kowal", "stanowisko": "Starszy sierżant kompani", "lokalizacja": "Kraków"},
    {"imie": "Mateusz", "nazwisko": "Kiper", "stanowisko": "Oficer Łączności", "lokalizacja": "Białystok"},
    {"imie": "Mariusz", "nazwisko": "Piotruk", "stanowisko": "Sierżant", "lokalizacja": "Bydgoszcz"},
    {"imie": "Martyna", "nazwisko": "Tupikowska", "stanowisko": "Dowódca", "lokalizacja": "Tarnów"},
    {"imie": "Mariusz", "nazwisko": "Pierożek", "stanowisko": "Celowniczy", "lokalizacja": "Gdańsk"},
    {"imie": "Leon", "nazwisko": "Seat", "stanowisko": "Oficer medyczny", "lokalizacja": "Zamość"}
]

pododdzialy: list = [
    {"nazwa_pododdziału": "Kompania Transportowa Sztabu Generalnego",
     "nazwa_jednostki": "Sztab Generalny Wojska Polskiego", "pracownicy": "Kamil Bednarek",
     "lokalizacja_pododdziału": "Warszawa"},
    {"nazwa_pododdziału": "21. Batalion Lekkiej Piechoty w Lublinie",
     "nazwa_jednostki": "2 Lubelska Brygada Obrony Terytorialnej",
     "pracownicy": "Mateusz Skrzypczak", "lokalizacja_pododdziału": "Lublin"},
    {"nazwa_pododdziału": "Kompania Saperów 14. Batalionu Ułanów Jazłowieckich",
     "nazwa_jednostki": "Wojskowa Komeda Uzupełnień w Szczecinie",
     "pracownicy": "Martyna Tupikowska", "lokalizacja_pododdziału": "Szczecin"},
    {"nazwa_pododdziału": "Pluton Łączności 31. Bazy Lotnictwa Taktycznego",
     "nazwa_jednostki": "2 Skrzydło Lotnictwa Taktycznego",
     "pracownicy": "Katarzyna Figura", "lokalizacja_pododdziału": "Poznań"},
    {"nazwa_pododdziału": "Drużyna Strzelecka Kompanii Ochrony 10. Wrocławskiego Pułku Dowodzenia",
     "nazwa_jednostki": "Wojskowa Komeda Uzupełnień we Wrocławiu", "pracownicy": "Karol Mostek",
     "lokalizacja_pododdziału": "Wrocław"},
    {"nazwa_pododdziału": "15. Mazowiecka Brygada Obrony Terytorialnej",
     "nazwa_jednostki": "Wojewódzki Sztab Wojskowy w Białymstoku",
     "pracownicy": "Michał Makowski", "lokalizacja_pododdziału": "Białystok"},
    {"nazwa_pododdziału": "Drużyna Medyczna 102. Batalionu Lekkiej Piechoty ",
     "nazwa_jednostki": "10 Świętokrzyska Brygada Obrony Teeytorialnej",
     "pracownicy": "Julian Kochanowski", "lokalizacja_pododdziału": "Kielce"},
    {"nazwa_pododdziału": "Batalion Wsparcia Bojowego", "nazwa_jednostki": "Jednostka Wojskowa NIL",
     "pracownicy": "Tomasz Karolak", "lokalizacja_pododdziału": "Kraków"},
    {"nazwa_pododdziału": "7. Pomorska Brygada Obrony Terytorialnej",
     "nazwa_jednostki": "Wojskowa Komeda Uzupełnień w Gdańsku", "pracownicy": "Wojciech Michalak",
     "lokalizacja_pododdziału": "Gdańsk"},
    {"nazwa_pododdziału": "Kompania Dowodzenia 25. Batalionu Lekkiej Piechoty",
     "nazwa_jednostki": "Wojskowa Komeda Uzupełnień w Zamościu",
     "pracownicy": "Mariusz Piotruk", "lokalizacja_pododdziału": "Zamość"}
]

pracownicy_pododdzialu: list = [

    {"imie": "Kamil", "nazwisko": "Bednarek", "stanowisko": "Oficer", "lokalizacja": "Grudziądz"},
    {"imie": "Karol", "nazwisko": "Mastek", "stanowisko": "Dowódca kampanii", "lokalizacja": "Olsztyn"},
    {"imie": "Julian", "nazwisko": "Kochanek", "stanowisko": "Radiooperator", "lokalizacja": "Toruń"},
    {"imie": "Katarzyna", "nazwisko": "Figura", "stanowisko": "Kierowca", "lokalizacja": "Gorzów Wielkopolski"},
    {"imie": "Tomasz", "nazwisko": "Karolak", "stanowisko": "Strzelec wyborowy", "lokalizacja": "Zielona Góra"},
    {"imie": "Wojciech", "nazwisko": "Michalak", "stanowisko": "Podporucznik", "lokalizacja": "Opole"},
    {"imie": "Michał", "nazwisko": "Makowski", "stanowisko": "Sanitariusz", "lokalizacja": "Częstochowa"},
    {"imie": "Mateusz", "nazwisko": "Skrzypczak", "stanowisko": "Chorąży", "lokalizacja": "Siedlce"},
    {"imie": "Mariusz", "nazwisko": "Piotruk", "stanowisko": "Sierżant", "lokalizacja": "Bydgoszcz"},
    {"imie": "Martyna", "nazwisko": "Tupikowska", "stanowisko": "Dowódca", "lokalizacja": "Tarnów"}

]

pracownicy_jednostki: list = [

    {"imie": "Artur", "nazwisko": "Lech", "stanowisko": "Dowódca", "lokalizacja": "Warszawa"},
    {"imie": "Zuzanna", "nazwisko": "Orkisz", "stanowisko": "Kapral", "lokalizacja": "Lublin"},
    {"imie": "Kacper", "nazwisko": "Trzcina", "stanowisko": "Dowódca", "lokalizacja": "Szczecin"},
    {"imie": "Konrad", "nazwisko": "Kowaliski", "stanowisko": "Podoficer", "lokalizacja": "Poznań"},
    {"imie": "Kinga", "nazwisko": "Bartoszewska", "stanowisko": "Strzelec", "lokalizacja": "Wrocław"},
    {"imie": "Andrzej", "nazwisko": "Iwniak", "stanowisko": "Podoficer", "lokalizacja": "Kielce"},
    {"imie": "Mirosław", "nazwisko": "Kowal", "stanowisko": "Starszy sierżant kompani", "lokalizacja": "Kraków"},
    {"imie": "Mateusz", "nazwisko": "Kiper", "stanowisko": "Oficer Łączności", "lokalizacja": "Białystok"},
    {"imie": "Mariusz", "nazwisko": "Pierożek", "stanowisko": "Celowniczy", "lokalizacja": "Gdańsk"},
    {"imie": "Leon", "nazwisko": "Seat", "stanowisko": "Oficer medyczny", "lokalizacja": "Zamość"}

]
