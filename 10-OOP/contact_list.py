from contact import Contact

class ContactList:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def display_contacts(self):
        for contact in self.contacts:
            print(f"{contact.name}\t{contact.email}\t{contact.telephone}")
