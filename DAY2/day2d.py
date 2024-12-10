
bill = float(input("how much is your Bill:"))
tip = int(input("how much tip do you want ot give: 5,10,12,15?? : "))
people = int(input("Between how many people are u splitting the bill: "))

c = tip/100*bill + bill

print("total bill will be: ", c)

perP = c/people

print(round (perP), 2)
