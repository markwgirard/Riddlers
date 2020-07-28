
n = 26
shirePop = [10*(i+1) + 1 for i in range(n)]
shireEVs = [i + 2 for i in range(1,n+1)]

totalPop = sum(shirePop)
totalEVs = sum(shireEVs)
EVsNeeded = totalEVs//2 + 1

print('Total population:       {}'.format(totalPop))
print('Total electoral votes:  {}'.format(totalEVs))
print('Electoral votes to win: {}'.format(EVsNeeded))
print('--------------')
print('Searching for best combination...')

bestWins = list(range(1,n+1))
bestVotes = totalPop
bestEVs = totalEVs
for mask in range (2**n):
    votes, evotes = 0, 0
    shire = 1
    wins = []
    while mask:
        if mask%2:
            votes  += shirePop[shire-1]//2 + 1
            evotes += shireEVs[shire-1]
            wins.append(shire)
        mask >>= 1
        shire += 1
        if votes >= bestVotes:
            break
        if evotes >= EVsNeeded:
            if votes < bestVotes:
                bestVotes = votes
                bestWins = wins
                bestEVs = evotes

print('Fewest number of votes needed: {}'.format(bestVotes))
print('Proportion of votes won:       {0:.2f}'.format(bestVotes/totalPop*100))
print('Best combination of shires won:',bestWins)
print('Which nets this many EVs:      {}'.format(bestEVs))
