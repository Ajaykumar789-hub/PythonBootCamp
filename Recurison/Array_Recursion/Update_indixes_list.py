arrList = []
def updateIndixesList(l1,x,index, arrList):
    if len(l1) == index:
        return
    if l1[index] == x:
        arrList.append(index)
    updateIndixesList(l1,x,index+1, arrList)

updateIndixesList([1,2,3,4,2,5,2,6],2,0,arrList) 
print(arrList)

