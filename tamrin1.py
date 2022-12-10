import math
m=int(input("enter the number of numbers"))
if m==2:
   a=int(input("enter number1:"))
   b=int(input("enter number2:"))
   op=input("enter operation")
   if op=="+":
      result=a+b
   if op=="-":
      if a>b:
         result=a-b
       else :
       result=b-a
   if op=="/":
      if a>b:
         result=a/b
      else :
         result=b/a
   if op=="*":
       if a>b:
          result=a*b
       else: 
       result=b*a
if m==1:
     a=int(input("enter number1:"))
   op=input("enter operation")
    if op=="factorial":
      result=math.factorial(a)
   if op=="sin":
      result=(math.sin(math.radians(a)))
   if op=="cos":
          result=(math.cos(math.radians(a)))

   if op=="tan":
        result=(math.tan(math.radians(a)))

        if op=="cot":
              result=(math.cot(math.radians(a)))
        if op=="radical":
             result=(math.sqrt(math.radians(a)))

print (result)