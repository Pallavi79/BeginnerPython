#using tuples

# records=[("x",100),("y",90),("z",80)]
# queries=["x","z"]

# for query in queries:
#     for record in records:
#         if(record[0]==query):
#             print(record[1])


#using dictionary
# records = {
#     "x":20,
#     "y":50,
#     "z":100
# }
# queries=["x","z"]

# for query in queries:
#     print(records[query])

# records2=records
# print(records,records2)
# records["x"]=80
# print(records,records2)

# records3=records.copy()
# print(records3)
# records3["y"]=60
# print(records,records3)

# print(records.get("x"))
# print(records.keys())



#set
# s=set()
# s.add(1)
# s.add(2)
# s.add(1)
# print(s)


# arr=[1,2,3,4,5,6,1,2,3,4]
# print(len(set(arr)))


#strings

# s="Soham Mukherjee"
# print(s)
# name = s.split(" ")
# print(name)
# first_name,last_name = s.split(" ")
# print(first_name)


# ip = input()
# print(ip)
# separated_integers=ip.split(" ")
# print(separated_integers)

# for i in range (len(separated_integers)):
#     separated_integers[i]=int(separated_integers[i])

# print(separated_integers)


# arr = list(map(int,input().split()))
# print(arr)

s = "    soham mukherjee    "
print(s)
print(s.strip().replace("ham","ya"))

digit="2"
print(digit.zfill(2))
print(digit.zfill(3))
