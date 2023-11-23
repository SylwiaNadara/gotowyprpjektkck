
import curses
from model import DogModel
from view import DogView
from controler import DogController

def main(stdscr): 
    model = DogModel()
    view = DogView(stdscr)
    controller = DogController(model, view)
    controller.run()
    
if __name__ == '__main__':
    curses.wrapper(main)

