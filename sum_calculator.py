#This program calculates the sum of a series
#of numbers entered by the user

max = 5 #the maximum number

# initialixes accumulator variable
total = 0.0

print ('this program calculates the sum of ')
print (max, 'numbers you will enter.')

#get numbers and accumulates them

for counter in range(max):
    number = int(input('enter a number: '))
    total = total + number

# Displays the toal

print('the total is ', total)
