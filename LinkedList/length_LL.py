from common import Node, take_input_better, print_LL

def length_ll(head):
    temp = head
    ans = 0
    while(temp != None):
        temp = temp.next 
        ans += 1
    return ans

headll = take_input_better()
length = length_ll(headll)
print(length)

def length_ll_recu(head):
    if head == None: ##base case
        return 0
    smallans = length_ll_recu(head.next) ##recursion
    return 1 + smallans #ourwork

length = length_ll_recu(headll)
print(length)