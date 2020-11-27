from copy import deepcopy
import sys
class Node:
    def __init__(self, next=None, prev=None, data=None):
        self.next = next
        self.prev = prev
        self.data = data

def printSolution(puzzle):
    print("Path:")
    printPuzzle(puzzle);
    while(puzzle.prev is not None):
        puzzle = puzzle.prev
        printPuzzle(puzzle);


def switchTiles(direction, newData, parent):
    # switch direction of 0
    # direction 0 == left; 1 == right
    #           2 == up; 3 == down
    newPuzzle = Node(prev=parent, data = deepcopy(newData));

    if(direction == 0):
        for row in newPuzzle.data:
            if(0 in row):
                zero = row.index(0);
                row[zero], row[zero-1] = row[zero-1], row[zero]
                break;

    if(direction == 1):
        for row in newPuzzle.data:
            if(0 in row):
                zero = row.index(0);
                row[zero], row[zero+1] = row[zero+1], row[zero]
                break;

    if(direction == 2):
        for row in newPuzzle.data:
            if(0 in row):
                zero = row.index(0);
                col = newPuzzle.data.index(row);
                newPuzzle.data[col][zero], newPuzzle.data[col-1][zero] =newPuzzle.data[col-1][zero], newPuzzle.data[col][zero]
                break;

    if(direction == 3):
        for row in newPuzzle.data:
            if(0 in row):
                zero = row.index(0);
                col = newPuzzle.data.index(row);
                newPuzzle.data[col][zero], newPuzzle.data[col+1][zero] =newPuzzle.data[col+1][zero], newPuzzle.data[col][zero]
                break;

    return newPuzzle;



def expand(puzzle):
    newNodes = [];

    row = None
    col = None

    for list in puzzle.data:
        if(0 in list):
            col = puzzle.data.index(list);
            row = list.index(0)

    if(row == 0):
        newNodes.append(switchTiles(1, puzzle.data, puzzle));
    if(row == 1):
        newNodes.append(switchTiles(1, puzzle.data, puzzle));
        newNodes.append(switchTiles(0, puzzle.data, puzzle));
    if(row == 2):
        newNodes.append(switchTiles(0, puzzle.data, puzzle));


    if(col == 0):
        newNodes.append(switchTiles(3, puzzle.data, puzzle));
    if(col == 1):
        newNodes.append(switchTiles(2, puzzle.data, puzzle));
        newNodes.append(switchTiles(3, puzzle.data, puzzle));
    if(col == 2):
        newNodes.append(switchTiles(2, puzzle.data, puzzle));

    return newNodes;


def printList(list):
    for e in list:
        printPuzzle(e);

def printPuzzle(puzzle):
    for i in puzzle.data:
        print(i)
    print()

def depth_search(puzzle, goal, knownNodes):

    newNodes = [];

    if(puzzle.data == goal.data):
        print("Goal reached");
        printSolution(puzzle);
        return 0;

    newNodes.extend(expand(puzzle));
    knownNodes.append(puzzle);

    for known in knownNodes:
        for new in newNodes:
            if(new.data == known.data):
                newNodes.remove(new);

    while(True):
        if newNodes == []:
            break;
        else:
            erg = depth_search(deepcopy(newNodes[0]), goal, knownNodes);
            if(erg == 0):
                return 0;
            newNodes.pop(0);

    return -1;

#---Main---
#TODO: Manual Input
sys.setrecursionlimit(10**6)
puzzle = Node(next=None, prev=None, data=[[1,2,3],[4,5,0],[7,8,6]])
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

emptyList = []
print("----------Starting-------------")
depth_search(puzzle, goal, emptyList)
print("Finished")
