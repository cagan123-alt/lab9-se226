import mysql.connector
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Please run this code after you created your database and table (run database.py first)
def add_button_clicked():
    dialog = tk.Toplevel(window)
    dialog.title("Add Item")

    dialog_frame = ttk.Frame(dialog, padding=20)
    dialog_frame.pack()

    id_label = ttk.Label(dialog_frame, text="ID:")
    id_label.grid(row=0, column=0, sticky=tk.W)
    id_entry = ttk.Entry(dialog_frame)
    id_entry.grid(row=0, column=1, pady=10)

    movie_label = ttk.Label(dialog_frame, text="Movie:")
    movie_label.grid(row=1, column=0, sticky=tk.W)
    movie_entry = ttk.Entry(dialog_frame)
    movie_entry.grid(row=1, column=1, pady=10)

    date_label = ttk.Label(dialog_frame, text="Date:")
    date_label.grid(row=2, column=0, sticky=tk.W)
    date_entry = ttk.Entry(dialog_frame)
    date_entry.grid(row=2, column=1, pady=10)

    mcu_phase_label = ttk.Label(dialog_frame, text="MCU Phase:")
    mcu_phase_label.grid(row=3, column=0, sticky=tk.W)
    mcu_phase_entry = ttk.Entry(dialog_frame)
    mcu_phase_entry.grid(row=3, column=1, pady=10)

    def ok_button_clicked():
        id_value = id_entry.get()
        movie_value = movie_entry.get()
        date_value = date_entry.get()
        mcu_phase_value = mcu_phase_entry.get()

        if id_value and movie_value and date_value and mcu_phase_value:
            item = [id_value, movie_value, date_value, mcu_phase_value]
            insert_data(item)
            messagebox.showinfo("Success", "Item added to the database.")
            dialog.destroy()
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    ok_button = ttk.Button(dialog_frame, text="Ok", command=ok_button_clicked)
    ok_button.grid(row=4, column=0, pady=10, padx=10)

    def cancel_button_clicked():
        dialog.destroy()  

    cancel_button = ttk.Button(dialog_frame, text="Cancel", command=cancel_button_clicked)
    cancel_button.grid(row=4, column=1, pady=10, padx=10)

def list_all_button_clicked():
    items = select_all_data()
    textbox.delete("1.0", tk.END)
    for item in items:
        item_str = " ".join(str(element) for element in item)
        textbox.insert(tk.END, item_str + "\n")


def insert_data(item):
    cnx = mysql.connector.connect(
        host='localhost',
        port=3310,
        user='root',
        password='your_password',
        database='your_module'
    )
    cursor = cnx.cursor()
    insert_query = "INSERT INTO movies (ID, MOVIE, DATE, MCU_PHASE) VALUES (%s, %s, %s, %s)"
    cursor.execute(insert_query, tuple(item))
    cnx.commit()
    cursor.close()
    cnx.close()


def select_data_by_id(id):
    cnx = mysql.connector.connect(
        host='localhost',
        port=3310,
        user='root',
        password='your_password',
        database='your_module'
    )
    cursor = cnx.cursor()
    select_query = "SELECT * FROM movies WHERE ID = %s"
    cursor.execute(select_query, (id,))
    item = cursor.fetchone()
    cursor.close()
    cnx.close()
    return item


def dropdown_selected(event):
    selected_id = dropdown.get()
    selected_item = select_data_by_id(selected_id)
    textbox.delete("1.0", tk.END)
    if selected_item:
        selected_item_str = " ".join(str(element) for element in selected_item)
        textbox.insert(tk.END, selected_item_str)

def select_all_data():
    cnx = mysql.connector.connect(
        host='localhost',
        port=3310,
        user='root',
        password='your_password',
        database='your_module'
    )
    cursor = cnx.cursor()
    select_query = "SELECT * FROM movies"
    cursor.execute(select_query)
    items = cursor.fetchall()
    cursor.close()
    cnx.close()
    return items
def select_all_ids():
    cnx = mysql.connector.connect(
        host='localhost',
        port=3310,
        user='root',
        password='your_password',
        database='your_module'
    )
    cursor = cnx.cursor()
    select_query = "SELECT ID FROM movies"
    cursor.execute(select_query)
    ids = [str(id[0]) for id in cursor.fetchall()]
    cursor.close()
    cnx.close()
    return ids

window = tk.Tk()
window.title("SE-226 20210601050 project")

frame = ttk.Frame(window, padding=20)
frame.pack()

add_button = ttk.Button(frame, text="Add", command=add_button_clicked)
add_button.grid(row=0, column=0, pady=10)

list_all_button = ttk.Button(frame, text="LIST ALL", command=list_all_button_clicked)
list_all_button.grid(row=0, column=1, pady=10, padx=10)

ids = select_all_ids()
dropdown = ttk.Combobox(frame, values=ids)
dropdown.grid(row=1, column=0, columnspan=2, pady=10)
dropdown.bind("<<ComboboxSelected>>", dropdown_selected)

textbox = tk.Text(frame)
textbox.grid(row=2, column=0, columnspan=2, pady=10)

window.mainloop()
