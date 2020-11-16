
class Node:
    def __init__(self, next=None, prev=None, data=None):
        self.next = next
        self.prev = prev
        self.data = data

def switchTiles(direction, puzzle):
    # switch direction of 0
    # direction 0 == left; 1 == right
    #           2 == up; 3 == down


    return;

def expand(puzzle):
    print("Expanding:");
    printPuzzle(puzzle);

    newNodes = [];

    row = None
    col = None

    for list in puzzle.data:
        if(0 in list):
            col = puzzle.data.index(list);
            row = list.index(0)


    if(row == 0):
        newNodes.append(switchTiles(1, puzzle));
    if(row == 1):
        newNodes.append(switchTiles(1, puzzle));
        newNodes.append(switchTiles(0, puzzle));
    if(row == 2):
        newNodes.append(switchTiles(0, puzzle));


    if(col == 0):
        newNodes.append(switchTiles(3, puzzle));
    if(col == 1):
        newNodes.append(switchTiles(3, puzzle));
        newNodes.append(switchTiles(2, puzzle));
    if(col == 2):
        newNodes.append(switchTiles(2, puzzle));

    return newNodes;


def printList(list):
    for e in list:
        printPuzzle(e);


def printPuzzle(puzzle):
    for i in puzzle.data:
        print(i)
    print()

def breadth_first(list, goal):

    newNodes = [];
    for p in list:
        if(p.data == goal.data):
            print("Goal reached");
            printPuzzle(p);
            return;

        newNodes.append(expand(p));

    if(len(newNodes) > 0 ):
        breadth_first(newNodes, goal);
    else:
        print("keine Lösung");
        return;

#---Main---
#TODO: Manual Input

puzzle = Node(next=None, prev=None, data=[[1,2,3],[4,5,6],[7,0,8]])
#print(" Input vals from 0-8 for start state ")
#for i in range(0,9):
#    x = int(input("enter vals :"))
#    puzzle.append(x)

 # User input of goal state
goal = Node(next=None, prev=None, data=[[1,2,3],[4,5,6],[7,8,0]])
#print(" Input vals from 0-8 for goal state ")
#for i in range(0,9):
#    x = int(input("Enter vals :"))
#    goal.append(x)

print("Start puzzle:")
printPuzzle(puzzle)

print("End puzzle:")
printPuzzle(goal)

list = []
list.append(puzzle)

breadth_first(list, goal)
print("Finished")
