def print_func(poss, nega):
    print(nega)
    print(poss)

    if poss > abs(nega):
        print("The positives are stronger than the negatives")
    else:
        print("The negatives are stronger than the positives")

numbers = [int(x) for x in input().split()]

positive_num = sum(n for n in numbers if n > 0)
negative_num = sum(n for n in numbers if n < 0)


print_func(positive_num, negative_num)