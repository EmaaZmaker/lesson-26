#zip elements of 2 lists

s1={1,2,3}
s2={"a","b","c"}
s3=list(zip(s1,s2))
print(s3)
list1=[1,2,3]
list2=[4,5,6]
for x,y in zip(list1,list2[::-1]):
    print(x,y)
name=["RIggy","Jack"]
roll_number=[1,2]
new_dict={i:j for i,j in zip(name,roll_number)}
print(new_dict)
