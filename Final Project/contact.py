class Contact:
  
    def __init__(self, name: str, phone: str, email: str) -> None:
        self.__name = name
        self.__phone = phone
        self.__email = email

    @property
    def name(self) -> str:
        return self.__name

    @property
    def phone(self) -> str:
        return self.__phone

    @property
    def email(self) -> str:
        return self.__email

    def to_dict(self) -> dict:
        
        return {
            "name": self.__name,
            "phone": self.__phone,
            "email": self.__email
        }

    @staticmethod
    def from_dict(data: dict) -> "Contact":
        
        return Contact(
            name=data.get("name", ""),
            phone=data.get("phone", ""),
            email=data.get("email", "")
        )
