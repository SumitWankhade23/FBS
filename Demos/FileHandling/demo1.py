f = open("abc.txt",'w')
f.write("MI won the cup\nChennai won the Cup")
f.writelines(["\nMI won the cup","\nChennai won the Cup"])
f = open("abc.txt","a")
f.write("\nCSK won the cup 5")
with open("abc.txt","a") as f:
    f.write("\nKKR won the cup")

