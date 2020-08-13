def checkyear(i):
    if i!='':
        i=int(i)
        if i>0:
            if (i%4):
                return('a normal year')
            elif (i%4)==0 and (i%100)!=0:
                return('a leap year')
            elif (i%100)==0 and (i%400)!=0:
                return('a normal year')
            elif (i%400)==0:
                return('a leap year')
        else:
            return('')
    else:
        return('')
n = int(input(''))
for i in range(n):
    s = int(input(''))
    print(checkyear(s))
