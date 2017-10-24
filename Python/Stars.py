#Part 1
def draw_stars(arr):
    for i in arr:
        print "*" * i

draw_stars()

#Part 2
def draw_stars(arr):
    for i in arr:
        if type(i) == int:
            print "*" * i
        elif type(i) == str:
            length = len(i)
            letter = i[0].lower()
            print letter * length

draw_stars([4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"])