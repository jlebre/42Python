def all_thing_is_obj(object: any)-> int:
    
    obj = type(object)

    if obj is list:
        print(f"List : {obj}")
    elif obj is tuple:
        print(f"Tuple : {obj}")
    elif obj is set:
        print(f"Set : {obj}")
    elif obj is dict:
        print(f"Dict : {obj}")
    elif obj is str:
        print(f"{object} is in the kitchen : {obj}")
    else:
        print("Type not found\n42", end='')
        return ''

