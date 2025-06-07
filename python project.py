import tkinter as tk
from tkinter import messagebox
class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"{self.name} | {self.phone} | {self.email}"

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def get_all_contacts(self):
        return self.contacts

class ContactBookGUI:
    def __init__(self, root):
        self.contact_book = ContactBook()

        self.root = root
        self.root.title("Contact Book")

        tk.Label(root, text="Name").grid(row=0, column=0)
        tk.Label(root, text="Phone").grid(row=1, column=0)
        tk.Label(root, text="Email").grid(row=2, column=0)

        self.name_entry = tk.Entry(root)
        self.phone_entry = tk.Entry(root)
        self.email_entry = tk.Entry(root)

        self.name_entry.grid(row=0, column=1)
        self.phone_entry.grid(row=1, column=1)
        self.email_entry.grid(row=2, column=1)

        tk.Button(root, text="Add Contact", command=self.add_contact).grid(row=3, column=0, pady=10)
        tk.Button(root, text="Show Contacts", command=self.show_contacts).grid(row=3, column=1, pady=10)

        self.contacts_listbox = tk.Listbox(root, width=50)
        self.contacts_listbox.grid(row=4, column=0, columnspan=2)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()

        if name and phone and email:
            contact = Contact(name, phone, email)
            self.contact_book.add_contact(contact)
            messagebox.showinfo("Success", "Contact added successfully!")
            self.clear_entries()
        else:
            messagebox.showwarning("Input Error", "Please fill in all fields")

    def show_contacts(self):
        self.contacts_listbox.delete(0, tk.END)
        for contact in self.contact_book.get_all_contacts():
            self.contacts_listbox.insert(tk.END, str(contact))

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookGUI(root)
    root.mainloop()
