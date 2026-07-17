# This program uses a function to create a list
# the fuction returns a reference to the list.

def main():
    # get a list with values stored in it
    numbers = get_values()

    #Displays the values in the list
    print('the numbers in the list are:')
    print(numbers)

# The get_values function gets a series of numbers
# from the user and stores them in a list
# The function returns a relerence to the list

def get_values():
    #creates an emplty list
    values = []
    #variable to control the loop
    again = 'y'

    # gets values from user to add to the list
    while again == 'y':
        #gets a number and adds it to the list
        num = int(input('Enter a number: '))
        values.append(num)

        # asks to input again
        print('Do you want to add another number?')
        print('Type y for yes')
        again = input('y = yes, anything else = no: ')
        print()

    # returns the list
    return values

# calls main function
main()      
