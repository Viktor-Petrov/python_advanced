from collections import deque

quantity = int(input())
orders = deque([int(n) for n in input().split()])

print(max(orders))

for order in orders.copy():
    if quantity - order >= 0:
        orders.popleft()
        quantity -= order
    else:
        print(f"Orders left: {' '.join(str(a) for a in orders)}")
        break
else:
    print("Orders complete")