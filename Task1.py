pr=int(input("Enter amount : "))
if(pr>=4000):
    dis=(pr*4)/100
    amt=pr-dis
    print("Final Balance : ",amt)
elif(pr>=3000):
    dis=(pr*3)/100
    amt=pr-dis
    print("Final Balance : ",amt)
elif(pr>=2000):
    dis=(pr*2/100)
    amt=pr-dis
    print("Final Balance : ",amt)
elif(pr>=1000):
    dis=(pr*1)/100
    amt=pr-dis
    print("Final Balance : ",amt)
else:
    amt=pr
    print("Final Balance : ",amt)