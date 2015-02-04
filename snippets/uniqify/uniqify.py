def uniqify(seq):
    seen = {}
    unique = []
    for item in seq:
        if item not in seen:
            seen[item] = 1
            unique.append(item)
    return unique

items = ['B', 'B', 'E', 'Q', 'Q', 'Q']
print uniqify(items)  # prints ['B', 'E', 'Q']
