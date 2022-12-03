# Import the data & parse by line break
data = open("Day1Input.txt").read().split("\n\n")

sums = []
for line in data:
    values = line.split("\n")
    sum = 0
    for value in values:
        sum = sum + int(value)
    sums.append(sum)

sums.sort()

print('Highest: ', sums[-1])
print('Sum of Top 3: ', sums[-1] + sums[-2] + sums[-3])
