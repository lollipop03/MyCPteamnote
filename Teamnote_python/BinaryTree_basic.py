class Node():
    def __init__(self, item, left, right):
        self.item = item
        self.left = left
        self.right = right

def preorder(tree, node):
    print(node.item, end = '')
    if node.left != '.':
        preorder(tree, tree[node.left])
    if node.right != '.':
        preorder(tree, tree[node.right])
        
def inorder(tree, node):
    if node.left != '.':
        inorder(tree, tree[node.left])
    print(node.item, end = '')
    if node.right != '.':
        inorder(tree, tree[node.right])
        
def postorder(tree, node):
    if node.left != '.':
        postorder(tree, tree[node.left])
    if node.right != '.':
        postorder(tree, tree[node.right])
    print(node.item, end = '')

N = int(input())
tree = {}
for _ in range(N):
    cur, left, right = input().strip().split()
    tree[cur] = Node(cur, left, right)
preorder(tree, tree['A'])
print()
inorder(tree, tree['A'])
print()
postorder(tree, tree['A'])
print()