def isStackFull():
    global SIZE, stack, top
    if (top == SIZE - 1):
        return True
    else:
        return False

def push(data):
    global SIZE, stack, top
    if (isStackFull() == True):
        print('스택 꽉참')
        return
    top += 1
    stack[top] = data

def isStackEmpty() :
    global SIZE, stack, top
    if (top == -1):
        return True
    else:
        return False

def pop():
    global SIZE, stack, top
    if (isStackEmpty()):
        print('스택 텅빔')
        return
    data = stack[top]
    stack[top] = None
    top -= 1
    return data

def peek():
    global SIZE, stack, top
    if (isStackEmpty()):
        print('스택이 비었습니다.')
        return None
    return stack[top]

SIZE = 5
stack = [None for _ in range(SIZE)]
top = -1

push('커피')
push('녹차')
# push('꿀물')
# push('콜라')
# push('환타')
# push('사이다')
print('바닥: ', stack)

print(pop())
print(pop())
print(pop())