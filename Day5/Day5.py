#     [H]         [H]         [V]
#     [V]         [V] [J]     [F] [F]
#     [S] [L]     [M] [B]     [L] [J]
#     [C] [N] [B] [W] [D]     [D] [M]
# [G] [L] [M] [S] [S] [C]     [T] [V]
# [P] [B] [B] [P] [Q] [S] [L] [H] [B]
# [N] [J] [D] [V] [C] [Q] [Q] [M] [P]
# [R] [T] [T] [R] [G] [W] [F] [W] [L]
#  1   2   3   4   5   6   7   8   9
stack1 = ["R", "N", "P", "G"]
stack2 = ["T", "J", "B", "L", "C", "S", "V", "H"]
stack3 = ["T", "D", "B", "M", "N", "L"]
stack4 = ["R", "V", "P", "S", "B"]
stack5 = ["G", "C", "Q", "S", "W", "M", "V", "H"]
stack6 = ["W", "Q", "S", "C", "D", "B", "J"]
stack7 = ["F", "Q", "L"]
stack8 = ["W", "M", "H", "T", "D", "L", "F", "V"]
stack9 = ["L", "P", "B", "V", "M", "J", "F"]


def chooseStack(num):
    if(num == 1):
        return stack1
    elif(num == 2):
        return stack2
    elif(num == 3):
        return stack3
    elif(num == 4):
        return stack4
    elif(num == 5):
        return stack5
    elif(num == 6):
        return stack6
    elif(num == 7):
        return stack7
    elif(num == 8):
        return stack8
    else:
        return stack9


data = open("Day5/Input.txt").read().split("\n")

for d in data:
    vals = [int(s) for s in d.split() if s.isdigit()]  # Get digits
    fromStack = chooseStack(vals[1])  # choose from
    toStack = chooseStack(vals[2])  # choose to
    for i in range(0, vals[0]):
        toStack.append(fromStack.pop())  # move from one to another

print("Stack 1: ", stack1.pop())
print("Stack 2: ", stack2.pop())
print("Stack 3: ", stack3.pop())
print("Stack 4: ", stack4.pop())
print("Stack 5: ", stack5.pop())
print("Stack 6: ", stack6.pop())
print("Stack 7: ", stack7.pop())
print("Stack 8: ", stack8.pop())
print("Stack 9: ", stack9.pop())
