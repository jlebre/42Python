def slice_me(family: list, start: int, end: int) -> list:
    """
    Slice list
    """
    members = len(family)
    size = len(family[0])
    for member in family:
        if len(member) != size:
            return

    if start > members or start < 0:
        return

    end = abs(end)
    if (members - end) < start:
        return

    new = []

    while start < end:
        new.append(family[start])
        start += 1

    Newmembers = len(new)
    Newsize = len(new[0])
    print(f"My shape is : ({members}, {size})")
    print(f"My new shape is : ({Newmembers}, {Newsize})")

    return new
