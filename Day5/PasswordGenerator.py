scores = [1,4,8]
#print(max(scores))

maxscore = 0
for score in scores:
    if score > maxscore:
        maxscore = score


print(maxscore)