def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """
    give bmi
    """

    if len(height) != len(weight):
        return

    if not all(int or float for c in height):
        return

    if not all(int or float for c in weight):
        return

    bmi = []

    for i, b in enumerate(height, 0):
        res = (weight[i] / b) / b
        bmi.append(res)

    return bmi


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    apply limit
    """
    if not all(int or float for c in bmi):
        return

    ret = []
    for c in bmi:
        if c > limit:
            ret.append(True)
        else:
            ret.append(False)

    return ret
