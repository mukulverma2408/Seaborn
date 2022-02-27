#list_comp = [[i,j,k] for i in range(2) for j in range(2) for k in range(2)]

list_comp = [[i,j,k] for i in range(2) for j in range(2) for k in range(2) if (i+j+k) !=2]
print(list_comp)
#for item in list_comp:
#    if (sum(item)) != 2:
#        print(item, end='')
    #print(item, end='')


