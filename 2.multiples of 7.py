def mul(a, b):
    pro = 0
    for n in range(a, b):
        if n % 7 == 0:
            pro += n
    return pro


ans = mul(1107, 21000)
print(ans)
