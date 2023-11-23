# view.py
import curses

class DogView:
    def __init__(self, stdscr):
        curses.curs_set(0)
        self.stdscr = stdscr
        self.height, self.width = self.stdscr.getmaxyx()

    def display_menu(self, options, selected_row):
        self.stdscr.clear()
        height, width = self.stdscr.getmaxyx()

        for i, option in enumerate(options):
            x = width // 2 - len(option) // 2
            y = height // 2 - len(options) // 2 + i
            if i == selected_row:
                self.stdscr.attron(curses.color_pair(1))
                self.stdscr.addstr(y, x, option)
                self.stdscr.attroff(curses.color_pair(1))
            else:
                self.stdscr.addstr(y, x, option)

        self.stdscr.refresh()

    def display_pies(self, psy, selected_row):
        self.stdscr.clear()
        h, w = self.stdscr.getmaxyx()

        # Calculate the number of columns based on the width
        num_columns = 10
        column_width = w // num_columns

        for index, pies in enumerate(psy, start=1):
            column = (index - 1) % num_columns
            row = (index - 1) // num_columns

            x = column * column_width + column_width // 2 - len(pies["Imie"]) // 2
            y = h // 2 - len(psy) // 2 + row

            if index - 1 == selected_row:
                self.stdscr.attron(curses.color_pair(1))
                self.stdscr.addstr(y, x, pies["Imie"])
                self.stdscr.attroff(curses.color_pair(1))
            else:
                self.stdscr.addstr(y, x, pies["Imie"])

        self.stdscr.refresh()

    def display_pies_info(self, pies_info):
        self.stdscr.clear()
        h, w = self.stdscr.getmaxyx()

        y = h // 2 - len(pies_info) // 2
        x = w // 2 - max(len(key) for key in pies_info) // 2

        for key, value in pies_info.items():
            self.stdscr.addstr(y, x, f"{key}: {value}")
            y += 1

        self.stdscr.refresh()
        self.stdscr.getch()

    def get_psy(self, psy):
        selected_row = 0
        while True:
            self.display_pies(psy, selected_row)
            key = self.stdscr.getch()

            if key == curses.KEY_DOWN and selected_row < len(psy) - 1:
                selected_row += 1
            elif key == curses.KEY_UP and selected_row > 0:
                selected_row -= 1
            elif key == 10:  # Enter key
                if selected_row == len(psy) - 1:  # Ostatnia opcja (Powrot do menu)
                    break
                else:
                    chosen_pies = psy[selected_row]
                    self.display_pies_info(chosen_pies)
                    self.stdscr.getch()  # Oczekiwanie na naciśnięcie klawisza przed powrotem do menu
            elif key == 27:  # Escape key
                break

    
    def display_message(self, message):
        self.stdscr.clear()
        height, width = self.stdscr.getmaxyx()

        y = height // 2
        x = width // 2 - len(message) // 2

        self.stdscr.addstr(y, x, message)

        self.stdscr.refresh()
        self.stdscr.getch()  


    def display_schronisko_info(self, shelter_info):
        self.stdscr.clear()
        h, w = self.stdscr.getmaxyx()

        y = h // 2 - len(shelter_info) // 2
        x = 2

        for key, value in shelter_info.items():
            self.stdscr.addstr(y, x, f"{key}: {value}")
            y += 1

        self.stdscr.refresh()
        self.stdscr.getch()

    def display_shelters(self, schroniska, selected_row):
        self.stdscr.clear()
        h, w = self.stdscr.getmaxyx()

        for index, schronisko in enumerate(schroniska, start=1):
            miasto = schronisko["Miasto"]
            x = w // 2 - len(miasto) // 2
            y = h // 2 - len(schroniska) // 2 + index - 1
            if index - 1 == selected_row:
                self.stdscr.attron(curses.color_pair(1))
                self.stdscr.addstr(y, x, miasto)
                self.stdscr.attroff(curses.color_pair(1))
            else:
                self.stdscr.addstr(y, x, miasto)

        self.stdscr.refresh()
   
    def get_user_input(self, prompt):
        curses.echo()
        self.stdscr.addstr(self.height - 1, 0, prompt)
        user_input = self.stdscr.getstr().decode(self.stdscr.encoding)
        curses.noecho()
        return user_input

    import curses



    def display_adoption_form(self, questions):
        answers = [""] * len(questions)  # Inicjalizacja listy odpowiedzi
        current_question = 0

        while current_question < len(questions):
            self.stdscr.clear()
            h, w = self.stdscr.getmaxyx()

            # Wyświetlanie wszystkich pytań i odpowiedzi
            for i in range(len(questions)):
                y = h // 2 - len(questions) + i * 2
                # Aktualne pytanie jest podświetlane
                if i == current_question:
                    self.stdscr.attron(curses.color_pair(1))
                    self.stdscr.addstr(y, 2, f"{questions[i]}: {answers[i]}")
                    self.stdscr.attroff(curses.color_pair(1))
                else:
                    self.stdscr.addstr(y, 2, f"{questions[i]}: {answers[i]}")

            self.stdscr.refresh()

            key = self.stdscr.getch()

            if key == 10:  # Enter key
                # Dodaj sprawdzanie ograniczeń dla wieku i numeru telefonu
                if current_question == 4:  # Wiek
                    try:
                        age = int(answers[current_question])
                        if age < 0:
                            raise ValueError("Wiek nie może być ujemny.")
                    except ValueError:
                        self.display_message("Wprowadź poprawny wiek (liczbę dodatnią).")
                        continue
                elif current_question == 3:  # Numer telefonu
                    phone_number = answers[current_question]
                    if not phone_number.isdigit() or len(phone_number) != 9:
                        self.display_message("Numer telefonu powinien składać się z 9 cyfr.")
                        continue

                current_question += 1
            elif key == 27:  # Escape key
                break
            elif key == curses.KEY_BACKSPACE:
                answers[current_question] = answers[current_question][:-1]
            elif key == 9:  # Tab key
                current_question = max(0, current_question - 1)  # Nie schodzimy poniżej pierwszego pytania
            else:
                answers[current_question] += chr(key)

        return answers




    def display_adoption_success(self):
        self.stdscr.clear()
        h, w = self.stdscr.getmaxyx()
        message = "Formularz adopcyjny został złożony. Dziękujemy!"
        self.stdscr.addstr(h // 2, w // 2 - len(message) // 2, message)
        self.stdscr.refresh()
        self.stdscr.getch()

