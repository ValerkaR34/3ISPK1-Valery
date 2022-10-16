def fdd(n):

    count = 0
    for i in range(len(str(n))):
        if n[i] == '0':
            count += 1
        else:
            break

    return str(count)

