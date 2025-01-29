#Goal 1
x = 0
while x < 10:
    x += 1
    print(x)

#Goal 2
y = 200
while y > 1:
    y /= 2
    print(y)

#Challenge 1
def fibonacci(x):
    y = 0
    z = 1
    while y <= x:
        print(y)
        y += z
        print(z)
        z += y

fibonacci(200)