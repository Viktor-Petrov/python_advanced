clothes = [int(n) for n in input().split()]
rack_space = int(input())

current_rack_space = rack_space
counter = 1

while clothes:
    cloth = clothes.pop()
    if current_rack_space - cloth >= 0:
        current_rack_space -= cloth
    else:
        counter += 1
        current_rack_space = rack_space - cloth

print(counter)
