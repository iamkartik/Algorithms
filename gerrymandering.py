import numpy as np

def checkGerrymander(n,m,votes):
    vA=votes[0]
    mn = m*n
    max_p = n//2 
    majority = mn/4 + 1
    S = np.zeros((n,max_p,mn,mn))
    S[0][0][0][0] = True
    
    print(majority)
    print(S[0][0][0][0])
    
    for j in range(n):
        for k in range(max_p):
            for x in range(mn):
                for y in range(mn):
                    if x==0 or y==0 or k==0:
                        S[j][k][x][y] = True



    print('_____>')
    for j in range(1,n):
        for k in range(1,max_p):
            t = m*j
            for x in range(t):
                for y in range(t):
                    S[j][k][x][y] = S[j-1][k-1][x-vA[j]][y] or S[j-1][k][x][y-vA[j]]


    for i in range(0,n):
        for j in range(0,max_p):
            for k in range(mn):
                for l in range(mn):
                    if S[i][j][k][l] == True and k>majority and l>majority and j==max_p:
                        print(i,j,k,l)

    print(S[3][1][103][102])
    print(S[3][1][102][103])
                  
if __name__ =="__main__":
    n=4
    m=100
    votes =[[55, 43, 60, 47],[45, 57, 40, 53]]
    # m=80
    # votes =[[45, 50, 34, 56],[35, 30, 46, 24]]

    checkGerrymander(n,m,votes)