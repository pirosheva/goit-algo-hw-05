def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter user name."
    return inner

@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_username_phone(args, contacts):
    name, phone = args
    for contact in contacts:
        if contact == name:
            contacts[contact] = phone
            return "Contact changed"
    return "Contact not finded"

@input_error
def print_phone_username(args, contacts):
    name = args[0]
    return contacts.get(name)

@input_error
def show_all(contacts):
    for contact in contacts:
        print(contact + " " + contacts[contact])

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_username_phone(args, contacts))
        elif command == "phone":
            print(print_phone_username(args, contacts))
        elif command == "all":
            show_all(contacts)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
