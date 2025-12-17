global_variable = 10

def variable_scope ():
    scope_local = [1, 2, 3]
    print(scope_local)

def change_global ():
    global global_variable
    global_variable += 2
    print(global_variable)

change_global()

variable_scope()
#print(scope_local)
print(f'Variable local: {scope_local}')

