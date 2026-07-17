#this program determines whether a bank customer
#qualifies for a loan

min_sal = 30000 #minimum salary to qualify
min_year = 2    #Minimum number of years to qualify

#get anuual salary
salary = float(input('enter your salary' ))
#get the number of years
years = int(input('Enter the number of years you had this job for '))

#determines whether the customer qualifies

if salary >= min_sal or years >= min_year:
    print ("You qualify for the loan")
else:
    print ("you do not qualify for the loan")


