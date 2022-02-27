#for i in range(3):
#    user_input = input("Enter String \n")
#    action, value = user_input.split(' ')[0], user_input.split(' ')[1:]
#    action = action + "(" + ",".join(value) + ")"
    #action = action + "(" + "," + value + ")"
    #action += "(" + ",".join(value) + ")"
#    print(action)

string = "mukulVermamukulmuk"
substring = "muku"
length = len(substring)
counter = 0
for i in range(len(string)):
    check = string[i:length]
    if substring in check:
        counter += 1
    length += 1
print(counter)

