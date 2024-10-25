from tkinter import Entry, Button

from tkcalendar import DateEntry

EXCEL_NAME = "all_cancellations.xlsx"

COL_NAMES = ["First Name", "Second Name", "Order Number", "Location", "Destination", "Airline", "Potential Refund",
             "Cancellation Date", "Flight Date"]

SUBMIT = "Submit"

FIRST_NAME = COL_NAMES[0]
SECOND_NAME = COL_NAMES[1]
ORDER_NUM = COL_NAMES[2]
LOCATION = COL_NAMES[3]
DESTINATION = COL_NAMES[4]
AIRLINE = COL_NAMES[5]
REFUND = COL_NAMES[6]
CANCEL_DATE = COL_NAMES[7]
FLIGHT_DATE = COL_NAMES[8]



ADDING_BUTTON = 1
SHOWING_BUTTON = 2
EXIT_BUTTON = 3

def entry_settings(screen_name):
    return Entry(screen_name, width=20, font=('Arial', 10))


def date_settings(screen_name):
    return DateEntry(screen_name, selectmode="day", date_pattern="dd-mm-yyyy")



