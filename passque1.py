# wap to find the sum of first n numbers. (using while)
n = 5
sum = 0
i = 1
while i<=n:
    sum += i
    i += 1

print("total sum:",sum)

# wap to find the factorial of n numbers.(using while)

n = 4
fac = 1
i = 1
while i<=n:
    fac *= i
    i += 1

print("total fac:",fac)

# using for
n = 4
fac = 1
for i in range(1 , n+1):
    fac *= i
print("factorial of n:",fac)