#Goal 1
def stylish(socks, sandals):
    if socks == True and sandals == True:
        return True
    else:
        return False

socks = True
sandals = True
boolean = stylish(socks, sandals)
print(boolean)

#Goal 2
def i_scream(chocolate, vanilla):
    if chocolate == True or vanilla == True:
        return True
    else:
        return False

chocolate = True
vanilla = False
icecream = i_scream(chocolate, vanilla)
print(icecream)

#Goal 3
def opposite_day(opposite):
    if opposite == True:
        return False
    else:
        return True
    
opposite = True
backwards = opposite_day(opposite)
print(backwards)

#Challenge 1
def limited_sum(a,b):
    answer = a + b
    if int(answer) >= 20 and int(answer) <= 29:
        answer = 30
        return answer
    else:
        return answer

a = 7
b = 16
answer = limited_sum(a,b)
print(answer)

#Challenge 2
def super_sevens(c,d):
    if a == 7 or b == 7 or a+b ==7 or a-b == 7 or b-a == 7:
        return True
    else:
        return False

c = 19
d = 12
sevens = super_sevens(c,d)
print(sevens)

#Challenge 3
def close_to_ten(num):
    if num % 10 <= 3:
        return True
    else:
        return False

num = 97
closeten = close_to_ten(num)
print(closeten)