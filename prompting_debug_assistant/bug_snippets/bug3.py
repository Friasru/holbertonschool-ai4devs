def add_item(item, basket=[]):
    """Add an item to a basket and return it."""
    basket.append(item)
    return basket


def main():
    """Run a few sample calls to add_item"""
    first_basket = add_item("apple")
    print(first_basket)

    second_basket = add_item("banana")
    print(second_basket)

    third_basket = add_item("carrot")
    print(third_basket)


if __name__ == "__main__":
    main()
