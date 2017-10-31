x = ["Hello", "World", 15, 40, 3]
count = 0
integer = 0 
string = 0
newstr = ''
for i in range (0, len(x)):
    if type(x[i]) == int:
        count += x[i]
        integer += 1
    elif type(x[i]) == str:
        newstr += x[i]
        string += 1
if integer > 0 and string > 0:
    print "This list is mixed"
    print "Sum:", count
    print "String:", newstr
elif integer > 0 and string == 0:
    print "This list contains integer(s)"
    print "Sum:", count
elif integer == 0 and string > 0:
    print "This list contains string(s)"
    print "String:", newstr

