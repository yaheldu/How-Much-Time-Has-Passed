from tkinter import *
import general


def initialize_all_data():
    # importing all data from Excel sheet
    all_data = []
    wb, sheet = general.loading_excel_sheet()
    row_num = sheet.max_row
    col_num = len(general.COL_NAMES)
    for row in range(2, row_num + 1):
        row_lst = []
        for column in range(1, col_num + 1):
            row_lst += [sheet.cell(row=row, column=column).value]
        all_data += [row_lst]
    return all_data


all_data = initialize_all_data()


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
    first_name_label = Label(receive_info_screen, text=general.FIRST_NAME)
    first_name_label.grid(row=1, column=0)
    first_name_entry = general.entry_settings(receive_info_screen)
    first_name_entry.grid(row=1, column=1)

    # asking for second name
    second_name_label = Label(receive_info_screen, text=general.SECOND_NAME)
    second_name_label.grid(row=3, column=0)
    second_name_entry = general.entry_settings(receive_info_screen)
    second_name_entry.grid(row=3, column=1)

    # asking for order number
    order_label = Label(receive_info_screen, text=general.ORDER_NUM)
    order_label.grid(row=5, column=0)
    order_entry = general.entry_settings(receive_info_screen)
    order_entry.grid(row=5, column=1)

    # asking for location
    location_label = Label(receive_info_screen, text=general.LOCATION)
    location_label.grid(row=7, column=0)
    location_entry = general.entry_settings(receive_info_screen)
    location_entry.grid(row=7, column=1)

    # asking for destination
    destination_label = Label(receive_info_screen, text=general.DESTINATION)
    destination_label.grid(row=9, column=0)
    destination_entry = general.entry_settings(receive_info_screen)
    destination_entry.grid(row=9, column=1)

    # asking for airline
    airline_label = Label(receive_info_screen, text=general.AIRLINE)
    airline_label.grid(row=11, column=0)
    airline_entry = general.entry_settings(receive_info_screen)
    airline_entry.grid(row=11, column=1)

    # asking for refund
    refund_label = Label(receive_info_screen, text=general.REFUND)
    refund_label.grid(row=13, column=0)
    refund_entry = general.entry_settings(receive_info_screen)
    refund_entry.grid(row=13, column=1)

    # asking for cancellation date
    cancellation_date_label = Label(receive_info_screen, text=general.CANCEL_DATE)
    cancellation_date_label.grid(row=15, column=0)
    cancellation_date_input = general.date_settings(receive_info_screen)
    cancellation_date_input.grid(row=16, column=0)

    # asking for flight date
    flight_date_label = Label(receive_info_screen, text=general.FLIGHT_DATE)
    flight_date_label.grid(row=15, column=1)
    flight_date_input = general.date_settings(receive_info_screen)
    flight_date_input.grid(row=16, column=1)

    def get_all_data():
        data_list = [first_name_entry.get(),
                     second_name_entry.get(),
                     order_entry.get(),
                     location_entry.get(),
                     destination_entry.get(),
                     airline_entry.get(),
                     refund_entry.get(),
                     cancellation_date_input.get(),
                     flight_date_input.get()]
        all_data.append(data_list)
        general.adding_to_excel(data_list)
        receive_info_screen.destroy()
        return all_data

    # submit button

    submit_button = Button(receive_info_screen, width=10, text=general.SUBMIT, command=get_all_data)

    submit_button.grid(row=17, columnspan=2)

    receive_info_screen.mainloop()
