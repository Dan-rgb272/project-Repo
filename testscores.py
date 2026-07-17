#this program displays the average of three test scores

# if the score is greater than 95%
# then it is considered a high score
high = 95

# input for test scores
test = int (input('Enter a test score '))
test2 = int (input('Enter a test score '))
test3 = int (input('Enter a test score '))

#calculating the average
avg = (test + test2 + test3) / 3

print ('the average score is ', avg)

if avg >= high:
    print ("congratulations!  That's a great average! ")

