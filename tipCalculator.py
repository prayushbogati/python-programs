#Tip calculator

totalBill = float(input("What was the total bill? $"))
tipRate = float(input("Enter tip rate: 10, 12 or 15?"))
people = float(input("No. of people to split the bill: "))

newBill = tipRate/100*totalBill+totalBill
billPerPerson = round((newBill / people), 2)

print("Each should pay $" + str(billPerPerson))

