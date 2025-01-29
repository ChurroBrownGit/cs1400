#Goal 1
#This causes a NameError.
#The variable "name" only exists in alien_encounter() as a local variable, which means if we try to call it in main(), it doesn't see "name".

#Goal 2
scope = 0

def tell_a_scope(scope):
    scope = 1
    return scope

tell_a_scope(scope)
print(scope)

#This will keep scope the same at the value of 0. This only changes if the print(scope) is put within the function.

#Challenge 1
def function1(x):
    return function2(x + 1)

def function2(x):
    return function3(x + 1)

def function3(x):
    return function4(x + 1)

def function4(x):
    return function5(x + 1)

def function5(x):
    return function6(x + 1)

def function6(x):
    return x

def main():
    print(function1(2))

main()