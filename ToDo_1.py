#PushFront
def pushfront(lst,frnt):
    newlst = []
    for i in range(0, len(lst)):
        if i == 0:
            newlst.append(frnt)

        newlst.append(lst[i]) 

    return newlst
mylst = [-1,1,1,1]
mylst2 = [1,6,-4,-2,-7,-2]
print("pushfront",pushfront(mylst,5))
print("pushfront",pushfront(mylst2,6))

#PopFront
def popfront(lst):
    newlst = []
    firststr = ""
    for i in range(0, len(lst)):
        if i == 0:
            firststr = lst[i]
        else:
            newlst.append(lst[i])

    newlst.append(firststr)
    return newlst
mylst = [-1,1,1,1]
mylst2 = [1,6,-4,-2,-7,-2]
print("popfront",popfront(mylst))
print("popfront",popfront(mylst2))

#Insert At
def insertat(lst,ipos,val):
    newlst = []
    for i in range(0, len(lst)):
        if i == ipos:
            newlst.append(val)
            newlst.append(lst[i])
        else:
            newlst.append(lst[i]) 

    return newlst
mylst = [-1,1,1,1]
mylst2 = [1,6,-4,-2,-7,-2]
print("insertat",insertat(mylst,2,9))
print("insertat",insertat(mylst2,3,9))

#Remove At
def removeat(lst,ipos):
    newlst = []
    for i in range(0, len(lst)):
        if i != ipos:
            newlst.append(lst[i]) 

    return newlst
mylst = [-1,1,1,1]
mylst2 = [1,6,-4,-2,-7,-2]
print("removeat",removeat(mylst,2))
print("removeat",removeat(mylst2,3))

#Swap Pairs
def swappairs(lst):
    newlst = []
    onestr = ""
    for i in range(0, len(lst)):

        if((i % 2 == 0)):
            onestr = lst[i]
        else:
            newlst.append(lst[i]) 
            newlst.append(onestr)
            onestr = ""
            

    if onestr != "":
        newlst.append(onestr)

    return newlst
mylst = [1,2,3,4,5]
mylst2 = [1,2,3,4,5,6]
print("swappairs",swappairs(mylst))
print("swappairs",swappairs(mylst2))

#Remove Duplicates
def removedupes(lst):
    newlst = []
    for i in lst:
        if i not in newlst:
            newlst.append(i) 
    return newlst
mylst = [-1,1,1,1]
mylst2 = [1,1,2,2,3,3,4,5,5,6]
print("removedupes",removedupes(mylst))
print("removedupes",removedupes(mylst2))