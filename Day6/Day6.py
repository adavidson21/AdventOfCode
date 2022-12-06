data = open("Day6/Input.txt").read()  # parse by char

# start of packet marker = sequence of 4 unique characters
for i in range(0, len(data)-4):
    window = set()
    for j in range(i, i+4):
        window.add(data[j])
    if(len(window) == 4):
        print("Part 1: ", i+4)
        break

# start of packet marker = sequence of 14 unique characters
for i in range(0, len(data)-14):
    window = set()
    for j in range(i, i+14):
        window.add(data[j])
    if(len(window) == 14):
        print("Part 2: ", i+14)
        break
