
lst = []

print("Please enter a number:")
line = input()
while line != "no":
    lst.append(line)
    print("Please enter a number:")
    line = input()

print("Ok... the result is:", sum(lst)/len(lst))