import tkinter as tk
from tkinter import messagebox

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.contacts = {}

        # Create GUI components
        self.name_label = tk.Label(root, text="Name")
        self.name_label.grid(row=0, column=0)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1)

        self.phone_label = tk.Label(root, text="Phone")
        self.phone_label.grid(row=1, column=0)
        self.phone_entry = tk.Entry(root)
        self.phone_entry.grid(row=1, column=1)

        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=2, column=0, columnspan=2)

        self.display_button = tk.Button(root, text="Display Contacts", command=self.display_contacts)
        self.display_button.grid(row=3, column=0, columnspan=2)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        if name and phone:
            self.contacts[name] = phone
            messagebox.showinfo("Success", "Contact added successfully!")
            self.name_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter both name and phone number.")

    def display_contacts(self):
        contacts_str = "\n".join([f"{name}: {phone}" for name, phone in self.contacts.items()])
        messagebox.showinfo("Contacts", contacts_str if contacts_str else "No contacts available.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()
