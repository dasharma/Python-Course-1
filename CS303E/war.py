

def winningPlayer(c1, c2):

    if c1==0:
        c1=10
    elif c2==0:
        c2=10

    if c1>c2:
        return(1)
    elif c2>c1:
        return(2)
    else: return(3)

A=1
J=11
Q=12
K=13

def simulateWar():
    A=1
    J=11
    Q=12
    K=13
    score = 0
    p2 = 0
    p1 = 0
    for x in range(1,3):
        c1 = input()
        c2 = input()
        score = winningPlayer(c1,c2)
        if score==3:
            p2=p2+1
            p1=p1+1
        elif score==1:
            p1=p1+1
        elif score==2:
            p2=p2+1
        score = 0

    print(p1,p2)
