#this program uses a for loop to read
#all of the values in the sales.txt file

def main():
    #opens the sales.txt file for reading
    sales_file = open('sales.txt', 'r')

    #read all the lines in the file
    for line in sales_file:
        #converts the line to a float
        amount = float(line)
        #format and display the amount
        print(format(amount, '.2f'))
    #close the file
    sales_file.close()

#calls main function
main()
