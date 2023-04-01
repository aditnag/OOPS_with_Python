# 16. Take inputs from user to make a list. Again take one input from user and search it in the list and delete that element, if found. Iterate over list using for loop.


# Take inputs from user to make a list
my_list = []
while True:
    user_input = input("Enter an element for the list or press 'q' to stop: ")
    if user_input == 'q':
        break
    else:
        my_list.append(user_input)

ele_del = input("Enter an element to search and delete from the list: ")

for i in my_list:
    if ele_del == i:
        my_list.remove(ele_del)
        print(f"{ele_del} has been deleted from the list.")
        break
    else:
        print(f"{ele_del} is not in the list.")

print("The updated list is:")
for element in my_list:
    print(element, end=" ")
