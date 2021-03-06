from turtle import left
from collections import deque


class TreeNode:
# a rooted binary tree
    def __init__(self):
        self.item = None
        self.left = None
        self.right = None


# return true if the the tree is empty
def isEmpty(tree: TreeNode) -> bool:
    return tree.item == tree.left == tree.right == None


# return true if the tree is a single leaf
def isLeaf(tree: TreeNode) -> bool:
    return not isEmpty(tree) and isEmpty(tree.left) and isEmpty(tree.right)


# return a tree with the given root and subtrees
def join(item: object, left: TreeNode, right: TreeNode) -> TreeNode:
    tree = TreeNode()
    tree.item = item
    tree.left = left
    tree.right = right
    return tree


# return the size of the tree (the numbers of the items/nodes)
def size(tree: TreeNode) -> int:
    if isEmpty(tree):
        return 0
    else:
        return size(tree.left) + size(tree.right) + 1


# return the height of the tree (the number of levels, largest depth plus 1 - for root)
def height(tree: TreeNode) -> int:
    if isEmpty(tree):
        return 0
    else:
        return max(height(tree.left), height(tree.right)) + 1


#return true if the item occurs on the tree
def has(tree: TreeNode, item: object) -> bool:
    if isEmpty(tree):
        return False
    if tree.item == item: #visit a node
        return True
    return has(tree.left, item) or has(tree.right, item)


#print the expression produced by the tree
def inOrder(expression: TreeNode) -> None:
    if isEmpty(expression):
        return
    if isLeaf(expression):
        print(expression.item, end=' ')
        return
    print('(', end=' ')
    inOrder(expression.left)
    print(' ', expression.item, ' ', end=' ')
    inOrder(expression.right)
    print(')', end= ' ')

#return the value of the expresssion tree
def assess(expresssion: TreeNode) -> int:
    if isLeaf(expresssion):
        return expresssion.item
    leftValue = assess(expresssion.left)
    rightValue = assess(expresssion.right)
    operator = expresssion.item
    if operator == '+':
        return leftValue + rightValue
    if operator == '-':
        return leftValue - rightValue
    if operator == '*':
        return leftValue * rightValue
    if operator == '/':
        return leftValue / rightValue
        

#print the tree from the level down, one level per line
def levels(tree: TreeNode) -> None:
    thisLevel = deque()
    nextLevel = deque()
    thisLevel.append(tree)
    print(thisLevel)

    while len(thisLevel) > 0:
        tree = thisLevel.popleft()
        print(tree.item, ' ', end='')
        if not isEmpty(tree.left):
            nextLevel.append(tree.left)
        if not isEmpty(tree.right):
            nextLevel.append(tree.right)
        #start a new line whether it wsa the last tree on this level
        if len(thisLevel) == 0:
            print()
            thisLevel = nextLevel
            nextLevel = deque()

# construct trees bottom-up, starting from the leaves
EMPTY = TreeNode()
THREE = join(3, EMPTY, EMPTY)
FOUR = join(4, EMPTY, EMPTY)
FIVE = join(5, EMPTY, EMPTY)
SIX = join(6, EMPTY, EMPTY)

# join two subtrees
SMA = join( '-', join('*', join('+', THREE, FOUR), FIVE), SIX) #((3+4)*5)-6


# isEmpty(SMA)
#print(isLeaf(FOUR))
# isEmpty(EMPTY)
#print(isLeaf(SMA))
#print(size(SMA))
#print(height(SMA))
#print(has(SMA, 5))
#print(has(SMA, 7))

#inOrder(SMA)
#print('= ', assess(SMA))

levels(SMA)