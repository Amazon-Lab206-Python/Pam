def scores_grades():
    import random
    random_num = random.randint(60, 101)
    if random_num >59 and random_num < 70:
        print "Score:", random_num ,"; Your Grade is D"
    elif random_num >69 and  random_num< 80:
        print "Score:", random_num ,"; Your Grade is C"
    elif random_num >79 and  random_num< 90:
        print "Score:", random_num ,"; Your Grade is B"
    else:
        print "Score:", random_num ,"; Your Grade is A"

scores_grades()