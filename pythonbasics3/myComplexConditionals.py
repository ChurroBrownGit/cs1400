#Goal 1
def small3(x,y,z):
    if x < y and y < z:
        return x
    elif x > y and y < z:
        return y
    else:
        return z
    
smallest = small3(3,4,5)
print(smallest)

#Goal 2
def leap_year(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False

print(leap_year(2024))

#Challenge 1
def big4reorder(a, b, c, d):
    return sorted(a,b,c,d) 
#I looked up how I might sort this and learned about sorted().

print(big4reorder(10, 5, 20, 15))