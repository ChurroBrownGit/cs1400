side1 = int(input("What is the 1st side length? "))
side2 = int(input("What is the 2nd side length? "))
side3 = int(input("What is the 3rd side length? "))
total1 = side1 + side2
if total1 > side3:
    print("This is a valid triangle.")
else:
    print("This is not a valid trangle.")