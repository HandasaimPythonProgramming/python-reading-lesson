
print "Enter a number:"
number = int(raw_input())
for i in range(number, 1, -1):
    print " " * i + "A" * (2*number - 2 * i + 1) + " " * i
for i in range(1, number+1):
    print " " * i + "A" * (2*number - 2 * i + 1) + " " * i