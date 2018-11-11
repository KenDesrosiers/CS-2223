######################################################################################
#
#
#  Name: Kenneth Desrosiers
#  Date: 4/25/2018
#
#  This project compares two approaches to solving the cut rod problem.  A top down
#  approach and a bottom up approach.
#
#   
#
####################################################################################
import time 
def BottomCutRod(p, n):
    r, s = [], []
    for i in range(0, n+1):
        r.append(-1)
        s.append(0)
    r[0] = 0  
    for j in range(1, n+1):
        q = -1
        for i in range(1, j+1):
            if q < p[i]+r[j-i]:
                q = p[i]+r[j-i]
                s[j] = i
        r[j] = q
    return r, s

def PrintCutRod(p, n):
    r, s = BottomCutRod(p, n)
    print ('max revenue is', r[n])
    while n>0:
        print (s[n])
        n = n-s[n]

def topDownCutRod(p, n):
    r, s = [], [] 
    for i in range(0, n+1): 
        r.append(-1)
        s.append(0)
    return topDownCutRodhelp(p, n, r, s), s

def topDownCutRodhelp(p, n, r, s):
    if r[n]>=0:
        return r[n]    
    if n is 0:
        q = 0
    else:
        q = -1
        for i in range(1, n+1):
            if q < p[i] + topDownCutRodhelp(p, n-i, r, s):
                q = p[i] + topDownCutRodhelp(p, n-i, r, s)
                s[n] = i
    r[n]=q
    return q

def PrintCutRod2(p, n):
    q, s = topDownCutRod(p, n)
    print ('max revenue is', q)
    while n>0:
        print (s[n])
        n = n-s[n]

