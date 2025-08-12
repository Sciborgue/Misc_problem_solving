def triangle(row):
    newrow = ""
    for i in range(len(row) - 1):
        a = row[i]
        b = row[i + 1]
        base = ["B", "G", "R"]
        if a == b:
            newrow = newrow + a
        else:
            base.remove(a)
            base.remove(b)
            newrow = newrow + base[0]
    # lancer la récursive
    if len(newrow) == 1:
        return newrow
    else:
        return triangle(newrow)


print(triangle("RGBG"))

o = "RGBG"
print(o[0])
print(o[1])
print(o[2])
print(o[3])
