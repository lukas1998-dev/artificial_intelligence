
def printPuzzle(puzzle):

    for i in puzzle:
        if((puzzle.index(i)+1)%3 == 0):
            print(i)
        else:
            print(i, end='')
    print()

def calcNodes(puzzle):

    index = puzzle.index(0)

    if((index % 2) == 0):
        if(index == 4):
            return 4
        else:
            return 2
    else:
        return 3

def moveTile(puzzle, moves):
    

def breadth_first(puzzle, goal):
    if(puzzle == goal):
        print("Finished")
        return;
    else:
        possibleMoves = calcNodes(puzzle)
        moveTile(puzzle, possibleMoves)


#---Main---

puzzle = [1,2,3,6,0,6,7,9,8]
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

breadth_first(puzzle, goal)
