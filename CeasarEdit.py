from collections import defaultdict
def editDistance(source, target):
    if source == target: return 0
    source = [ord(source[i]) for i in range(len(source))]
    target = [ord(target[i]) for i in range(len(target))]
    differences = defaultdict(int)
    for i in range(len(source)):
        differences[source[i]-target[i]] += 1
    minChangesNeeded = len(source)*2
    for i in range(len(differences)):
        _, mostCommon = max(zip(differences.values(), differences.keys()))
        newSource = []
        newTarget = []
        newSource = source
        newTarget = [(target[k] + mostCommon) for k in range(len(target))]
        for i in range(len(newTarget)):
            if newTarget[i] > 122: newTarget[i] -= 26
        newDifference = [i for i in newSource + newTarget if i not in newSource or i not in newTarget]
        if minChangesNeeded > len(newDifference):
            minChangesNeeded = len(newDifference)
        newSource = []
        newTarget = []
        newSource = source
        newTarget = [(target[k] + mostCommon) for k in range(len(target))]
        for i in range(len(newTarget)):
            if newSource[i] > 122: newSource[i] -= 26
        newDifference = [i for i in newSource + newTarget if i not in newSource or i not in newTarget]
        if minChangesNeeded > len(newDifference):
            minChangesNeeded = len(newDifference)
        del differences[mostCommon]
    if minChangesNeeded == 1: return 2
    return minChangesNeeded

    
source = 'abc'
target = 'efc'
print(editDistance(source, target))