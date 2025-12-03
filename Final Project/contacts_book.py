import json
from typing import List, Optional

from contact import Contact
from logger import SimpleLogger


class ContactsBook:
    
    def __init__(self, file_path: str = "contacts.json", logger: Optional[SimpleLogger] = None) -> None:
        self.__file_path = file_path
        self.__contacts: List[Contact] = []
        self.__logger = logger or SimpleLogger()
        self.load_from_file()

    def add_contact(self, name: str, phone: str, email: str) -> None:
        
        name = name.strip()
        phone = phone.strip()
        email = email.strip()

        if not name:
            raise ValueError("Name cannot be empty.")
        if not phone:
            raise ValueError("Phone cannot be empty.")
        
        if email and "@" not in email:
            raise ValueError("Email is invalid.")

        contact = Contact(name, phone, email)
        self.__contacts.append(contact)
        self.__logger.log(f"Added contact: {name}")
        self.save_to_file()

    def list_contacts(self) -> List[Contact]:
        
        return list(self.__contacts)

    def search_by_name(self, query: str) -> List[Contact]:
        
        query = query.lower().strip()
        return [c for c in self.__contacts if query in c.name.lower()]

    def delete_contact(self, index: int) -> None:
        
        if index < 0 or index >= len(self.__contacts):
            raise IndexError("Contact index out of range.")

        contact = self.__contacts.pop(index)
        self.__logger.log(f"Deleted contact: {contact.name}")
        self.save_to_file()

    def load_from_file(self) -> None:
        
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.__contacts = [Contact.from_dict(item) for item in data]
            self.__logger.log("Loaded contacts from file.")
        except FileNotFoundError:
            
            self.__contacts = []
            self.__logger.log("Contacts file not found, starting with an empty book.")
        except (json.JSONDecodeError, OSError) as e:
            print(f"Error reading contacts file: {e}")
            self.__logger.log(f"Error reading contacts file: {e}")
            self.__contacts = []

    def save_to_file(self) -> None:
        
        try:
            data = [c.to_dict() for c in self.__contacts]
            with open(self.__file_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            self.__logger.log("Saved contacts to file.")
        except OSError as e:
            print(f"Error saving contacts: {e}")
            self.__logger.log(f"Error saving contacts: {e}")
