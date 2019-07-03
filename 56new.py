sm=input()
for i in range(0,len(sm)):
   if(sm[i].isalpha() and sm[i].isdigit()):
    print("No")
else:
  print("Yes")
