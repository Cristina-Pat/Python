
from msilib import add_data
from msilib.schema import Binary
from trees import TreeNode


class BinaryTree:
# a rooted binary tree
    def __init__(self):
        self.item = None
        self.left = None
        self.right = None

KEY = 0
VALUE  = 1

# return true if the the tree is empty
def isEmpty(tree: BinaryTree) -> bool:
    return tree.item == tree.left == tree.right == None


# return true if the tree is a single leaf
def isLeaf(tree: BinaryTree) -> bool:
    return not isEmpty(tree) and isEmpty(tree.left) and isEmpty(tree.right)


# return a tree with the given root and subtrees
def join(item: object, left: BinaryTree, right: BinaryTree) -> BinaryTree:
    tree = BinaryTree()
    tree.item = item
    tree.left = left
    tree.right = right
    return tree


#check if a given key exists
def check(tree: BinaryTree, key: object) -> bool:
    if isEmpty(tree):
        return False
    elif tree.item[KEY] == key:
        return True
    elif tree.item[KEY] < key:
        return check(tree.right, key)
    else:
        return check(tree.left, key)

#return the value associated to the key
def lookup(tree: BinaryTree, key: object) -> object:
    if tree.item[KEY] == key:
        return tree.item[VALUE]
    elif tree.item[KEY] < key:
        return lookup(tree.right, key)
    else:
        return lookup(tree.left, key)

#return the item with the smallest key
def smallest(tree: BinaryTree) -> object:
    while not isEmpty(tree.left):
        tree = tree.left
    return tree.item

#assosciate the value to the key in the three
def addInTree(tree: BinaryTree, key: object, value: object) -> None:
    #if the tree is empty, create a leaf
    if isEmpty(tree):
        tree.item = (key, value)
        tree.left = BinaryTree()
        tree.right = BinaryTree()
    #if the key is in the root, replace the value
    elif tree.item[KEY] == key:
        tree.item = (key, value)
    #recurrent relationship: add/replace in the appropiate subtree
    elif tree.item[KEY] < key:
        addInTree(tree.right, key, value)
    else:
        addInTree(tree.left, key, value)

#remove the tree's node with the key
def remove(tree: BinaryTree, key: object) -> object:
    if isEmpty(tree):
        pass
    elif tree.item[KEY] < key:
        remove(tree.right, key)
    elif key < tree.item[KEY]:
        remove(tree.left, key)
    else:
        if isEmpty(tree.left):
            tree.item = tree.right.item
            tree.left = tree.right.left
            tree.right = tree.right.right
        elif isEmpty(tree.right):
            tree.item = tree.left.item
            tree.right = tree.left.right
            tree.left = tree.left.left
        else:
            tree.item = smallest(tree.right)
            remove(tree.right, tree.item[KEY])

#print the tree as a in file browser
def list(tree: BinaryTree, level: int) -> None:
    if isEmpty(tree):
        print(' ' * 7 * level, 'EMPTY')
    else:
        print(' ' * 7 * level, tree.item)
        list(tree.left, level + 1)
        list(tree.right, level + 1)


ONE = (1, 'I')
SEVEN = (7, 'VII')
EIGHT = (8, 'VIII')
NINE = (9, 'IX')
TEN = (10, 'X')

one = join(ONE, BinaryTree(), BinaryTree())
nine = join(NINE, BinaryTree(), BinaryTree())

BST = join(SEVEN, one, join(TEN, join(SEVEN, BinaryTree(), nine), BinaryTree()))

#adding a node with key 3 put it as the right child of 1
addInTree(BST, 3, 'III')
#list(BST, 0)

addInTree(BST, 5, 'V')
#list(BST, 0)

addInTree(BST, 4, 'IV')
#list(BST, 0)

remove(BST, 10)
list(BST, 0)

#print(check(BST, 2))
#print(check(BST, 9))
#print(smallest(BST))
#list(BST, 0) #0 is the initial indentation level

