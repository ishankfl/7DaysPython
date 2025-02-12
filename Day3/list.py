# # list = [1,2,3,4,5]

# a = 1
# b = 2
# c = 3
# name = "ishanrumitaakash"

# list = ["ishan", "rumit", "aakash","binod", "chesta"]
# for i in range(0,len(list),2): #range(0,len(list))
#     print(list[i])
    


# #output: 
# """
# ishan
# next name

# next name
# """

# new_list = input("Enter a value of list: ")
# print(new_list)
# print(list(new_list))

# a = "2"
# b = "3"
# output = 2 + 3 = 5
# print(int(a)+int(b))
# new_list = []
# for i in range(1,4):
#     user_input = input("Enter item: ")
#     new_list.append(user_input)
#     print(new_list)
# print(new_list)

num_list = input("Enter a list of numbers separated by spaces: ").split()
new_list=[]
for i in num_list:
    new_list.append(int(i))
