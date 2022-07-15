t= int(input())

while(t):
    t= t-1
    p, sum1 = 0, 0
    n= int(input())
    x = [int(i) for i in input().split()]
    for i in range(n):
        if (x[i] == 1):
            print("Chef")
            break
        sum1 += x[i]
    else:
        if (sum1%2==0):
            print("Chefina")
        else:
            print("Chef")
    