
LENGTH = 8
mystery = "XXXXXXXXXX    $XXX XXXXXX   XX XX X X  XX  XX XXX     *XXXXXXXXX"

line = raw_input()
current = mystery.find('*')
for c in line:
    if c == 'U':
        current -= LENGTH
    elif c == 'D':
        current += LENGTH
    elif c == 'L':
        current -= 1
    elif c == 'R':
        current += 1
    
    if mystery[current] == "X":
        print "Invalid Opration!"
        break
    if mystery[current] == "$":
        print "Success!"
        break
