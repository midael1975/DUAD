first_list = ['Hay', 'en', 'que', 'iteracion', 'indices', 'muy']
second_list = ['casos', 'los', 'la', 'por', 'es', 'util']


#def mix_lists(first_list, second_list):
    #mix_lists = []
   # max_len = max(len(first_list), len(second_list))
    #for i in range(max_len):
      #  if i < len(first_list):
       #     mix_lists.append(first_list[i])
       # if i < len(second_list):
        #    mix_lists.append(second_list[i])
    #return mix_lists

#result = mix_lists(first_list, second_list)
#print(result)


for i in range(len(first_list)):
    print(first_list[i], second_list[i])

#range(len(first_list)): This creates a sequence of numbers starting from 0 up to 
# the length of first_list. Since first_list has 6 elements, this generates the 
# numbers 0, 1, 2, 3, 4, 5.

#for i in ...: This loop iterates through the sequence of numbers. 
# In each iteration, the variable i holds the current number 
# (which serves as an index).

#print(first_list[i], second_list[i]): Inside the loop, i is used as an index 
# to access an element from first_list and an element from second_list at the same 
# position.
