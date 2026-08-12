#Write a program to input any alphabet and check whether it is vowel or consonant.

alpha = input("Enter alphabet: ")
if alpha in 'aeiouAEIOU': 
    print(f"{alpha} is vowel")
else:
    print(F"{alpha} is consonant")    