def last_n_items(items, n):
    """Return the last n items of a list"""
    result = []
    for i in range(len(items) - n, len(items)):
        result.append(items[i])
    return result


def main():
    """Run a few sample calls to last_n_items"""
    numbers = [1, 2, 3, 4, 5]
    print(last_n_items(numbers, 2))
    print(last_n_items(numbers, 5))
    print(last_n_items(numbers, 7))


if __name__ == "__main__":
    main()
