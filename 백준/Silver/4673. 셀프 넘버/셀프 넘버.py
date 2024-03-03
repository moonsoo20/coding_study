
def selfnum(n):
    num=list(str(n))
    asw=n
    for i in range(len(num)):
        asw+=int(num[i])
    return asw

SET=list(range(1,10001))
for n in range(1,10001):
    if selfnum(n) in SET:
        SET.remove(selfnum(n))

for i in range(len(SET)):
    print(SET[i])
