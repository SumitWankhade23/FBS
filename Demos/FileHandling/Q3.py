#WAP a code for alternate odd number from list
# li = [1, 6, 2, 21, 19, 12, 27]

# result = []
# take = True                    
# for x in li:
#     if x % 2 != 0:            
#         if take:
#             result = result + [x]
#         take = not take        

# print("Alternate numbers:", result)

li = [1,9,2,21,18,12,9]
alternate = 0
for i in li:
    if(i%2!=0):
        if (alternate%2==0):
            print(i)
        alternate = alternate+1