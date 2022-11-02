def main(list1):
    """
    A list of several elements is given. Return this list by adding the reverse.
    Args:
        list1(list): parameter
    Returns:
        list: return answer.
    """
    b=list1.copy()
    a=[]
    while list1:
        a+=[list1.pop()]
    
    return b+a
