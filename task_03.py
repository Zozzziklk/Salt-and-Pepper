
def maxxx_odd(list):
    if list is None:
        return None
    for i in list:
        if isinstance(i, (int, float)) and i % 2 == 1:
            range = i

    print(range)


print(maxxx_odd([ 2, 7, 4, 5]))