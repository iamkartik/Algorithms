import numpy as np

def lcs(a,b,c,m,n,p,t):
    if m<0 or n<0 or p<0:
        # print(t)
        return 0
    else:
        if a[m]==b[n]==c[p]:
            t=f'{t}{a[m]}'
            return 1+lcs(a,b,c,m-1,n-1,p-1,t)
        else:
            return max(
                lcs(a,b,c,m-1,n,p,t),
                lcs(a,b,c,m,n-1,p,t),
                lcs(a,b,c,m,n,p-1,t)
            )

def lcsdp(a,b,c):
    m=len(a)
    n=len(b)
    p=len(c)
    t=""
    dp=np.zeros((m+1,n+1,p+1))
    # print(dp)

    for i in range(m+1):
        for j in range(n+1):
            for k in range(p+1):
                if i==0 or j==0 or k==0:
                    continue

                if a[i-1]==b[j-1]==c[k-1]:
                    dp[i][j][k]=dp[i-1][j-1][k-1]+1
                else:
                    dp[i][j][k] = max(
                        dp[i-1][j][k],
                        dp[i][j-1][k],
                        dp[i][j][k-1]
                    )

    print(dp[m][n][p])
    print(i,m,j,n,k,p)

    str=""
        

    while i>0 and j>0 and k>0:
        # print(i,j,k)
        if a[i-1]==b[j-1]==c[k-1]:
            print(a[i-1])
            str=f'{a[i-1]}{str}'
            i-=1
            j-=1
            k-=1
            # print(i,j,k)
        else:
            n1=dp[i-1][j][k]
            n2=dp[i][j-1][k]
            n3=dp[i][j][k-1]
            if n1>=n2 and n1>=n3:
                i-=1
            elif n2>=n1 and n2>=n3:
                j-=1
            elif n3>=n1 and n3>=n2:
                k-=1
            else:
                print('##',n1,n2,n3)

    print(str) 

if __name__ == "__main__":
    a="6662220542630314443712"
    # a="ACHCGGTCGAGTTGCGCGGAHAGCCLGGCCGAA"
    b="00078321207413782377777"
    # b="GTCXGTTCGDGAATGFCGTTGCTOTGTAAA"
    c="6664664567861104057425"
    # c="AKLGTCGTCGGAAUIOGCCGGCCGAA"
    

    m=len(a)
    n=len(b)
    p=len(c)
    t=""
    print(m)
    # test=lcs(a,b,c,m-1,n-1,p-1,t)
    lcsdp(a,b,c)

    