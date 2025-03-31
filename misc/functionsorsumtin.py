def countStartsWith(words, letter):
    count = 0
    for word in words:
        if word[0] == letter:
            count += 1
    print(count)

countStartsWith(['bob', 'joe', 'sam'], 'b')

countStartsWith(['bob', 'joe', 'sam', 'sally'], 's')

names = ['bomb', 'joe', 'sam', 'sally', 'tommy', 'john', 'jacob', 'sean', 'shat', 'walmart employee', 'robet', 'tim allen']
letters = ['j','s','b','t','w','u','r']

for l in letters:
    countStartsWith(names, l)
