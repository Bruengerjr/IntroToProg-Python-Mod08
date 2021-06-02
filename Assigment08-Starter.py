# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# Bruenger,6/1/21,Added Product Class
# Bruenger,6/1/21,Added Menu Code and code for options 1,2,3.
# Bruegner,6/2/21,Got as far as I could before running out of time.
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []


class Product():
    # Fields
    strName = ""
    fltPrice = ""

    def __init__(self, name, price):
        self.strName = name
        self.fltPrice = price


objP1 = Product("Cool Thing", 50)

"""Stores data about a product:

    properties:
        product_name: (string) with the product's  name
        product_price: (float) with the product's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <Your Name>,<Today's Date>,Modified code to complete assignment 8
    """
pass
# Data -------------------------------------------------------------------- #


# Processing  ------------------------------------------------------------- #
def read_data_from_file(list_of_rows):
    """ Reads data from a file into a list of dictionary rows

    :param file_name: (string) with name of file:
    :param list_of_rows: (list) you want filled with file data:
    :return: (list) of dictionary rows
    """
    list_of_rows.clear()  # clear current data
    file = open(strFileName, "r")
    for line in file:
        name, price = line.split(",")
        row = {"Name": name.strip(), "Price": price.strip()}
        list_of_rows.append(row)
    file.close()
    return list_of_rows, 'Success'


def write_data_to_file(list_of_rows):
    objFile = open(strFileName, "w")
    for row in lstOfProductObjects:
        objFile.write(row["Name"] + ',' + row["Price"] + '\n')
    objFile.close()
    # print("\tData saved to file!")


class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <Your Name>,<Today's Date>,Modified code to complete assignment 8
    """
    pass


# Processing  ------------------------------------------------------------- #


# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    # TODO: Add docstring
    pass

    @staticmethod
    def print_menu_products():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new Product
        2) Save Data to File        
        3) Reload Data from File
        4) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def print_current_products_in_list(list_of_rows):
        """ Shows the current Products in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current Products ToDo are: *******")
        for row in list_of_rows:
            print(row["Name"] + " (" + row["Price"] + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user

        :return: string
        """
        return str(input(message)).strip().lower()

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')


    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    # TODO: Add code to show the current data from the file to user

    @staticmethod
    def input_new_product():
        strName = input("Enter a Name: ")
        strPrice = input("Enter a Price: ")
        dicRow = {"Name": strName, "Price": strPrice}
        lstOfProductObjects.append(dicRow)
        dicRow = str(dicRow).replace("{", "(")
        dicRow = str(dicRow).replace("}", ")")
        dicRow = str(dicRow).replace("'", "")
        print()
        print("\t The record " + dicRow + " was added!")

# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
while(True):
    # Step 3 Show current data
    IO.print_menu_products()  # Shows menu
    strChoice = IO.input_menu_choice()  # Get menu option

    # Step 4 - Process user's menu choice
    if strChoice.strip() == '1':  # Add a new Product
        IO.input_new_product()
        IO.input_press_to_continue()
        continue  # to show the menu

    elif strChoice == '2':   # Save Data to File
        strChoice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")
        if strChoice.lower() == "y":
            write_data_to_file(lstOfProductObjects)
            IO.input_press_to_continue()
        else:
            IO.input_press_to_continue("Save Cancelled!")
        continue  # to show the menu

    elif strChoice == '3':  # Reload Data from File
        print("Warning: Unsaved Data Will Be Lost!")
        strChoice = IO.input_yes_no_choice("Are you sure you want to reload data from file? (y/n) -  ")
        if strChoice.lower() == 'y':
            read_data_from_file(strFileName)  # read file data
            IO.input_press_to_continue()
        else:
            IO.input_press_to_continue("File Reload Cancelled!")
        continue  # to show the menu

    elif strChoice == '4':  #  Exit Program
        print("Goodbye!")
        break   # and Exit
# Load data from file into a list of product objects when script starts
# Show user current data in the list of product objects
# Main Body of Script  ---------------------------------------------------- #
