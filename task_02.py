def coincidence(list=None, range=None):
    if list is None or range is None:
        return []
    result = []
    start_range = range.start
    stop_range = range.stop
    for i in list:

        if isinstance(i, (int, float)):
            if start_range <= i < stop_range
                result.append(i)
    return result

print(coincidence([1, 2, 3, 4, 5], range(3, 6)))
print(coincidence())
print(coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4)))

