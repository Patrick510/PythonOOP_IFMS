class Contact:
    all_contacts = [] 
    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

class Supplier(Contact):
        def order(self, order):
            print(f"If this were a real system we would send '{order}' order to '{self.name}'")

class ContactList(list):
    def search(self, name):
        """Return all contacts that contain the search value in their name."""
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts

class Friend(Contact):
        def __init__(self, name, email, phone):
            super().__init__(name, email) # chama o método __init__ pai
            self.phone = phone

class MailSender:
    def send_mail(self, message):
        print("Sending mail to " + self.email)
        # Add e-mail logic here

class EmailableContact(Contact, MailSender):
    pass
