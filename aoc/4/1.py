totalscore = 0
with open('input.txt') as openfileobject:
    for line in openfileobject:
        winners = line.split("|")[0].split()[2:]
        tickets = line.split("|")[1].split()
        score = 0
        for t in tickets:
            if t in winners and score is 0:
                score = 1
            elif t in winners:
                score *= 2
        totalscore += score
print(totalscore)
