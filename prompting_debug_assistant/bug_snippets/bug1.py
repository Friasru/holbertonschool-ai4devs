def last_n_items(items, n):
    """Return the last n items of a list"""
    result = []
    for i in range(len(items) - n, len(items)):
        result.append(items[i])
    return result

print(last_n_items([1, 2, 3, 4, 5], 7))
