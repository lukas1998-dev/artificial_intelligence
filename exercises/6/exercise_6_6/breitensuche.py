
list = [];

class Node:
    def __init__(self, next=None, prev=None, data=None):
        self.next = next
        self.prev = prev
        self.data = data

def expand(puzzle):
    print("Expanding:");
    printPuzzle(puzzle);

    row = None
    col = None

    for list in puzzle.data:
        if(0 in list):
            col = puzzle.data.index(list);
            row = list.index(0)

    print(row)
    print(col)

def printList(list):
    for e in list:
        printPuzzle(e);


def printPuzzle(puzzle):
    for i in puzzle.data:
            print(i)
    print()

def breadth_first(puzzle, goal):
    if(puzzle.data == goal.data):
        print("Goal reached")
        return;
    else:
        global list;
        list.append(puzzle);

        nextPuzzle = None;
        #while(True):

        for p in list:
            if(p.next is None):
                nextPuzzle = p;
                break;

        expand(nextPuzzle);
        #break;

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

breadth_first(puzzle, goal)
print("Finished")
