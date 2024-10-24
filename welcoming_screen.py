from tkinter import *

import receiving_input
from showing_data import show_all_data, save_all_data_in_excel


def create_display():
    welcome_screen = Tk()
    welcome_screen.title("Welcome Screen")
    welcome_screen.geometry("1000x500")
    welcome_screen.columnconfigure(0, weight=1)
    welcome_screen.columnconfigure(1, weight=1)
    welcome_text = Label(welcome_screen, text="Please Choose an Option:")
    welcome_text.config(font=("Courier", 14))
    welcome_text.grid(row=0, columnspan=2)
    return welcome_screen


def which_pressed(button_num):  
    if button_num == ADDING_BUTTON:
        welcome_screen.destroy()
        receiving_input.add_new_reservation()
    if button_num == SHOWING_BUTTON:
        welcome_screen.destroy()
        show_all_data()
    if button_num == EXIT_BUTTON:
        welcome_screen.destroy()
        save_all_data_in_excel()
        global run
        run = False
        return run


def add_buttons(welcome_screen):
    add_new_res = Button(welcome_screen, text="Add New Cancellation", width=20,
                         command=lambda: which_pressed(ADDING_BUTTON))
    add_new_res.grid(row=1, column=0)
    show_all_res = Button(welcome_screen, text="See All Cancellations", width=20,
                          command=lambda: which_pressed(SHOWING_BUTTON))
    show_all_res.grid(row=1, column=1)
    return welcome_screen


def add_exit_button(welcome_screen):
    exit_button = Button(welcome_screen, text="Exit", width=20, command=lambda: which_pressed(EXIT_BUTTON))
    exit_button.grid(row=2, columnspan=2)


run = True
while run:
    ADDING_BUTTON = 1
    SHOWING_BUTTON = 2
    EXIT_BUTTON = 3
    welcome_screen = create_display()
    add_buttons(welcome_screen)
    add_exit_button(welcome_screen)
    welcome_screen.mainloop()
