#Find and Replace
words = "It's thanksgiving day. It's my birthday too!"
print words.find("day")
words = words.replace("day","month")
print words

#Min and Max
x = [2,54,-2,7,12,98]
print min(x)
print max(x)

#First and Last
x = ["hello",2,54,-2,7,12,98,"world"]
print [x[0], x[len(x) - 1]]


#NewList
x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
print x
first = x[:len(x)/2]
second = x[len(x)/2:]
second.insert(0, first)
print second
