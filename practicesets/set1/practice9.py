totalcost = float(input("What was the total money amount? "))
if totalcost > 100.00:
    totalcost = totalcost * 0.90
    print("Your new total is " + totalcost + ".")
else:
    print("Your total is " + totalcost + ".")