#this program shows a grade for a test

# if 90+ the grade is A, 80+ the grade is B,
# if 70+ the grade is c, 60+ the grade is D

# input for test scores

test = int (input('Enter a test score '))
A = 90
B = 80
C = 70
D = 60
#calculating the average


if test >= A:
    print ("your grade is a(n) A")
else:
        if test >= B:
            print ("your grade is a(n) B")
        else:
            if test >= C:
                print ("your grade is a(n) C")
            else:
                    if test >= D:
                        print ("your grade is a(n) D")
                    else:
                        print ("your grade is a(n) F")

