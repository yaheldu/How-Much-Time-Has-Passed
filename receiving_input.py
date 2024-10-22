# home screen
from tkinter import *
from tkcalendar import DateEntry
import pandas as pd
import smtplib as smt

# taking input screen
screen = Tk()
screen.title("Cancellations")
screen.geometry("500x500")
screen.columnconfigure(0, weight=1)
screen.columnconfigure(1, weight=1)

# asking for first name
first_name_label = Label(screen, text="First Name:")
first_name_label.grid(row=1, column=0)
first_name_entry = Entry(screen, width=20, font=('Arial', 10))
first_name_entry.grid(row=1, column=1)

# asking for second name
second_name_label = Label(screen, text="Second Name:")
second_name_label.grid(row=3, column=0)
second_name_entry = Entry(screen, width=20, font=('Arial', 10))
second_name_entry.grid(row=3, column=1)

# asking for order number
order_label = Label(screen, text="Order Number:")
order_label.grid(row=5, column=0)
order_entry = Entry(screen, width=20, font=('Arial', 10))
order_entry.grid(row=5, column=1)

# asking for location
location_label = Label(screen, text="Location:")
location_label.grid(row=7, column=0)
location_entry = Entry(screen, width=20, font=('Arial', 10))
location_entry.grid(row=7, column=1)

# asking for destination
destination_label = Label(screen, text="Destination:")
destination_label.grid(row=9, column=0)
destination_entry = Entry(screen, width=20, font=('Arial', 10))
destination_entry.grid(row=9, column=1)

# asking for airline
airline_label = Label(screen, text="Airline:")
airline_label.grid(row=11, column=0)
airline_entry = Entry(screen, width=20, font=('Arial', 10))
airline_entry.grid(row=11, column=1)

# asking for refund
refund_label = Label(screen, text="Potential Refund:")
refund_label.grid(row=13, column=0)
refund_entry = Entry(screen, width=20, font=('Arial', 10))
refund_entry.grid(row=13, column=1)

# asking for cancellation date
cancellation_date_label = Label(screen, text="Cancellation Date:")
cancellation_date_label.grid(row=15, column=0)
cancellation_date_input = DateEntry(screen, selectmode="day", date_pattern="dd-mm-yyyy")
cancellation_date_input.grid(row=16, column=0)

# asking for flight date
flight_date_label = Label(screen, text="Flight Date:")
flight_date_label.grid(row=15, column=1)
flight_date_input = DateEntry(screen, selectmode="day", date_pattern="dd-mm-yyyy")
flight_date_input.grid(row=16, column=1)


def get_all_data():
    data_dict = {"First Name": first_name_entry.get(),
                 "Second Name": second_name_entry.get(),
                 "Order Number": order_entry.get(),
                 "Location": location_entry.get(),
                 "Destination": destination_entry.get(),
                 "Airline": airline_entry.get(),
                 "Potential Refund": refund_entry.get(),
                 "Cancellation Date": cancellation_date_input.get(),
                 "Flight Date": flight_date_input.get()}
    return data_dict

# submit button
data_dict = {}
submit_button = Button(screen, text="Submit", command=get_all_data)
submit_button.grid(row=17, column=1)


all_data = pd.DataFrame(data_dict)

print(all_data)

screen.mainloop()

