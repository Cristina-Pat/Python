from collections import deque
from http.cookies import Morsel

class Tree:
    def __init__(self):
        self.root = None
        self.left = None
        self.right = None

def isEmpty(tree: Tree) -> bool:
        return tree.root == tree.left == tree.right == None

def isLeaf(tree: Tree) -> bool:
    return not isEmpty(tree) and isEmpty(tree.left) and isEmpty(tree.right)

def join(root: object, left: Tree, right: Tree) -> Tree:
    tree = Tree()
    tree.root = root
    tree.left = left
    tree.right = right
    return tree

#return the item with the smallest key
def smallest(tree: Tree) -> object:
    while not isEmpty(tree.left):
        tree = tree.left
    return tree.root

#print the Morse tree in order
def inOrder(expression: Tree) -> None:
    if isEmpty(expression):
        return
    if isLeaf(expression):
        print(expression.root, end=' ')
        return
    print('', end=' ')
    inOrder(expression.left)
    print(' ', expression.root, ' ', end=' ')
    inOrder(expression.right)
    print('', end= ' ')

#print each level of the Morse tree (breadth-first search)
def levels(tree: Tree) -> None:
    thisLevel = deque()
    nextLevel = deque()
    thisLevel.append(tree)
    print(thisLevel)

    while len(thisLevel) > 0:
        tree = thisLevel.popleft()
        print(tree.root, ' ', end='')
        if not isEmpty(tree.left):
            nextLevel.append(tree.left)
        if not isEmpty(tree.right):
            nextLevel.append(tree.right)
        #start a new line whether it was the last tree on this level
        if len(thisLevel) == 0:
            print()
            thisLevel = nextLevel
            nextLevel = deque()

EMPTY = Tree()
H = join('H',EMPTY,EMPTY)
V = join('V',EMPTY,EMPTY)
F = join('F',EMPTY,EMPTY)
L = join('L',EMPTY,EMPTY)
P = join('P',EMPTY,EMPTY)
J = join('J',EMPTY,EMPTY)
B = join('B',EMPTY,EMPTY)
X = join('X',EMPTY,EMPTY)
C = join('C',EMPTY,EMPTY)
Y = join('Y',EMPTY,EMPTY)
Z = join('Z',EMPTY,EMPTY)
Q = join('Q',EMPTY,EMPTY)
S = join('S',H,V)
U = join('U',F,EMPTY)
R = join('R',L,EMPTY)
W = join('W',P,J)
D = join('D',B,X)
K = join('K',C,Y)
G = join('G',Z,Q)
O = join('O',EMPTY,EMPTY)
I = join('I',S,U)
A = join('A',R,W)
N = join('N',D,K)
M = join('M',G,O)
E = join('E',I,A)
T = join('T',N,M)
MORSE = join('START',E,T)


print(smallest(MORSE))
inOrder(MORSE)
levels(MORSE)