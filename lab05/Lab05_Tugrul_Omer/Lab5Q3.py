def seperate(l):
    """
    Takes list of n integer elements and produces a dictionary where keys are integers in the list and values will be
    tuples of having two integer numbers for the two halves of the number in the key.
    Parameter: l type:list
    Returns: dic type: dictionary
    """
    dic={}
    for el in l:
        if el%2==0:
            dic[el]=(el//2,el//2)
        else:
            dic[el]=(el//2 +1,el//2 )
    return dic

l = [5,8,12,17,5]

print(seperate(l))