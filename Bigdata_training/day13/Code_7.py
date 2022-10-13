SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = -1

rear += 1
queue[rear] = '화사'
rear += 1
queue[rear] = '솔라'
print('출구 <- ', queue, ' <- 입구' )

front += 1
data = queue[front]
queue[front] = None
print('식사손님: ', data)

front += 1
data = queue[front]
queue[front] = None
print('식사손님: ', data)

print(front, rear)