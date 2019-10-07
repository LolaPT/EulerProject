limit = 30000000
n = 20

for x in range(1, limit):
    flag = True

    for y in range(1, n+1):
        if x % y != 0:
            flag = False
            break
    if flag:
        print(x)
