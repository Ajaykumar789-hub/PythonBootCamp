

def return_list_indices(l1,x, index):

    if len(l1) == index:
        return []
    sl = return_list_indices(l1,x,index+1)
    if l1[index] == x:
        sl.insert(0,index)

    return sl

anslist = return_list_indices([1,2,4,5,2,6],2,0)
print(anslist)