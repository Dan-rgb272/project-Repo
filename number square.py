#this program uses a loop to display
#a table of numbers and squares

# gets ending limit
print('this program displays a list of numbers')
print('(strting at 1 ) and their squares')
end = int(input("How high should it go?_"))

#print the table heading
print()
print('Number\tSquare')
print('--------------')

for number in range(1, end  + 1):
    square = number**2
    print(number, '\t', square)
