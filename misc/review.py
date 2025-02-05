#Goal 1 % 2
def words_of_length(words, length):
    new_words = []
    for i in range(len(words)):
        if len(words[i]) == length:
            new_words.append(words[i])
    return new_words

def get_words(count):
    words = []
    for i in range(count):
        word = input("Enter a word: ")
        words.append(word)
    return words

def s_words(words):
    count2 = 0
    for word in words:
        if word[0].lower() == "s":
            count2 += 1
    return count2

def main():
    count = int(input("How many words do you want? "))
    words = get_words(count)
    count2 = s_words(words)
    three_letters = words_of_length(words, 3)
    four_letters = words_of_length(words, 4)
    five_letters = words_of_length(words, 5)
    six_letters = words_of_length(words, 6)

    print("Out of", len(words), "words,", end=" ")
    print((len(three_letters)/len(words))*100, "% have 3 letters")
    print("Out of", len(words), "words,", end=" ")
    print((len(four_letters)/len(words))*100, "% have 4 letters")
    print("Out of", len(words), "words,", end=" ")
    print((len(five_letters)/len(words))*100, "% have 5 letters")
    print("Out of", len(words), "words,", end=" ")
    print((len(six_letters)/len(words))*100, "% have 6 letters")
    print("Out of", len(words), "words,", count2 , "start(s) with s." )

main()