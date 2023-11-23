# model.py
class DogModel:
    def __init__(self):
        self.dogs = [
        {
            "Pies": 1,
            "Imie": "Rex",
            "Wiek": 3,
            "Rasa": "Owczarek niemiecki",
            "Kolor sierci": "Czarny",
            "Plec": "Suczka",
            "Waga": "25.5",
            "Rodzaj sierci": "Krotka",
            "Wielkosc": "Duzy",
            "Data przyjecia do schroniska": "2023/01/20",
            "Miasto": "Bialystok"
        },
        {
            "Pies": 2,
            "Imie": "Alex",
            "Wiek": 1,
            "Rasa": "Boxer",
            "Kolor sierci": "Brazowy",
            "Plec": "Pies",
            "Waga": "15.0",
            "Rodzaj sierci": "Krotka",
            "Wielkosc": "Duzy",
            "Data przyjecia do schroniska": "2022/09/30",
            "Miasto": "Warszawa"
        },
        {
            "Pies": 3,
            "Imie": "Buddy",
            "Wiek": 2,
            "Rasa": "Golden Retriever",
            "Kolor sierci": "Zloty",
            "Plec": "Pies",
            "Waga": "30.0",
            "Rodzaj sierci": "Dluga",
            "Wielkosc": "Sredni",
            "Data przyjecia do schroniska": "2019/05/21",
            "Miasto": "Warszawa"
        },
        {
            "Pies": 4,
            "Imie": "Luna",
            "Wiek": 4,
            "Rasa": "Labrador",
            "Kolor sierci": "Czekoladowy",
            "Plec": "Suczka",
            "Waga": "28.0",
            "Rodzaj sierci": "Krotka",
            "Wielkosc": "Duzy",
            "Data przyjecia do schroniska": "2020/11/05",
            "Miasto": "Krakow"
        },
        {
            "Pies": 5,
            "Imie": "Max",
            "Wiek": 5,
            "Rasa": "Bulldog",
            "Kolor sierci": "Bialy",
            "Plec": "Pies",
            "Waga": "18.5",
            "Rodzaj sierci": "Krotka",
            "Wielkosc": "Sredni",
            "Data przyjecia do schroniska": "2022/12/26",
            "Miasto": "Lodz"
        },
        {
            "Pies": 6,
            "Imie": "Lola",
            "Wiek": 2,
            "Rasa": "Yorkshire Terrier",
            "Kolor sierci": "Czarny i brazowy",
            "Plec": "Suczka",
            "Waga": "04.0",
            "Rodzaj sierci": "Dluga",
            "Wielkosc": "Maly",
            "Data przyjecia do schroniska": "2021/07/16",
            "Miasto": "Gdansk"
        },
        {
            "Pies": 7,
            "Imie": "Rocky",
            "Wiek": 3,
            "Rasa": "Siberian Husky",
            "Kolor sierci": "Szary i bialy",
            "Plec": "Pies",
            "Waga": "22.0",
            "Rodzaj sierci": "Dluga",
            "Wielkosc": "Duzy",
            "Data przyjecia do schroniska": "2022/03/31",
            "Miasto": "Warszawa"
        },
        {
            "Pies": 8,
            "Imie": "Charlie",
            "Wiek": 2,
            "Rasa": "Cavalier King Charles Spaniel",
            "Kolor sierci": "Brazowy i bialy",
            "Plec": "Pies",
            "Waga": "07.5",
            "Rodzaj sierci": "Dluga",
            "Wielkosc": "Maly",
            "Data przyjecia do schroniska": "2021/09/12",
            "Miasto": "Krakow"
        },
        {
            "Pies": 9,
            "Imie": "Pikus",
            "Wiek": 5,
            "Rasa": "Kundel",
            "Kolor sierci": "Czarny",
            "Plec": "Pies",
            "Waga": "11.0",
            "Rodzaj sierci": "Dluga",
            "Wielkosc": "Maly",
            "Data przyjecia do schroniska": "2019/10/25",
            "Miasto": "Lodz"
        },
        ]

        self.shelters = [
            {
            "Miasto": "Bialystok",
            "Nazwa": "Dom Nadziei dla Psich Przyjaciół",
            "Hasło": "Za każdy łapacz życia, zasługuje na bezpieczny dom",
            "Lokalizacja": "Białystok, ul. Zwierzyniecka 45",
            "Historia Schroniska": "Powstanie schroniska w 2005 roku jako inicjatywa grupy miłośników zwierząt",
            "Kontakt": {
                "Telefon": "+48 85 987 654 321",
                "E-mail": "adopcje@domnadziei-dlapsow.pl"
            }
        },
        {
            "Miasto": "Warszawa",
            "Nazwa": "Przytulisko Serce dla Bezdomnych Zwierząt",
            "Hasło": "Miłość, szansa, dom - każde zwierzę zasługuje na szczęśliwe życie",
            "Lokalizacja": "Warszawa, ul. Zwierzyniecka 78",
            "Historia Schroniska": "Założone w 2010 roku przez grupę wolontariuszy z pasją do zwierząt",
            "Kontakt": {
                "Telefon": "+48 22 345 678 901",
                "E-mail": "adopcje@przytuliskoserce.pl"
            }
        },
        {
            "Miasto": "Kraków",
            "Nazwa": "Krakowskie Schronisko dla Bezdomnych Zwierząt",
            "Hasło": "Wspólnie dla zwierząt - każda pomoc ma znaczenie",
            "Lokalizacja": "Kraków, ul. Zwierzyniecka 56",
            "Historia Schroniska": "Rozpoczęło działalność w 2012 roku, z zaangażowaniem społeczności krakowskiej",
            "Kontakt": {
                "Telefon": "+48 50 987 654 321",
                "E-mail": "kontakt@schroniskokrakow.pl"
            }
        },
        {
            "Miasto": "Gdańsk",
            "Nazwa": "Gdańskie Schronisko Zwierząt Morskich",
            "Hasło": "Ratujmy razem - dla zdrowia morskich przyjaciół",
            "Lokalizacja": "Gdańsk, ul. Morska 87",
            "Historia Schroniska": "Schronisko powstało w 2015 roku, jako odpowiedź na potrzeby zwierząt morskich",
            "Kontakt": {
                "Telefon": "+48 58 123 456 789",
                "E-mail": "kontakt@schroniskogdansk.pl"
            }
        },
        {
            "Miasto": "Łódź",
            "Nazwa": "Łódzkie Schronisko Zwierząt",
            "Hasło": "Daj im dom, a oni dadzą ci miłość",
            "Lokalizacja": "Łódź, ul. Zwierzęca 12",
            "Historia Schroniska": "Początki sięgają 2008 roku, z inicjatywy miłośników zwierząt z Łodzi",
            "Kontakt": {
                "Telefon": "+48 42 789 012 345",
                "E-mail": "kontakt@schroniskolodz.pl"
            }
        },
        ]
        self.adoption_forms = []  # Dodana lista do przechowywania formularzy adopcyjnych

    def add_adoption_form(self, form_data):
        self.adoption_forms.append(form_data)

    def submit_adoption_form(self, form_data):
        self.add_adoption_form(form_data) 


    def filter_dogs(self, category, criteria):
        filtered_dogs = []
        for dog in self.dogs:
            if category in dog and str(dog[category]).lower() == criteria.lower():
                filtered_dogs.append(dog)
        return filtered_dogs
