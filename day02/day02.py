file = open('input.txt','r')
raw_data = file.read().split("\n")
opp_scoring  = {'A' : 1, 'B' : 2, 'C' : 3}
your_scoring = {'X' : 1, 'Y' : 2, 'Z' : 3}
score_total = 0

# part a
for game in raw_data:
    turns = game.split(" ")
    opp_score = opp_scoring[turns[0]]
    your_score = your_scoring[turns[1]]
    result_score = 6 if (opp_score % 3) + 1 == your_score else 3 if opp_score == your_score else 0
    score_total += your_score + result_score
print(score_total)

# part b
score_total = 0
for game in raw_data:
    turns = game.split(" ")
    opp_score = opp_scoring[turns[0]]
    objective = your_scoring[turns[1]]
    score_to_add = 0
    if objective == 1:
        score_to_add = opp_score - 1 if opp_score - 1 >= 1 else 3
    elif objective == 2:
        score_to_add = 3 + opp_score
    else:
        score_to_add = 6 + (opp_score % 3) + 1
    score_total += score_to_add
print(score_total)