#print(r"FBs\tfirstbitSolution")
import re
#data = "My name is Virat and age is 36 or 37"
#re.findall(pattern,data)
# d = re.findall(r"\d+",data)
# d = re.search(r"\d+",data)#
#print(d.group())                                             #.group() method work on match object and return 

#data = "36My name is Virat and age is 36 or 37"
#re.findall(pattern,data)
# d = re.match(r"\d+",data)                                   #if starting me available hoga to return karega if not it returns NONE
# print(d)

# d = re.fullmatch(r"\d+","I12345")
# #print(d.group())
# print(d)

# data = "Pradip Mock is Easy"
# re.sub("Easy","Worthy",data)
# print(re.sub("Easy","Worthy",data))
# print(data)


# print(re.findall(r'\D',"ABCDEF1234#^&!_"))
# print(re.findall(r'\w',"ABCDEF1234#^&!_"))
# print(re.findall(r'\W',"ABCDEF1234#^&!_"))
# print(re.findall(r'\s',"I am good"))
# print(re.findall(r'c.t',"cut cat caut"))

##-------------------------------------------------------
print(re.findall('ab*',"abcd abd ab"))
print(re.findall('ab?',"abcd abd ab"))
print(re.findall(r'\w{2}',"abc abcd ab abcde"))
print(re.findall(r'\w{3,4}',"abc abcd ab abcde"))
print(re.findall("[aeiou]","I am good in pYthon"))
print(re.findall("[1-9]{1}","I am good in pYthon47896"))
print(re.findall("[1-9]{2}","I am good in pYthon47896"))
print(re.findall("[1-9]$","I am good in pYthon9"))


