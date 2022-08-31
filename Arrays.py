# marks =[100,20,30,60,90,50]
# print(marks)
# print(len(marks))
# total=0
# for i in range(0,len(marks)):
#     total+=marks[i]

# print(total)
# total=0
# for value in marks:
#     total+=value
# print(total)

# def greet(name):
#     print("Hello " ,name)

# names=["John","Tony","Lily","Nancy"]

# for n in names:
#     greet(n)



#some inbuilt functions

# arr=[]
# arr.append(30)
# arr.append(10)
# arr.append(20)
# print(arr)
# arr.sort()
# print(arr)
# arr.pop()
# print(arr)
# arr.insert(2,50)
# print(arr)



#Create an array of len 20

# arr=[]
# for i in range(0,20):
#     arr.append(0)

# print(len(arr))

# #or
# arr2 =[0]*20
# print(len(arr2))


#2D Arrays

# mat=[[0]*3]*2
# print(mat)
# print(len(mat))

# for i in range(2):
#     for j in range (3):
#         print(mat[i][j], end=" ")
#     print(" ")



#Tuples

# record_1 =("soham",10)
# print(record_1)

# records=[("soham",20),("John",50)]
# print(records)



#list
arraylist = list()
arraylist.append(1)
arraylist.append(2)
arraylist.append(3)
print(arraylist)
#insert at a particulat position
arraylist.insert(1,6)
print(arraylist)
#remove the last element
arraylist.pop()
print(arraylist)
#sort the list
arraylist.sort()
print(arraylist)
#sort in reverse order
arraylist.sort(reverse=True)
print(arraylist)

#values will change in both lists
arraylist2=arraylist
arraylist2[1]=8
print(arraylist,arraylist2)
print(arraylist2)
arraylist.append(9)
print(arraylist,arraylist2)

#values will not change in both lists
arraylist3=arraylist.copy()
print(arraylist3)
arraylist3[2]=5
print(arraylist,arraylist3)
#count the number of 1's
print(arraylist.count(1))
#remove any particular element
arraylist.remove(1)
print(arraylist)
#append another list
arraylist4 = arraylist.__add__([1,2,3,4])
print(arraylist4)
