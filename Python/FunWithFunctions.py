#Odd/Even
def odd_even():
    for i in range(1, 2001):
        if i%2 == 0:
            print "The number is", i, "This is an even number"
        else:
            print "The number is", i, "This is an odd number"
odd_even()

#Multiply
def multiply(arr, num):
    for x in range(0, len(arr)):
        arr[x] *= num
    return arr

b = multiply([1,2,3], 5)
print b


