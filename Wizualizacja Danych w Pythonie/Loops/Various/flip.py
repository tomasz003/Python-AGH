n=int(input("Please type in a number: "))
list=[x for x in range(1,n+1)]

for i in range(0,n//2):
    c=list[2*i+1]
    list[2*i+1]=list[2*i]
    list[2*i]=c

for i in list:
    print(i)