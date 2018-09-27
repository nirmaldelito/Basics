def pal(word):
    new = word.lower()
    space = new.replace(" ", "")
    rev = space[::-1]
    if space == rev:
        return True
    else:
        return False


ans = pal("A nut for a jar of tuna")
print(ans)
