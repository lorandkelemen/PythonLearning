


def format_name(f_name,l_name):
    f_name = f_name.title()
    l_name = l_name.title()
    output = str(f"Hello {f_name} {l_name}")

    return print(output)

first = input("what is your first name? :")
last = input("what is your last name? :")

format_name(first,last)
