#this program has two functions which
# have local variables with the same name

def main():
    texas()
    #calls function referring to texas
    cali()
    #calls function referring to california

#texas function has a variable named birds
def texas():
    birds = 5000
    print('Texas has', birds, 'birds')

#cali fuction uses the same variable: birds
#but with a different amount

def cali():
    birds = 8000
    print('California has', birds, 'birds')
    
#calls main function
main()
