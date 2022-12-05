# Import the data & parse by line break
data = open("Day2/Input.txt").read().split("\n")
totalScore1 = 0
totalScore2 = 0

# Win = 6 points
# Draw = 3 points
# Rock = 1 points
# Paper = 2 points
# Scissors = 3 points

outcomes1 = {
    # Draws
    "A X": 4,
    "B Y": 5,
    "C Z": 6,
    # Wins
    "C X": 7,
    "A Y": 8,
    "B Z": 9
}

# X = Lose
# Y = Draw
# Z = Win

outcomes2 = {
    "A X": 3,  # Rock + Lose => Scissors 3 + 0
    "B X": 1,  # Paper + Lose => Rock 1 + 0
    "C X": 2,  # Scissors + Lose => Paper 2 + 0
    "A Y": 4,  # Rock + Draw => Rock 1 + 3
    "B Y": 5,  # Paper + Draw => Paper 2 + 3
    "C Y": 6,  # Scissors + Draw => Scissors 3 + 3
    "A Z": 8,  # Rock + Win => Paper 2 + 6
    "B Z": 9,  # Paper + Win => Scissors 3 + 6
    "C Z": 7,  # Scissors + Win => Rock 1 + 6
}

# Part One
for d in data:
    if(d in outcomes1):
        totalScore1 += outcomes1[d]
    else:
        if('X' in d):
            totalScore1 += 1
        if('Y' in d):
            totalScore1 += 2
        if('Z' in d):
            totalScore1 += 3

# Part Two
for d in data:
    totalScore2 += outcomes2[d]

print("Part One: ", totalScore1)
print("Part Two: ", totalScore2)
