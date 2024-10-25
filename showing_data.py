from tkinter import *
import pandas as pd
from openpyxl.workbook import Workbook

import consts
from receiving_input import all_data




def create_display():
    display_data_screen = Tk()
    display_data_screen.title("All Cancellations")
    display_data_screen.geometry("1000x500")
    for i in range(len(consts.COL_NAMES)):
        display_data_screen.columnconfigure(i, weight=4)
    return display_data_screen


def show_all_data():
    display_data_screen = create_display()

    for column in consts.COL_NAMES:
        col_num = consts.COL_NAMES.index(column)
        col_label = Label(display_data_screen, text=column)
        col_label.grid(row=0, column=col_num)

        for row_num in range(len(all_data)):
            cancellation = all_data[row_num]
            value = cancellation[column]
            value_label = Label(display_data_screen, text=value)
            value_label.grid(row=row_num + 1, column=col_num)
    display_data_screen.mainloop()


def save_all_data_in_excel(): #not working yet
    df = pd.DataFrame(all_data)
    df._append().to_excel(consts.EXCEL_NAME, index=False)


def create_data_frame(): # unassigned
    df2 = pd.DataFrame(all_data)
