list = [["dog", "cat", "frog", "horse", "cat"], ["car", "plane", "jet", "boat", "motorcycle"], ["fortnite", "minecraft", "mario", "zelda", "tetris"]]

def showCrap(topic):
    print("SHOW CRAP: " + topic)

for i in list:
    for topic in i:
        showCrap(topic)

board = [["X", "O", "X"], ["O", "O", "X"], [" ", " ", "X"]]