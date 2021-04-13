
def sameFirstLast(string):
    """
    Takes sentence of words and returns tuple of words which starts and end with same characters.
    Parameter: string type: str
    Return: tup type: tuple
    """
    tup =()
    count=0
    pos1=string.find(' ')
    while pos1!= -1:
        text=string[count:pos1]
        if text[0].lower() ==text[-1].lower():
            tup+=(text,)
        count=pos1+1
        pos1=string.find(' ',count)
    return tup

inp = input("Enter word: ")
word=sameFirstLast(inp)

for i in word:
    print(i)
