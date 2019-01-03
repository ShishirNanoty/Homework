myUniqueList = []
myLeftovers = []
print('Original',myUniqueList)

def addleftovers(rejected):
    myLeftovers.append(rejected)

def additems(new):
    val = False
    if not new in myUniqueList:
        myUniqueList.append(new)
        val = True
    else: addleftovers(new)
    return val
while True:
    x = input('Enter No:')
    if x == 'done': break
    y = additems(x)
    print('Unique',myUniqueList,y)
    print('Duplicates',myLeftovers)
print('Done!')
