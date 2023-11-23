# controller.py
import curses
from model import DogModel
from view import DogView

class DogController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.selected_row = 0

    def run(self):  
            curses.curs_set(0)
            curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
            options = ["Informacje o wszystkich psach",
                       "Wypełnij formularz adopcyjny",
                       "Kontakt z schroniskiem",
                       "Filtruj",
                       "Sortuj",
                       "Wyjście"]

            while True:
                self.view.display_menu(options, self.selected_row)
                key = self.view.stdscr.getch()

                if key == curses.KEY_DOWN and self.selected_row < 5:
                    self.selected_row += 1
                elif key == curses.KEY_UP and self.selected_row > 0:
                    self.selected_row -= 1
                elif key == 10:  # Enter key
                    if self.selected_row == 5:
                        break
                    elif self.selected_row == 0:
                        self.show_dog_information()
                    elif self.selected_row == 1:
                        self.fill_adoption_form()
                    elif self.selected_row == 2:
                        self.show_shelters()
                    elif self.selected_row == 3:
                        self.filter_dogs()
                    elif self.selected_row == 4:
                        self.sort_dogs()
    
       

    def show_dog_information(self):
        psy = self.model.dogs
        selected_row = 0

        while True:
            self.view.display_pies(psy, selected_row)
            key = self.view.stdscr.getch()

            if key == curses.KEY_DOWN and selected_row < len(psy) - 1:
                selected_row += 1
            elif key == curses.KEY_UP and selected_row > 0:
                selected_row -= 1
            elif key == 10:  # Enter key
                chosen_pies = psy[selected_row]
                self.view.display_pies_info(chosen_pies)
                key = self.view.stdscr.getch()  # Oczekiwanie na naciśnięcie klawisza przed powrotem do menu
                if key == 27:  # Escape key
                    break
            elif key == 27:  # Escape key
                break


    def fill_adoption_form(self):
        # Implementuj logikę wypełniania formularza adopcyjnego
        pass

    def show_shelters(self):
        shelters = self.model.shelters
        selected_row = 0

        while True:
            self.view.display_shelters(shelters, selected_row)
            key = self.view.stdscr.getch()

            if key == curses.KEY_DOWN and selected_row < len(shelters) - 1:
                selected_row += 1
            elif key == curses.KEY_UP and selected_row > 0:
                selected_row -= 1
            elif key == 10:  # Enter key
                chosen_shelter = shelters[selected_row]
                self.view.display_schronisko_info(chosen_shelter)
                key = self.view.stdscr.getch()  # Oczekiwanie na naciśnięcie klawisza przed powrotem do menu
                if key == 27:  # Escape key
                    break
            elif key == 27:  # Escape key
                break


    def sort_dogs(self):
        sort_options = ["Imie", "Wiek", "Waga", "Data przyjecia do schroniska", "Powrot do menu"]
        selected_row = 0

        while True:
            self.view.display_menu(sort_options, selected_row)
            key = self.view.stdscr.getch()

            if key == curses.KEY_DOWN and selected_row < len(sort_options) - 1:
                selected_row += 1
            elif key == curses.KEY_UP and selected_row > 0:
                selected_row -= 1
            elif key == 10:  # Enter key
                if selected_row == len(sort_options) - 1:  # Ostatnia opcja (Powrot do menu)
                    break
                else:
                    self.sort_dogs_and_display(sort_options[selected_row])

    def sort_dogs_and_display(self, sort_option):
        if sort_option == "Imie":
            self.model.dogs.sort(key=lambda x: x["Imie"])
        elif sort_option == "Wiek":
            self.model.dogs.sort(key=lambda x: x["Wiek"])
        elif sort_option == "Waga":
            self.model.dogs.sort(key=lambda x: x["Waga"])
        elif sort_option == "Data przyjecia do schroniska":
            self.model.dogs.sort(key=lambda x: x["Data przyjecia do schroniska"])
        # Dodaj kolejne warunki sortowania według innych opcji

        selected_row = 0
        while True:
            self.view.display_pies(self.model.dogs, selected_row)
            key = self.view.stdscr.getch()

            if key == curses.KEY_DOWN and selected_row < len(self.model.dogs) - 1:
                selected_row += 1
            elif key == curses.KEY_UP and selected_row > 0:
                selected_row -= 1
            elif key == 10:  # Enter key
                chosen_pies = self.model.dogs[selected_row]
                self.view.display_pies_info(chosen_pies)
                key = self.view.stdscr.getch()  # Oczekiwanie na naciśnięcie klawisza przed powrotem do menu
                if key == 27:  # Escape key
                    break
            elif key == 27:  # Escape key
                break



    def filter_dogs(self):
        filter_options = ["Rasa", "Plec", "Waga", "Kolor sierci", "Wielkosc", "Miejscowosc", "Powrot do menu"]
        selected_row = 0

        while True:
            self.view.display_menu(filter_options, selected_row)
            key = self.view.stdscr.getch()

            if key == curses.KEY_DOWN and selected_row < len(filter_options) - 1:
                selected_row += 1
            elif key == curses.KEY_UP and selected_row > 0:
                selected_row -= 1
            elif key == 10:  # Enter key
                if selected_row == len(filter_options) - 1:  # Ostatnia opcja (Powrot do menu)
                    break
                else:
                    filter_category = filter_options[selected_row]
                    self.perform_filter(filter_category)
            elif key == 27:  # Escape key
                break

    def perform_filter(self, filter_category):
        user_input = self.view.get_user_input(f"Podaj kryterium dla {filter_category}: ")
        filtered_dogs = self.model.filter_dogs(filter_category, user_input)

        if not filtered_dogs:
             self.view.display_message("Brak wyników.")
        else:
            selected_row = 0
            while True:
                self.view.display_pies(filtered_dogs, selected_row)
                key = self.view.stdscr.getch()

                if key == curses.KEY_DOWN and selected_row < len(filtered_dogs) - 1:
                    selected_row += 1
                elif key == curses.KEY_UP and selected_row > 0:
                    selected_row -= 1
                elif key == 10:  # Enter key
                    chosen_pies = filtered_dogs[selected_row]
                    self.view.display_pies_info(chosen_pies)
                    key = self.view.stdscr.getch()  # Oczekiwanie na naciśnięcie klawisza przed powrotem do menu
                    if key == 27:  # Escape key
                        break
                elif key == 27:  # Escape key
                    break

    def fill_adoption_form(self):
        adoption_form_questions = [
            "Imię wnioskodawcy:",
            "Nazwisko wnioskodawcy:",
            "Adres:",
            "Numer telefonu:",
            "Wiek wnioskodawcy:",
            "Gdzie mieszkasz? (dom/mieszkanie):",
            "Czy posiadasz jakieś inne zwierzęta? (Tak/Nie):",
            "Wymień jakie są to zwierzęta:",
            "Czy posiadasz dzieci? (Tak/Nie):",
            "Wymień liczbę dzieci i ich wiek.",
            "Czy jesteś gotowy na regularne spacery z psem? (Tak/Nie):",
            "Jakiego psa chcesz zadoptować? Podaj imię.",
        ]

        form_answers = self.view.display_adoption_form(adoption_form_questions)
        form_data = dict(zip(adoption_form_questions, form_answers))
        self.model.submit_adoption_form(form_data)
        self.view.display_adoption_success()





    
