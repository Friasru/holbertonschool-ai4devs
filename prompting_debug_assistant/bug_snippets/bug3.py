def add_item (item, basket=[]):
    """Add an item to a basket and return it."""
    basket.append(item)
    return basket

print(add_item("apple"))
print(add_item("banana"))
