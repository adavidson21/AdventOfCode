data = open("Day6/Input.txt").read()  # parse by char

# start of packet marker = sequence of 4 unique characters
for i in range(0, len(data)-4):
    first, second, third, fourth = data[i], data[i+1], data[i+2], data[i+3]
    # Ugly brute force check if any match
    if(first != second and first != third and first != fourth and second != third and second != fourth and third != fourth):
        print("Part 1: ", i+4)
        break
