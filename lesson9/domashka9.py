Contact_book = {}
Exit_list = ["good bye", "close", "exit"]


def main():
    phrase = input().lower()
    while phrase not in Exit_list:
        if phrase.startswith("hello"):
            print("How can I help you?")
        elif "add" in phrase:
            print(add_contact(phrase))
        elif "change" in phrase:
            change_func = change(phrase)
            if change_func != None:
                print(change_func)
        elif "phone" in phrase:
            phone_func = phone(phrase)
            if phone_func != None:
                print(phone_func)        
        elif "show all" in phrase:             
            print(show_all())
        else:
            print("I don't understand the command. Try again.")
        phrase = input().lower()
    return "Good bye!"


def input_error(fn):
    def wrapped(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except Exception as e:
            print("Error:", e)
    return wrapped



def add_contact(phrase):
    phrase_list = phrase.split(' ')
    Contact_book[phrase_list[1].capitalize()] = phrase_list[2]
    return "Done"


@input_error
def change(phrase):
    phrase_list = phrase.split(' ')
    for i in Contact_book:
        if phrase_list[1].capitalize() == i:
            Contact_book[i] = phrase_list[2]
            return "Done"
    raise Exception("No such name")


@input_error
def phone(phrase):
    phrase_list = phrase.split(' ')
    for i in Contact_book:
        if phrase_list[1].capitalize() == i:
            return Contact_book[i]
    raise Exception("No such name")


def show_all():
    return Contact_book


print(main())
