#Goal 1
toys = ["doll", "truck", "ball", "yo-yo", "action figure", "stuffed animal"]
foods = ["eggs", "bacon", "toast", "sausage", "pancakes", "waffles", "orange juice"]
nums = [5, 6, 7, 8, 10, 12, 14, 16, 20, 24, 28, 32, 40, 48, 56, 64, 80, 96, 112, 128]
prices = ["1.99", "2.99", "3.99", "4.99", "5.99", "19.99", "199.99"]

for toy in toys:
    print(toy)

for food in foods:
    print(food)

for num in nums:
    print(num)

for price in prices:
    print(price)

#Goal 2
vowels = "AEIOUYaeiouy"
consonants = "BCDFGHJKLMNPQRSTVWXZbcdfghjklmnpqrstvwxz"
symbols = "~!@#$%^&*()_+-=[]{}|;:',.<>/?"
numbers = "0123456789"

for i in vowels:
    print(i)

for i in consonants:
    print(i)

for i in symbols:
    print(i)

for i in numbers:
    print(i)

#Challenge 1
def count_5s(nums):
    count5 = 0
    for num in nums:
        if num == 5:
            count5 += 1
    return count5

count5 = count_5s([1, 2, 3, 4, 5, 6, 7, 5, 4, 2, 3, 5, 9])
print(count5)

#Challenge 2
def find_w(characters):
    for i in range(len(characters)):
        if characters[i] == "w":
            return i
    return -1
            
w = find_w("The quick brown fox jumps over the lazy dog.")
print(w)