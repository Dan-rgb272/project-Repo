#This program gets an item's original price
#it then calculates the sales price with a 20% discount
#Gets the item's original price
Origin_price = float (input("Enter the original price:$ "))
#Calculates the discount
Dis = Origin_price * 0.2
print ("the discount is by $", Dis)
#Calculates the Sale's price
Sale = Origin_price - Dis
#Displays sale's price
print ("The sale price of the item is $", Sale)
