# count poker hands

# 1. open the poker data file for reading
pokerFile = open("poker-hand-testing.txt",'rU')

totalCount         = 0 # 2. create variable to hold the count
nothingCount       = 0
pairCount          = 0 # create and initialize variable to hold pair count
twoPairCount       = 0
threeOfaKindCount  = 0
straightCount      = 0
flushCount         = 0
fullHouseCount    = 0
fourOfaKindCount   = 0
straightFlushCount = 0
royalFlushCount    = 0

# 3. step through each line of the file
for line in pokerFile:
    totalCount = totalCount + 1 # at each line increment the counter

    handRank = line.split(',')[-1] # get last item
    handRank = int(handRank)

    if handRank == 0:
        nothingCount       += 1
    if handRank == 1:
        pairCount          += 1
    if handRank == 2:
        twoPairCount       += 1
    if handRank == 3:
        threeOfaKindCount  += 1
    if handRank == 4:
        straightCount      += 1
    if handRank == 5:
        flushCount         += 1
    if handRank == 6:
        fullHouseCount     += 1
    if handRank == 7:
        fourOfaKindCount   += 1
    if handRank == 8:
        straightFlushCount += 1
    if handRank == 9:
        royalFlushCount    += 1

print "Total hands in file: ",totalCount
print "Count of hands: ",nothingCount,pairCount,twoPairCount,\
      threeOfaKindCount,straightCount,flushCount,fullHouseCount,\
      fourOfaKindCount,straightFlushCount,royalFlushCount
totalCountFP = float(totalCount)
print "Probability:"
print " of nothing:         %5.3f %%" % (100* nothingCount/totalCountFP)
print " of one pair:        %5.3f %%" % (100* pairCount/totalCountFP)
print " of two pairs:       %5.3f %%" % (100* twoPairCount/totalCountFP)
print " of three of a kind: %5.3f %%" % (100* threeOfaKindCount/totalCountFP)
print " of a straight:      %5.3f %%" % (100* straightCount/totalCountFP)
print " of a flush:         %5.3f %%" % (100* flushCount/totalCountFP)
print " of a full house:    %5.3f %%" % (100* fullHouseCount/totalCountFP)
print " of four of a kind:  %5.3f %%" % (100* fourOfaKindCount/totalCountFP)
print " of a straight flush:%5.3f %%" % (100* straightFlushCount/totalCountFP)
print " of a royal flush:   %5.3f %%" % (100* royalFlushCount/totalCountFP)













