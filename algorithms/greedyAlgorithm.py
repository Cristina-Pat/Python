
pounds = [1, 2, 5, 10, 20, 50, 100] #1, 2 ... 50 is 1p, 2p ... 50p and 100 means £1.


def giveChange(change, coins):
    # create a list in size of length coins filled with 0
    toGive = [0] * len(coins)
    highestCoins = enumerate(reversed(coins)) # allow go backwards through coins list

    #loop through the list, but keep the position in another variable, i
    for i, coin in highestCoins: #the loop starts with coin = 100 and i = 6
        while coin <= change:
            change -= coin
            toGive[i] += 1 #keep track of the counter
    return(toGive)


print(giveChange(60, pounds))
print(giveChange(120, pounds))


