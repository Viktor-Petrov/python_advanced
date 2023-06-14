from collections import deque

data = deque(input())
open_data = deque()

while data:
    left_data = data.popleft()

    if left_data in "([{":
        open_data.append(left_data)
    elif not open_data:
        print("NO")
        break
    else:
        if f"{open_data.pop() + left_data}" not in "{}[]()":
            print("NO")
            break

else:
    print("YES")

