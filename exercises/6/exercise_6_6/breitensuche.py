

def printPuzzle(puzzle):

    for i in puzzle:
        if(i%3 == 0):
            print(i)
        else:
            print(i, end='')
    print()

#---Main---

puzzle = [1,2,3,4,5,6,7,8,0]
#print(" Input vals from 0-8 for start state ")
#for i in range(0,9):
#    x = int(input("enter vals :"))
#    puzzle.append(x)

 # User input of goal state
goal = [1,2,3,4,5,6,7,8,0]
#print(" Input vals from 0-8 for goal state ")
#for i in range(0,9):
#    x = int(input("Enter vals :"))
#    goal.append(x)

print("Start puzzle:")
printPuzzle(puzzle)

print("End puzzle:")
printPuzzle(goal)
