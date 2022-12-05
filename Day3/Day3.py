# Import the data & parse by line break
data = open("Day3/Input.txt").read().split("\n")
sum1 = 0
sum2 = 0
groups = list(zip(*[iter(data)]*3))

priorities = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
    "A": 27,
    "B": 28,
    "C": 29,
    "D": 30,
    "E": 31,
    "F": 32,
    "G": 33,
    "H": 34,
    "I": 35,
    "J": 36,
    "K": 37,
    "L": 38,
    "M": 39,
    "N": 40,
    "O": 41,
    "P": 42,
    "Q": 43,
    "R": 44,
    "S": 45,
    "T": 46,
    "U": 47,
    "V": 48,
    "W": 49,
    "X": 50,
    "Y": 51,
    "Z": 52,
}

# Part 1
for d in data:
    p1, p2 = d[:len(d)//2], d[len(d)//2:]  # split string
    first, second = set(p1), set(p2)
    unique = list(first & second)
    sum1 += int(priorities[unique[0]])  # Get priority of first unique value

# Part 1
for group in groups:

    first, second, third = set(group[0]), set(group[1]), set(group[2])
    unique = list(first & second & third)
    sum2 += int(priorities[unique[0]])  # Get priority of first unique value

print("Part 1:",  sum1)
print("Part 2:",  sum2)
