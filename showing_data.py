from tkinter import *
import general
from receiving_input import all_data


def create_display():
    display_data_screen = Tk()
    display_data_screen.title("All Cancellations")
    display_data_screen.geometry("1000x500")
    for i in range(len(general.COL_NAMES)):
        display_data_screen.columnconfigure(i, weight=4)
    return display_data_screen


def show_all_data():
    display_data_screen = create_display()

    for column in general.COL_NAMES:
        col_num = general.COL_NAMES.index(column)
        col_label = Label(display_data_screen, text=column)
        col_label.grid(row=0, column=col_num)

        for row_num in range(len(all_data)):
            cancellation = all_data[row_num]
            value = cancellation[col_num]
            value_label = Label(display_data_screen, text=value)
            value_label.grid(row=row_num + 1, column=col_num)
    display_data_screen.mainloop()



