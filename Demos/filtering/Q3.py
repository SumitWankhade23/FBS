#add odd no from list to new list 
# li = [10,2,3,4,7,11,33]
# new=[]
# for i in li:
#     if i%2 != 0:
#         new.append(i)
# print(new)     
li = [10,2,3,4,7,11,33]   
new =[x for x in li if x%2 != 0]
print(new)
