def even_odd_filter(**numbers):
    if "odd" in numbers.keys():
        numbers["odd"] = [n for n in numbers["odd"] if int(n) % 2 != 0]
    if "even" in numbers:
        numbers["even"] = [n for n in numbers["even"] if int(n) % 2 == 0]

    return dict(sorted(numbers.items(), key=lambda x: -len(x[1])))

# def even_odd_filter(**kwargs):
#     if "odd" in kwargs:
#         kwargs["odd"] = [n for n in kwargs["odd"] if int(n) % 2 == 1]
#
#     if "even" in kwargs:
#         kwargs["even"] = list(filter(lambda x: x % 2 == 0, kwargs["even"]))
#
#     return dict(sorted(kwargs.items(), key=lambda x: -len(x[1])))

print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
