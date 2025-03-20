def ft_filter(function, iterable):
    """
    Return an iterator yielding those items of iterable
    for which function(item) is true. If function is None,
    return the items that are true.
    """

    new = []

    for i in iterable:
        if function(i) is True:
            new.append(i)

    return new
