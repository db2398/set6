m,u=map(int,input().split())
l=list(map(int,input().split()[:m]))
count=0
for i in l:
   if(i==u):
      print("yes")
      break
else:
   print("no")
