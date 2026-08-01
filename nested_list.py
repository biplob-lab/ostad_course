""" my_favourite_list= ["football","ROnaldo",["Gta v","Last of US"]]
print(my_favourite_list[2][0])
m=[] """
""" Without nested loop
for i in range(5):#(0,1,2,3,4)
    m.append([])#creat empty list
    for j in range(5):
       m[i].append(j)
print(m) """
""" #List comprehension
m = [[c for c in range(5)] for b in range(5)]
print (m) """

""" m = [[2,3,5],[4,9,11],[6,3,5]]
odds = [e for r in  m for e in r if e %2 !=0]
print (set(odds)) """

m = [["apple","banana","cherry"],
     ["date","grape","lichi"]]
capitalize = [[f.capitalize() for f in r] for r in m]
print(capitalize)


