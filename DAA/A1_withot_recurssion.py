n=int(input("Enter digit:"))

if(n<=1):
  print(n)
else:
  n1=0
  n2=1
  for x in range(n-1):
    feb=n1+n2
    n1=n2
    n2=feb
  print(feb)
  
#recursive methode


