#Goal 1

def multiple_22():
    int(input("List a number: "))
    if multiple_22 % 22 == 0:
        return True
    else:
        return False
    

#Goal 2

#Any number from 0-9 can be n in n % 10.

#Challenge 1
for i in range(333):
    print(i % 3)

#Challenge 2

def digits(numbers):
    ones = numbers % 10
    tens = numbers // 10 % 10
    hundreds = numbers // 10 // 10 % 10
    thousands = numbers // 10 // 10 // 10 % 10
    return [thousands, hundreds, tens, ones]
    
numbers = int(input("Input a number"))
r = digits(numbers)
print(r)
