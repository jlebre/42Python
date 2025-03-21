def load(path: str)-> Dataset: 
    """
    your code here
    (You have to adapt the type of return
    according to your library)
    """
    try:
        file = open(path)
        for i in file:
            count += 1
            
        return count
        
    except Exception as error:
        print(f"Error: {error}")