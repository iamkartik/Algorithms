def rain_brute(arr,mean):
    n = len(arr)
    maxl=0
    maxr=0
    maxdef=0
    count=0
    for l in range(0,n):
        defI=0
        for r in range(l,n):
            count+=1
            defI+=arr[r]
            defIm = (r-l+1)*mean
            idef=defIm-defI   
            # print(l,r,'--->',defIm,defI,idef) 
            if idef>maxdef:
                maxdef=idef
                maxl = l
                maxr = r
    print(count,'*****',maxdef,'[',maxl,',', maxr,']')
            
def rain_dp(arr,mean):
    n= len(arr)
    opt = [0]*(n)
    test = [0]*(n)

    test[0] = mean - arr[0]
    test_def=0
    tr=0
    tl=0
    for i in range(1,n):
        x=mean - arr[i]
        test[i] = max(x,x+test[i-1])
        if test[i]>test_def:
            test_def = test[i]
            tr = i
        
        if test[i]<0:
            tl = i+1

    print(test)
    print(test_def,tl,tr)
    



    for i in range(n):
        opt[i] = mean - arr[i]

    max_c = max_g = -99999999
    l = 0
    r = 0
    for i in range(1,n):

        max_c = max(opt[i-1]+max_c, opt[i-1])
        
        if max_c > max_g:          
            max_g = max_c
            r=i-1
        if max_c <0:
            l = i              
        
    print(max_g)
    # print(opt)
    print(l,r)
        

if __name__ == "__main__":
    arr=[10,14,13,2,2,3,1,1,3,12,4,6,7,0,1,23,1,1,1,12,12,3,44,1,2,2,12]
    # arr=[1,1,2,2,6,6]
    # arr=[1,1,1,3,4]
    mean = sum(arr)/len(arr) 
    print(mean)
    rain_brute(arr,mean)
    rain_dp(arr,mean)