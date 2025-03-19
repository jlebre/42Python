def NULL_not_found(object: any)-> int:
    obj = type(object)

    # Python 3.0 para cima já não tem NoneType
    NoneType = type(None)

    if obj is NoneType:
        print(f"Nothing : {object} {obj}")
        return 0
    elif obj is float:
        print(f"Cheese : {object} {obj}")
        return 0
    elif obj is int:
        print(f"Zero : {object} {obj}")
        return 0
    elif object == '"':
        print(f"Empty : {obj}")
        return 0
    elif obj is bool:
        print(f"Fake : {object} {obj}")
        return 0
    else:
        print("Type not found")
        return 1