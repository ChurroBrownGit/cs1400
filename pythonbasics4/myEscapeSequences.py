#Goal 1
print("Test\n\n\n\n\ning")

#Goal 2
print(len('\n'))
#This simply prints "1"

#Goal 3
print("\t\"Folks are usually about as \n\nhappy as they make their \n\nminds up to be.\" - Abraham Lincoln")

#Challenge 1
def clean_string(string):
    cleaned = ''
    for i in string:
        if i != '\n':
            cleaned += i
    return cleaned

test_str = "This\n\n\nis\na\n\n\n\n\nlot\nof\n\nnewlines\n"
cleaned = clean_string(test_str)
print(cleaned)

#Challenge 2
#print("\\\")
#This gives a SyntaxError because it still thinks the brackets are open if you escape.