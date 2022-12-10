name=input("enter name: ")
family=input("enter family: ")
a=int(input("enter nomre 1: "))
b=int(input("enter nomre 2: "))
c=int(input("enter nomre 3: "))
ave=(a+b+c)/3
if ave>=17:
    result=" \n create"
if ave>=12 and ave <17:
    result="\n normal"
if ave <12:
    result="\n fai"
    print("status",result)