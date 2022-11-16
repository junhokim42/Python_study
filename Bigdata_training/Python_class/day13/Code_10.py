class TreeNode():
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

memory = []
root = None
nameAry = ['Haruhi', 'Yuki', 'Kyon', 'Mikuru', 'Koizumi']

node = TreeNode()
node.data = nameAry[0]
root = node
memory.append(node)

for name in nameAry[1:]:
    node = TreeNode()
    node.data = name

    current = root
    while True:
        if name < current.data :
            if current.left == None:
                current.left = node
                break
            else:
                current = current.left
        else:
            if current.right == None:
                current.right = node
                break
            else:
                current = current.right

    memory. append(node)

print("이진 탐색 트리 완료")

findName= 'Kyona'

current = root
while True:
    if (findName == current.data):
        print(findName, '는 SOS단 멤버')
        break
    elif (findName < current.data):
        if (current.left == None):
            print('그런 인물은 없다')
        current = current.left
    else:
        if (current.right == None):
            print('그런 인물은 없다')
        current = current.right