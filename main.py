import tkinter as tk
from tkinter import simpledialog
import csv

# Function to display the form for entering new contact details
def enter_new_number():
    global name_entry, country_entry, phone_entry

    # Create a new window for the form
    form_window = tk.Toplevel(root)
    form_window.title("Enter New Number")

    # Create and pack form entries
    tk.Label(form_window, text="Name:").pack(pady=5)
    name_entry = tk.Entry(form_window)
    name_entry.pack(pady=5)

    tk.Label(form_window, text="Country:").pack(pady=5)
    country_entry = tk.Entry(form_window)
    country_entry.pack(pady=5)

    tk.Label(form_window, text="Phone Number:").pack(pady=5)
    phone_entry = tk.Entry(form_window)
    phone_entry.pack(pady=5)

    # Create and pack the submit button
    submit_button = tk.Button(form_window, text="Submit", command=add_contact)
    submit_button.pack(pady=10)

# Function to add a new contact to the CSV file
def add_contact():
    name = name_entry.get()
    country = country_entry.get()
    phone_number = phone_entry.get()

    # Open the CSV file in append mode and write the new contact details
    with open("contacts.csv", mode="a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, country, phone_number])

    # Close the form window after submitting
    form_window.destroy()

    # Display a success message
    tk.messagebox.showinfo("Success", "Contact added successfully!")

# Function to display a list of names and allow selection to view contact details
def show_names():
    with open("contacts.csv", mode="r") as file:
        reader = csv.reader(file)
        contacts = list(reader)

    # Create a new window for displaying names
    names_window = tk.Toplevel(root)
    names_window.title("Contact Names")

    # Create and pack a listbox with names
    listbox = tk.Listbox(names_window)
    for contact in contacts:
        listbox.insert(tk.END, contact[0])
    listbox.pack(pady=10)

    # Function to show contact details when a name is selected
    def show_contact_details(event):
        selected_name = listbox.get(listbox.curselection())
        for contact in contacts:
            if contact[0] == selected_name:
                details = f"Name: {contact[0]}\nCountry: {contact[1]}\nPhone Number: {contact[2]}"
                tk.messagebox.showinfo("Contact Details", details)

    # Bind the selection event to the function
    listbox.bind("<<ListboxSelect>>", show_contact_details)

# Create the main window
root = tk.Tk()
root.title("Contact Management System")

# Create and pack a label with the welcome message
tk.Label(root, text="Welcome to the Contact Management System").pack(pady=10)

# Create and pack a button to enter a new number
enter_button = tk.Button(root, text="Enter New Number", command=enter_new_number)
enter_button.pack(pady=10)

# Create and pack a button to show names
show_names_button = tk.Button(root, text="Show Names", command=show_names)
show_names_button.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()
