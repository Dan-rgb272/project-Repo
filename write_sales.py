#this program prompts the user for sales amounts
#and write those amounts to the sales.txt file


def main():
    #gets the number of days
    num_days = int(input('for how many days do' +
                    'you have sales? '))
    
    #opens new file sales.txt
    sales_file = open('sales.txt', 'w')


    #gets the amount of sales for each day and
    #writes them into the file
    for count in range(1, num_days + 1):
        sales = float(input(f'Enter the sales for day #' + \
                    str(count) + ': '))

    #write the sles amount to the file.
    sales_file.write(str(sales) + '\n')

    #close the file
    sales_file.close()
    print('data written to sales.txt.')
    
#calls main function
main()
