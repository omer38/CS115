def longest(l_string):
    """
    Takes list of string as a parameter and returns longest words in new list
    Parameter: l_string type:list
    Returns: a_list type:list
    """
    long=0
    n_list=[]
    a_list=[]
    for i in l_string:
        if long < len(i):
            long=len(i)
            n_list.append(i)
        elif long == len(i):
            n_list.append(i)
    for i in n_list:
        if len(i)==long:
            a_list.append(i)

    return a_list


o_list = ['abc', 'qwe', 'sss', 'x123', 'nnnn', 'atat', '43215']
print("Original List: \n",o_list,"\n")
print("New List: \n",longest(o_list))
