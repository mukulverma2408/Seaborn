def reverse_pattern(n):
    my_list = []
    for i in reversed(range(n)):
        my_list.append("*"*i)
    print("\n".join(my_list))
    #print(my_list)

def pattern(n):
    my_list = []
    for i in range(n):
        my_list.append("*"*i)
    print("\n".join(my_list))
    #print(my_list)

def star_pattern(n):
    space = n-1
    for k in range(space):
        print("", end='')



#reverse_pattern(5)
#pattern(5)