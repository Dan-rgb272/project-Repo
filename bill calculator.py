#this program calculates the total bill for a purchase
#first the usser enters the prices for the five items purchased 
#then the program calculates
#the total price before tax, the tax owed and the total with tax included

#this is where the prices aare entered
price1 = float (input("how much does this cost?  $"))
price2 = float (input("how much does this cost?  $"))
price3 = float (input("how much does this cost?  $"))
price4 = float (input("how much does this cost?  $"))
price5 = float (input("how much does this cost?  $"))

#this adds the prices into a pre-tax bill

bill = price1 + price2 + price3 + price4 + price5
print ("the pre-tax bill is $ ", bill)

#the tax is calculated

tax = bill * 0.70
print ("the tax owed for this perchase is $ ", tax)

#the total with tax is calculated
total = bill + tax
print ("the total bill is $", total)

