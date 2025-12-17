my_list = [4, 3, 6, 1, 7]

#for i in range(len(my_list)):
    #for j in range(i + 1, len(my_list)):
        #if my_list[i] > my_list[j]:
            #my_list[i], my_list[j] = my_list[j], my_list[i]

#print(my_list)

#for i in range(0, len(my_list)):
    #my_list[0], my_list[i] = my_list[i], my_list[0]
    #for j in range(i , len(my_list)):
        #if my_list[i] > my_list[j]:
            #my_list[i], my_list[j] = my_list[j], my_list[i]
 
#print(my_list)


if len(my_list) > 1:
    my_list[0], my_list[-1] = my_list[-1], my_list[0]

print(my_list)

#if len(my_list) > 1:: This is a crucial safety check. It ensures that the code 
# only attempts a swap if the list contains at least two elements. 
# Trying to access my_list[0] and my_list[-1] on an empty list would cause an 
# IndexError, and swapping is meaningless on a list with only one element.

#my_list[0], my_list[-1] = my_list[-1], my_list[0]: This is the core of the 
# operation and a very "Pythonic" way to swap two values.

#my_list[0] accesses the first element of the list.
#my_list[-1] is a handy Python feature that accesses the last element of the list.
#This single line swaps the values at these two positions without needing a 
# temporary variable. It works by creating a temporary tuple (my_list[-1], 
# my_list[0]) behind the scenes and then unpacking its values back into the 
# list at the new positions.
#print(my_list): After the swap, this line prints the modified list