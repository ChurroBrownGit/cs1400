#Goal 1
try:
    myfile = open("myfile.txt", 'r')
except:
    print("Can't read file")
    
#Goal 2
try:
    answer = 1/0
    print(answer)
except:
    print("Can't divide by 0")

#Challenge 1
def file_exists(filename):
    try:
        with open(filename, 'r'):
            return True
    except IOError:
        return False

exists = file_exists("filesname.txt")
print(exists)