#Goal 1
def smallest_number(numbers):
    smallest = numbers[0]
    for i in range(len(numbers)):
        if numbers[i] < smallest:
            smallest = numbers[i]
    return smallest

small = smallest_number([12, 54, 78, 77, 98, 21, 14, 9, 5])
print(small)

#Challenge 1
def averages(numbers):
    frequency = {}
    max_freq = 0
    mode = None
    count = 0
    total = 0
    for number in numbers:
        total += number
        count += 1
        average = total/count
    for number in numbers:
        if number in frequency:
            frequency[number] += 1
        else:
            frequency[number] = 1
        if frequency[number] > max_freq:
            max_freq = frequency[number]
            mode = frequency
    return average, mode

average, mode = averages([12, 54, 78, 77, 77, 21, 14, 9, 5])
print(average)
print(mode)

#Challenge 2
def median(numbers):
    count = 0
    med = 0
    for number in numbers:
        count += 1
    med = med + int(count / 2)
    medians = numbers[med]
    return medians

medians = median([12, 54, 78, 77, 98, 21, 14, 9, 5])
print(medians)