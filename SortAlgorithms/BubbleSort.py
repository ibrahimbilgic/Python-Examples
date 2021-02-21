number_list = [10,2,5,6,7,4]

for i in range(len(number_list)):
    for j in range(i):
        if int(number_list[j]>int(number_list[j+1])):
            number_list[j],number_list[j+1] = number_list[j+1],number_list[j]
    print(F"Step{i}: {number_list}")
print (number_list)