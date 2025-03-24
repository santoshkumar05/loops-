list=[5,6,4,2,3,1,7,8,9,10]
for i in list:
    for j in range(len(list)-1):
        if list[j]>list[j+1]:
            list[j],list[j+1]=list[j+1],list[j]
print(list)
    