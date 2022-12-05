data = open("Day4/Input.txt").read().split("\n")
count = 0

for d in data:
    set = d.split(',')
    r1, r2 = set[0].split('-'), set[1].split('-')

    # Create ranges (add 1 for offset for python ranges)
    range1, range2 = range(int(r1[0]), int(
        r1[1])+1), range(int(r2[0]), int(r2[1])+1)

    # Check min and max of each range with other range.
    if(int(r1[0]) in range2 and int(r1[1]) in range2):
        count += 1
    elif(int(r2[0]) in range1 and int(r2[1]) in range1):
        count += 1

print("Part 1: ", count)
