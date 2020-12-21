

def print_menu():
    print("*" * 40)
    print("   Welcome to PyWarehouse   ")
    print("*" * 40)

    print("[1] Register Product")
    print("[2] View Catalog")

    print("[a] Calculate age")
    print("[b] Calculate Tip")

    print(" [x] Close the system")

def print_header(header_text):
    clear()
    print('_' * 40)
    print(header_text)
    print('_' * 40)


def clear():
    print("\n\n\n\n\n")
