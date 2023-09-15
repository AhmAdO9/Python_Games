def cal(*numbers):
   x =  list(numbers)
   y = len(x)
   count = 0
   while count < y:
      if count == (y-1):
         return p
      p = x[0]+x[1]
      x.pop(0)
      x.pop(0)
      x.insert(0,p)
      count +=1
   return p
     


print(cal(1,2,3))
