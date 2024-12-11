print("welcome to personal pizza delivery")

size = input("what size pizza do you want? S,M or L: ")
pepperoni = input("Do you want pepperoni eith pizza? y or n: ")
ext_cheese = input("do you want extra cheese? y or n: ")

Bill = 0

if size == S:
    Bill = 15
    if pepperoni == y:
        Bill += 2
        if ext_cheese == y:
            Bill += 1
            print("your total bill is: "+ Bill)


