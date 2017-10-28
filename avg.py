
lst = []

print "Please enter a number or the word no:"
line = raw_input()
while line != "no":
    lst.append(int(line))
    print "Please enter a number:"
    line = raw_input()

print "Ok... the result is:", sum(lst)/len(lst)