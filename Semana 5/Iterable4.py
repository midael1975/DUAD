my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

pair_lists = []
for i in my_list:
    if i % 2 == 0:
        pair_lists.append(i)


print(pair_lists)

#pair_lists = []: An empty list named pair_lists is created. This list will be 
# used to store the even numbers that are found. (Note: In Spanish, "números pares" means "even numbers," so the variable name likely intends to mean even_list).

#for i in my_list:: This loop iterates through each element in my_list. 
# In each pass of the loop, the variable i will hold one of the numbers from 
# the list (from 1 to 9).

#if i % 2 == 0:: This is the filtering condition.

T#he modulo operator (%) gives the remainder of a division.
#i % 2 will be 0 if the number i is perfectly divisible by 2 (i.e., it's an even 
# number).
#It will be 1 if the number is odd.
#So, this if statement checks if the current number i is even.
#pair_lists.append(i): If the condition in the if statement is true, this line 
# adds the even number i to the pair_lists.

#print(pair_lists): After the loop has checked every number in my_list, this line 
# prints the final pair_lists