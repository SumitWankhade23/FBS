#Convert the time entered in hh,min and sec into seconds.
Time = int(input("Enter the seconds: "))

#Total 1 Hour = 60min * 60second = 3600 seconds

hh = Time // 3600
remain = Time % 3600

mm = remain // 60
ss = remain % 60

print("Total time: ", Time, "in seconds")
print("Hours: ", hh)
print("Minitues: ", mm)
print("Seconds: ", ss)


