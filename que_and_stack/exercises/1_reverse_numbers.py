from collections import deque
data = deque(input().split())
data.reverse()
print(' '.join(data))

# print(*input().split()[::-1], sep=" ")