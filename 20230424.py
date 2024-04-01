#내장클래스 확장

class ContactList(list["Contact"]):
    def search(self, name:str)->list["Contact"]:
        matching_contacts : list["Contact"] = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
            return matching_contacts


class Contact:
    all_contacts = ContactList()

    def __init__(self,name:str, email:str) -> None :
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

    def __repr__(self)-> str:
        return f'이름;{self.name} ,이메일{self.email}'

if __name__ =='__main__':
    contacts = Contact
