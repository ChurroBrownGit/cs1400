#Goal 1
def print_nums(n=0):
    if n > 10:
        return
    print(n)
    print_nums(n + 1)

print_nums()

#Goal 2
def print_backwards(s):
    if s == "":
        return
    print(s[-1])
    print_backwards(s[:-1]) 

print_backwards("hello")

#Goal 3
def infinite_recursion():
    infinite_recursion()
    return

infinite_recursion()
#This will give the error "RecursionError: maximum recursion depth exceeded".

#Challenge 1
def triangle(rows):
    if rows == 0:
        return 0
    return rows + triangle(rows - 1)

print(triangle(0))
print(triangle(1))
print(triangle(2))
print(triangle(3))