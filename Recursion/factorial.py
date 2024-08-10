def factorial(n):
    if n == 0 :
        return 1 
    ans = n * factorial(n-1)
    return ans

print(factorial(4))
