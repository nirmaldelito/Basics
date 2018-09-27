def x(word):
    pop = word[::-1]
    if word == pop:
        return True
    else:
        return False

a = x('malayalam')
print(a)
