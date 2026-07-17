# this program uses a function
# to calculate the total values in a list

def main():
    numbers = [2, 4, 6, 8, 10]
    #displays the total of the elements in the list
    print ('the total is: ', get_total(numbers))
# fuction get_total accepts the list as an
# argument and returns the total values in the list

def get_total(value_list):
    # creats variable for the accumulator
    total = 0

    # calculates the total of the list of.
    for num in value_list:
        total += num

    #returns the total
    return total

#calls main function
main()
