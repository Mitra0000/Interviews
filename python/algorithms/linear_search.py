def linear_search(iterable, search_value):
    """
        Performs a linear search of an iterable looking for search_value.
        If found, return the index of search_value in the iterable. Otherwise,
        return -1.
    """
    for idx, item in enumerate(iterable):
        if item == search_value:
            return idx
    return -1