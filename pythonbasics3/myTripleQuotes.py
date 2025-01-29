#Goal 1
def star():
    print('''
          *
         ***
     ***********
       *******
       *** ***
       *     *
    ''')

star()

#Goal 2/Challenge 1

def star():

    '''
    Parameters: None
    Return: None, prints a star
    Example: star() -> 
          *
         ***
     ***********
       *******
       *** ***
       *     *
    '''   
    print('''
          *
         ***
     ***********
       *******
       *** ***
       *     *
    ''')

star()

def smallest_number(numbers):
    '''
    Parameters: a list of numbers 
    Return: smalles number in said list
    Example: smallest_number([12, 54, 78, 77, 98, 21, 14, 9, 5]) -> 5
    '''
    smallest = numbers[0]
    for i in range(len(numbers)):
        if numbers[i] < smallest:
            smallest = numbers[i]
    return smallest

small = smallest_number([12, 54, 78, 77, 98, 21, 14, 9, 5])
print(small)

def fibonacci(x):
    '''
    Parameters: number that will stop the code once y reaches it.
    Return: The fibonacci sequence up to the inputted number.
    Example: fibonacci(200) ->
    0
    1
    1
    2
    3
    5
    8
    13
    21
    34
    55
    89
    144
    233
    '''
    y = 0
    z = 1
    while y <= x:
        print(y)
        y += z
        print(z)
        z += y

fibonacci(200)