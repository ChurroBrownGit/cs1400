#Goal 1
test = open("unrealfile.txt", "r")
#This gives the error of "FileNotFoundError: [Errno 2] No such file or directory: 'unrealfile.txt'"

#Goal 2
with open("readme.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print(line.strip())

#Challenge 1
def every_other(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
    for i in range(0, len(lines), 2):
        print(lines[i].strip())

every_other("readme.txt")

#Challenge 2
def no_z(filename):
    with open(filename, "r") as file:
        for line in file:
            clean_line = ''
            for char in line:
                if char != 'z' and char != 'Z':
                    clean_line += char
            print(clean_line.strip())

no_z("readme.txt")
