
def kwargs_length(**dict):
    return len(dict.keys())


dictionary = {'name': 'Peter', 'age': 25}

print(kwargs_length(**dictionary))
