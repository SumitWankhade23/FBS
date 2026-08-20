#WAP to calculate SI using Lambda function P,R,T input
intrest = lambda P,R,T: (P * R * T)/100 + P


res = intrest(1000,10,2)
print(res)