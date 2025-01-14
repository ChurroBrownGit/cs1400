num1 = int(input("What is the first number?: "))
num2 = int(input("What is the second number?: "))
num3 = int(input("What is the third number?: "))

if num1 == num2 and num2 == num3:
    print("All three numbers are the same.")
elif num1 == num2 or num2 == num3 or num1 == num3:
    print("Two of these numbers are the same.")
elif num1 < num2 and num2 < num3:
    print("These numbers are in accending order.")
elif num1 > num2 and num2 > num3:
    print("These numbers are in deccending order.")
else:
    print("No specific pattern found.")