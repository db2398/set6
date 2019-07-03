u,v=map(int,input().split())
l=list(map(int,input().split()[:u]))
count=0
for i in l:
   if(i==v):
      count=count+1
print(count)      
