word_list = ['hello','world','my','name','is','Anna']
char = 'o'
newlist = []

for i in range (0, len(word_list)):
    for x in range (0, len(word_list[i])):
        if word_list[i][x] == char:
            newlist.append(word_list[i])
        else: 
            continue
print newlist
