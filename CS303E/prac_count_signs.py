neg = int()
pos = int()
hold = int()

num = int(input())

if num == 0:
    print(0, 0)

else:
    hold = num
    if hold > 0:
        pos = pos + 1
    else: neg = neg + 1
    
    while True:
        num = int(input())

        if num != 0:
            if num>0:
                pos = pos+1
            elif num<0:
                neg = neg+1
        elif num == 0:
            break

    print(pos,neg)

            
