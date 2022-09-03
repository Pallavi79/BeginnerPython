import json


file = open("sample.txt","a")

# #Read file
# content = file.read()

# #Extract Characters

# # for char in content:
# #     print("1",char)


# #Extract lines
# lines = content.split("\n")
# print(lines)
# for line in lines:
#     print(line)




#write in a file

file.writelines(["hello !!"," This is my first line"])
file.close()


#another way

# with open("sample.txt") as f:
#     print(f.read())

# #another way if a json file

# with open("sample.txt") as f:
#     data=json.load(f)
#     print(data)

with open("config.json","r") as f:
    configuration = json.load(f)
    print(configuration["Environment"])
    print(configuration["Database_url"])