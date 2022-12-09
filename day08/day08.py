trees = [[int(i) for i in line] for line in open('input.txt', 'r').read().strip().split("\n")]
num_visible_trees = 0

# part a
for row in range(len(trees)):
    for col in range(len(trees[row])):
        tree = trees[row][col]
        leftTrees = [trees[row][iter] for iter in range(0, col)]
        rightTrees = [trees[row][iter] for iter in range(col + 1, len(trees[row]))]
        upTrees = [trees[iter][col] for iter in range(0, row)]
        downTrees = [trees[iter][col] for iter in range(row + 1, len(trees))]
        if all(tree > i for i in leftTrees) or all(tree > i for i in rightTrees) or all(tree > i for i in upTrees) or all(tree > i for i in downTrees):
            num_visible_trees += 1
print(num_visible_trees)

# part b
best_scenic_score = 0
for row in range(len(trees)):
    for col in range(len(trees[row])):
        tree = trees[row][col]
        leftTrees = [trees[row][iter] for iter in range(0, col)]
        rightTrees = [trees[row][iter] for iter in range(col + 1, len(trees[row]))]
        upTrees = [trees[iter][col] for iter in range(0, row)]
        downTrees = [trees[iter][col] for iter in range(row + 1, len(trees))]
        scoreFromLeft, scoreFromRight, scoreFromUp, scoreFromDown = 0, 0, 0, 0
        for t in reversed(leftTrees):
            scoreFromLeft += 1
            if(t >= tree):
                break
        for t in rightTrees:
            scoreFromRight += 1
            if(t >= tree):
                break
        for t in reversed(upTrees):
            scoreFromUp += 1
            if(t >= tree):
                break
        for t in downTrees:
            scoreFromDown += 1
            if(t >= tree):
                break
        scenic_score = scoreFromLeft * scoreFromRight * scoreFromUp * scoreFromDown
        if scenic_score > best_scenic_score:
            best_scenic_score = scenic_score
print(best_scenic_score) 