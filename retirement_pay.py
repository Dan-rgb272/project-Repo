#the following is used as a global contsraint
#the contribution rate
CONTRIBUTION_RATE = 0.05

def main():
    gross = float(input('enter the gross pay: '))
    bonus = float(input('enter the amount of bonus pay: '))
    show_pay_contrib(gross)
    show_bonus_contrib(bonus)

#the show_pay_contrib function accepts the gross pay
#as an argument and displays the retirement
#contribution for that amount of pay
def show_pay_contrib(gross):
    contrib = gross * CONTRIBUTION_RATE
    print('Contribution for gross pay: $', \
          format(contrib, ',.2f'), \
          sep='')

#the show_pay_contrib function accepts the bonus pay
#as an argument and displays the retirement
#contribution for that amount of pay

def show_bonus_contrib(bonus):
    contrib = bonus * CONTRIBUTION_RATE
    print('Contribution for gross pay: $', \
          format(contrib, ',.2f'), \
          sep='')

#calls main function
main()
