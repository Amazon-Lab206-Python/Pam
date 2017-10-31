def coin_toss(rep):
    import random
    print "Starting program"
    count_one = 0 
    count_two = 0
    for i in range(1,rep):
        flip = random.randint(1,2)
        if flip == 1:
            count_one += 1
            print "Attempt",i,"Tossing Coin...It's heads! Tally: Heads -", count_one, "Tails -", count_two
        elif flip == 2:
            count_two += 1
            print "Attempt",i,"Tossing Coin...It's tails! Tally: Heads -", count_one, "Tails -", count_two
coin_toss(5001)