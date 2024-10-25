# home screen
from tkinter import *
import smtplib as smt
import consts

all_data = []


def create_display():
    receive_info_screen = Tk()
    receive_info_screen.title("New Cancellation")
    receive_info_screen.geometry("500x500")
    receive_info_screen.columnconfigure(0, weight=1)
    receive_info_screen.columnconfigure(1, weight=1)
    return receive_info_screen


def add_new_reservation():
    receive_info_screen = create_display()

    # asking for first name
    first_name_label = Label(receive_info_screen, text=consts.FIRST_NAME)
    first_name_label.grid(row=1, column=0)
    first_name_entry = consts.entry_settings(receive_info_screen)
    first_name_entry.grid(row=1, column=1)

    # asking for second name
    second_name_label = Label(receive_info_screen, text=consts.SECOND_NAME)
    second_name_label.grid(row=3, column=0)
    second_name_entry = consts.entry_settings(receive_info_screen)
    second_name_entry.grid(row=3, column=1)

    # asking for order number
    order_label = Label(receive_info_screen, text=consts.ORDER_NUM)
    order_label.grid(row=5, column=0)
    order_entry = consts.entry_settings(receive_info_screen)
    order_entry.grid(row=5, column=1)

    # asking for location
    location_label = Label(receive_info_screen, text=consts.LOCATION)
    location_label.grid(row=7, column=0)
    location_entry = consts.entry_settings(receive_info_screen)
    location_entry.grid(row=7, column=1)

    # asking for destination
    destination_label = Label(receive_info_screen, text=consts.DESTINATION)
    destination_label.grid(row=9, column=0)
    destination_entry = consts.entry_settings(receive_info_screen)
    destination_entry.grid(row=9, column=1)

    # asking for airline
    airline_label = Label(receive_info_screen, text=consts.AIRLINE)
    airline_label.grid(row=11, column=0)
    airline_entry = consts.entry_settings(receive_info_screen)
    airline_entry.grid(row=11, column=1)

    # asking for refund
    refund_label = Label(receive_info_screen, text=consts.REFUND)
    refund_label.grid(row=13, column=0)
    refund_entry = consts.entry_settings(receive_info_screen)
    refund_entry.grid(row=13, column=1)

    # asking for cancellation date
    cancellation_date_label = Label(receive_info_screen, text=consts.CANCEL_DATE)
    cancellation_date_label.grid(row=15, column=0)
    cancellation_date_input = consts.date_settings(receive_info_screen)
    cancellation_date_input.grid(row=16, column=0)

    # asking for flight date
    flight_date_label = Label(receive_info_screen, text=consts.FLIGHT_DATE)
    flight_date_label.grid(row=15, column=1)
    flight_date_input = consts.date_settings(receive_info_screen)
    flight_date_input.grid(row=16, column=1)

    def get_all_data():
        data_dict = {consts.FIRST_NAME: first_name_entry.get(),
                     consts.SECOND_NAME: second_name_entry.get(),
                     consts.ORDER_NUM: order_entry.get(),
                     consts.LOCATION: location_entry.get(),
                     consts.DESTINATION: destination_entry.get(),
                     consts.AIRLINE: airline_entry.get(),
                     consts.REFUND: refund_entry.get(),
                     consts.CANCEL_DATE: cancellation_date_input.get(),
                     consts.FLIGHT_DATE: flight_date_input.get()}
        all_data.append(data_dict)
        receive_info_screen.destroy()
        return all_data

    # submit button

    submit_button = Button(receive_info_screen, width=10, text=consts.SUBMIT, command=get_all_data)

    submit_button.grid(row=17, columnspan=2)

    receive_info_screen.mainloop()


# add_new_reservation()

# print(all_data)
