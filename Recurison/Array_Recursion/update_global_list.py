arrlist =[]
def update_global_list(l1, x, index):
    if len(l1) == index:
        return
    if l1[index] == x:
        arrlist.append(index)
    update_global_list(l1,x,index+1)

update_global_list([1,2,4,5,2,6,2], 2, 0)

print(arrlist)