# Import the data & parse by line break
# Parse data separated by blank lines
data = open("Day1/Input.txt").read().split("\n\n")

sums = []  # store all sums

for item in data:
    values = item.split("\n")  # Separate by individual value
    sum = 0
    for value in values:
        sum += int(value)
    sums.append(sum)

sums.sort()

print('Part 1 - Highest Count: ', sums[-1])
print('Part 2 - Sum of Top 3: ', sums[-1] + sums[-2] + sums[-3])
