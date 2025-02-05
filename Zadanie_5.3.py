
# Zadanie: wizytówki

# Dysponujesz już całkiem rozbudowanym programem do obsługi wizytówek. Po dodaniu kilku elementów wyślij go Mentorowi.

#     Używając dziedziczenia, rozdziel podstawową klasę wizytówki na dwie osobne: pierwsza (BaseContact) powinna przechowywać podstawowe dane kontaktowe takie jak imię, nazwisko, telefon, adres e-mail. Za pomocą kolejnej klasy (BusinessContact) rozszerz klasę bazową o przechowywanie informacji związanych z pracą danej osoby – stanowisko, nazwa firmy, telefon służbowy.
#     Oba typy wizytówek, powinny oferować metodę contact(), która wyświetli na konsoli komunikat w postaci “Wybieram numer +48 123456789 i dzwonię do Jan Kowalski”. Wizytówka firmowa powinna wybierać służbowy numer telefonu, a wizytówka bazowa prywatny.
#     Oba typy wizytówek powinny mieć dynamiczny atrybut label_length, który zwraca długość imienia i nazwiska danej osoby.
#     Stwórz funkcję create_contacts, która będzie potrafiła komponować losowe wizytówki. Niech ta funkcja przyjmuje dwa parametry: rodzaj wizytówki oraz ilość. Wykorzystaj bibliotekę faker do generowania danych.

from faker import Faker

#Klasa do tworzenia wizytówki prywatnej
class BaseContact:
    def __init__(self, first_name, last_name, private_phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.private_phone = private_phone
        self.email = email
        
    def __str__(self):
        return f"{self.first_name}, {self.last_name}, {self.email}"
    
    def contact(self):
        return f"Wybieram numer {self.private_phone} i dzwonię do {self.first_name} {self.last_name}"
   
    @property
    def label_length(self):
        return len(self.first_name) + len(self.last_name)
    

#Klasa do tworzenia wizytówki firmowej
class BusinessContact(BaseContact):
    def __init__(self, first_name, last_name, private_phone, email, position, company_name, company_phone):
        super().__init__(first_name, last_name, private_phone, email)
        self.position = position
        self.company_name = company_name
        self.company_phone = company_phone
    
    def contact(self):
        return f"Wybieram numer {self.company_phone} i dzwonię do {self.first_name} {self.last_name}"
    
    @property  #CZy jestesmy w stanie zrobic bez kopiowania ?
    def label_length(self):
        return len(self.first_name) + len(self.last_name)


# Funkcja tworzenia wizytówek
def create_contacts(contact_type, number_of_contacts):
    fake = Faker()
    contacts = []
    
    for _ in range(number_of_contacts):
        first_name = fake.first_name()
        last_name = fake.last_name()
        private_phone = fake.phone_number()
        email = fake.email()
        
        # Tworzymy BaseContact lub BusinessContact w zależności od parametru contact_type
        if contact_type == "base":
            contact = BaseContact(first_name, last_name, private_phone, email)
        elif contact_type == "business":
            position = fake.job()
            company_name = fake.company()
            company_phone = fake.phone_number()
            contact = BusinessContact(first_name, last_name, private_phone, email, position, company_name, company_phone)
        else:
            raise ValueError("Invalid contact type. Use 'base' or 'business'.")
        
        contacts.append(contact)
    
    return contacts

#  Testowanie funkcji
base_contacts = create_contacts("base", 5)
business_contacts = create_contacts("business", 3)

# Wyświetlamy wygenerowane wizytówki
print("Base Contacts:")
for contact in base_contacts:
    print(contact, f"       Długość Imienia i Nazwiska wynosi: {contact.label_length}")
    print(contact.contact())  # Wyświetlanie metody kontaktu
    print(" ")
print("                               ")

print("\nBusiness Contacts:")
for contact in business_contacts:
    print(contact, f"      Długość Imienia i Nazwiska wynosi:: {contact.label_length}")  # Wyświetlanie długości imienia i nazwiska)
    print(contact.contact())  # Wyświetlanie metody kontaktu
    print(" ")
