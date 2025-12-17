my_string = 'Pizza con piña'

#for i in range(len(my_string) - 1, -1, -1):
    #print(my_string[i])
    
#- len(my_string) - 1 is the index of the last character.
#- -1 is the lower bound (before index 0).
#- -1 as a step indicates that we're going backward.

for i in my_string[::-1]:
    print(i)
    
#my_string[::-1]: This is the core of the technique. It uses Python's "slice" notation.

#-A slice is written as [start:stop:step].
#-When you omit start and stop and provide a step of -1, you are telling Python: 
# "Go through the entire string, but step backward one character at a time."
#-This effectively creates a new, reversed copy of the original string. 
# For my_string = 'Pizza con piña', the expression my_string[::-1] evaluates 
# to 'añip noc azziP'.
