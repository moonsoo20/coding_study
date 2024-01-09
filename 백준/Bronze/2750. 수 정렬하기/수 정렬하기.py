x=int(input())
num_list=[]

for i in range(x):
    num_list.append(int(input()))
num_list2= sorted(num_list)

for i in range(x):
    print(num_list2[i])