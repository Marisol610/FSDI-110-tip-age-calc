#imports
from menu import print_menu, print_header, clear
from homework import calculate_age, calculate_tip
#global variables

#functions



def register_product():
    print_header("Register a new Product")
    #title, category, stock, price
    title= input("Please provide the Title:")
    category = input("Please provide the Category")
    stock = input("Please provide the Stock Qty:")
    price = input("Please provide the Price:")




#intructions

opc= ''
while(opc != 'x'):
    clear()
    print_menu()
    opc = input("Please choose an option:")


    #compare based on the user option
    if(opc == "1"): # compare strings with strings
        register_product()

    elif(opc == 'a'):
        calculate_age()
    elif(opc == 'b'):
        calculate_tip()

print("Good bye!!")