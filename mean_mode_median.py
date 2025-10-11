list  = [30,43,67,87,56,44,32,43]
#mean
mode  = sum(list)/len(list)
print(mode)
#median
list.sort()
if(len(list)%2==0):
    median = (list[len(list)//2]+list[len(list)//2-1])/2
else:
    median = list[len(list)//2]
print(median)
#mode
mode_count = 0
for i in list:
    count = list.count(i)
    if(count>mode_count):
        mode = i
        mode_count = count
print(mode)
