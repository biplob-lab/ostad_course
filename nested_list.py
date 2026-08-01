my_favourite_list= ["football","ROnaldo",["Gta v","Last of US"]]
print(my_favourite_list[2][0])
m=[]
""" Without nested loop
for i in range(5):#(0,1,2,3,4)
    m.append([])#creat empty list
    for j in range(5):
       m[i].append(j)
print(m) """
#List comprehension
m = [[c for c in range(5)] for b in range(5)]
print (m)