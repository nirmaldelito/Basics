def mul(a,b):
    sum = 0
    for n in range(a,b):
        if n % 7 == 0:
            sum += n
    return(sum)

q = mul(100,150)
print(q)
