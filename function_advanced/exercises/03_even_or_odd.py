def even_odd(*args):
    command = args[-1]
    result = []
    if command == "even":
        for n in args[:-1]:
            if n % 2 == 0:
                result.append(n)
    elif command == "odd":
        for n in args[:-1]:
            if n % 2 != 0:
                result.append(n)
    return result

print(even_odd(1, 2, 3, 4, 5, 6, "even"))



