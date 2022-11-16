class Node():
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start):
    current = start
    print(current.data, end=' ')

    while current.link != None:
        current = current.link
        print(current.data, end = ' ')
    print()

def insertNode(findData, insertData):
    global memory, head, current, pre
    ## Case 1: 헤드 앞에 삽입 -> 다현, 화사
    if (findData == head.data):
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        memory.append(node)
        return

    ## Case 2: 중간 노드 앞에 삽입 -> 사나, 솔라
    current = head
    while (current.link != None):
        pre = current
        current = current.link
        if (current.data == findData):
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            memory.append(node)
            return
    
    ## Case 3: 없는 노드 앞에 삽입 (=마지막 노드로 추가) -> 재남, 문별
    node = Node()
    node.data = insertData
    current.link = node
    memory.append(node)
    return

def deleteNode(delData):
    global memory, head, current, pre
    # Case 1 : Head의 노드를 삭제 -> 다현
    if (delData == head.data):
        current = head
        head = head.link
        del(current)
        return

    # case 2 : 중간 노드를 삭제 => 쯔위
    current = head
    while current.link != None:
        pre = current
        current = current.link
        if (current.data == delData):
            pre.link = current.link
            del(current)
            return
    
    # case 3 : 없는 노드를 삭제 -> 재남
    return

def findNode(findData):
    global memory, head, current, pre
    current = head
    if current.data == findData:
        return current
    while current.link != None:
        current = current.link
        if current.data == findData:
            return current
    
    return Node()

memory = []
head, current, pre = None, None, None
dataAry = ['다현', '정연', '쯔위', '사나', '지효']

node = Node()
node.data = dataAry[0]
head = node
memory.append(node)

for data in dataAry[1:]:
    pre = node
    node = Node()
    node.data = data
    pre.link = node
    memory.append(node)

printNodes(head)

# insertNode('다현', '화사')
# printNodes(head)

# insertNode('사나', '솔라')
# printNodes(head)

# insertNode('재남', '문별')
# printNodes(head)

# deleteNode('다현')
# printNodes(head)

# deleteNode('쯔위')
# printNodes(head)

music = findNode('사나')
print(music.data, '음악이 나옵니다.')