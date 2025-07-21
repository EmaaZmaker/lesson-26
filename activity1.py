#adding two lists using Lambda and Maps
numbers1=[1,2,3]
numbers2=[4,5,6]
result=map(lambda x,y:x+y,numbers1,numbers2)
print(list(result))

#using map
list1=[1,2,3,4,5]
def square (n):
    return n*n
list2=list(map(square,list1))
print(list2)
