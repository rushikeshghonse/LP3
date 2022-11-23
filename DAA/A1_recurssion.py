def feb(n):
  if(n<=1):
    return n
  else:
    return (feb(n-1) + feb(n-2))

n=int(input("Enter Digit"));
print(feb(n))
