
def absolute(x):
    if x < 0:
        return -x
    return x

print "Please enter a number:"
number = int(raw_input())
print absolute(number)