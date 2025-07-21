def sq_n(n):
    return n*n
list1=[1,2,3,4,5]
new_list=map(sq_n,list1)
print(list(new_list))