from logger import SimpleLogger
from contacts_book import ContactsBook


def print_menu() -> None:
    print("\n--- Simple Contact Book ---")
    print("1. List contacts")
    print("2. Add contact")
    print("3. Search by name")
    print("4. Delete contact")
    print("5. Quit")


def main() -> None:
    logger = SimpleLogger()
    book = ContactsBook(logger=logger)

    while True:
        print_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            contacts = book.list_contacts()
            if not contacts:
                print("No contacts yet.")
            else:
                print("\nContacts:")
                for i, c in enumerate(contacts):
                    print(f"{i}. {c.name} | {c.phone} | {c.email}")

        elif choice == "2":
            print("\nAdd new contact:")
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email (optional): ")
            try:
                book.add_contact(name, phone, email)
                print("Contact added.")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "3":
            query = input("Search name: ")
            results = book.search_by_name(query)
            if not results:
                print("No matching contacts.")
            else:
                print("\nSearch results:")
                for i, c in enumerate(results):
                    print(f"{i}. {c.name} | {c.phone} | {c.email}")

        elif choice == "4":
            contacts = book.list_contacts()
            if not contacts:
                print("No contacts to delete.")
                continue

            for i, c in enumerate(contacts):
                print(f"{i}. {c.name} | {c.phone} | {c.email}")

            index_str = input("Enter index of contact to delete: ")
            try:
                index = int(index_str)
                book.delete_contact(index)
                print("Contact deleted.")
            except ValueError:
                print("Please enter a valid number.")
            except IndexError as e:
                print(f"Error: {e}")

        elif choice == "5":
            print("Goodbye!")
            logger.log("Application exited.")
            break

        else:
            print("Invalid choice. Please enter a number 1-5.")


if __name__ == "__main__":
    main()
