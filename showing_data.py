from tkinter import *
import pandas as pd
from openpyxl.workbook import Workbook

from receiving_input import all_data


COL_NAMES = ["First Name", "Second Name", "Order Number", "Location", "Destination", "Airline", "Potential Refund",
             "Cancellation Date", "Flight Date"]
# all_data = [
#     {'First Name': '1', 'Second Name': '2', 'Order Number': '3', 'Location': '4', 'Destination': '5', 'Airline': '6',
#      'Potential Refund': '7', 'Cancellation Date': '24-10-2024', 'Flight Date': '24-10-2024'},
#     {'First Name': '1', 'Second Name': '2', 'Order Number': '3', 'Location': '4', 'Destination': '5', 'Airline': '6',
#      'Potential Refund': '7', 'Cancellation Date': '24-10-2024', 'Flight Date': '24-10-2024'}]


def create_display():
    display_data_screen = Tk()
    display_data_screen.title("All Cancellations")
    display_data_screen.geometry("1000x500")
    for i in range(len(COL_NAMES)):
        display_data_screen.columnconfigure(i, weight=4)
    return display_data_screen




def show_all_data():
    display_data_screen = create_display()

    for column in COL_NAMES:
        col_num = COL_NAMES.index(column)
        col_label = Label(display_data_screen, text=column)
        col_label.grid(row=0, column=col_num)

        for row_num in range(len(all_data)):
            cancellation = all_data[row_num]
            value = cancellation[column]
            value_label = Label(display_data_screen, text=value)
            value_label.grid(row=row_num + 1, column=col_num)
    display_data_screen.mainloop()

def save_all_data_in_excel():
    df = pd.DataFrame(all_data)
    df.to_excel("all_cancellations.xlsx", index =False)
