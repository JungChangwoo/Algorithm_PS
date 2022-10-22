class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

class BinaryTree():
  def __init__(self):
    self.root = None

  def height(self, root):
    if root == None:
      return 0
    return max(self.height(root.left), self.height(root.right)) + 1

  def preorder(self, now):
    if now != None:
      print(now.item, end=' ')
      if now.left:
        self.preorder(now.left)
      if now.right:
        self.preorder(now.right)
        
  def postorder(self, now):
    if now != None:
      if now.left:
        self.postorder(now.left)
      if now.right:
        self.postorder(now.right)
      print(now.item, end=' ')
      
  def inorder(self, now):
    if now != None:
      if now.left:
        self.inorder(now.left)
      print(now.item, end=' ')
      if now.right:
        self.inorder(now.right)

  def levelorder(self, now):
    q = []
    q.append(now)
    while q:
      t = q.pop(0)
      print(t.item, end=' ')
      if t.left:
        q.append(t.left)
      if t.right:
        q.append(t.right)

tree = BinaryTree()
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)
n5 = Node(50)
n6 = Node(60)
n7 = Node(70)
n8 = Node(80)

tree.root = n1
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7
n4.left = n8

print('트리 높이 : ', tree.height(tree.root))

# 전위 순회: 10 20 40 80 50 30 60 70
print('전위 순회: ', end='')
tree.preorder(tree.root)
print()

# 후위 순회: 80 40 50 20 60 70 30 10 
print('후위 순회 : ', end='')
tree.postorder(tree.root)
print()

# 중위 순회: 80 40 20 50 10 60 30 70
print('중위 순회 : ', end='')
tree.inorder(tree.root)
print()

# 레벨 순회: 10 20 30 40 50 60 70 80
print('레벨 순회 : ', end='')
tree.levelorder(tree.root)
print()