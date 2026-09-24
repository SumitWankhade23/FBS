li = [1,3,2,6,9,11,12,15]
# new=[]
# for i in li:
#     if i%2 != 0:
#         new.append("odd")
#     else:
#         new.append("even")    
# print(new)

new = ["even" if i % 2 == 0 else "odd" for i in li]
print(new)