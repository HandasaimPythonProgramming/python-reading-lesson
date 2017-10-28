
from random import randint


lines1 =["   ", "*  ", "*  ", "* *", "* *", "***"]
lines2 =[" * ", "   ", " * ", "   ", " * ", "   "]
lines3 =["   ", "  *", "  *", "* *", "* *", "***"]

def print_dice(num):
    print '|' + lines1[num-1] + '|'
    print '|' + lines2[num-1] + '|'
    print '|' + lines3[num-1] + '|'

line = raw_input()
while line == "throw":
    print_dice(randint(1, 6))
    line = raw_input()
