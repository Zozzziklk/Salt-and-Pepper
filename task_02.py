def coincidence(list=None, range=None):
    if list is None or range is None:
        return []
    result = []
    for i in list:

        if isinstance(i, (int, float)) and i in range:
            result.append(i)
    return result

print(coincidence([1, 2, 3, 4, 5], range(3, 6)))
print(coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4)))