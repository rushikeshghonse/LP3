def alogrithm(n):
    if (n<=1):
        print('error')
    else:
        arr = []
        a = 0
        b = 1
        for i in range(2,n+1):
            c = a + b
            a = b
            b = c
            print(i)
            print("f = ",c)
            arr.append(c)
        ans = c
    return ans;
        
arr = [0,1]
n = int(input("Enter the No."))
print(alogrithm(n))