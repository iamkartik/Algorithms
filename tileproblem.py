import numpy as np

def tileMarker(n,a,b):
    m = 2**n
    grid = np.zeros((m,m))
    global tileNo
    tileNo = 0
     
    grid[a][b]=-1
    tiler(grid,a,b,m,0,0)
    
    print(grid)


def findExcludedTile(mid_x,mid_y, a,b):
    ex=mid_x 
    ey=mid_y
    q=1
    
    if a<mid_x and b<mid_y:
        ex=mid_x-1
        ey=mid_y-1
        q=1
    elif a<mid_x and b >= mid_y:
        ex=mid_x-1 
        ey=mid_y
        q=2
    elif a>=mid_x and b < mid_y:
        ex=mid_x 
        ey=mid_y-1
        q=3
    else:
        ex=mid_x 
        ey=mid_y
        q=4
    return (ex,ey,q)


def tiler(grid,a,b,m, ox,oy):
    if m ==1:return

    mid = m//2

    mid_x =  ox+mid
    mid_y =  oy+mid
    # find excluded tile quadrant and put tile in the others
    ex,ey,q = findExcludedTile(mid_x,mid_y,a, b)
    # print(ex,ey,q)
    putTile(mid_x-1,mid_y-1,mid_x,mid_y,ex,ey,grid)
    

    if q==1:
        tiler(grid,a,b,m//2,ox,oy)
        tiler(grid,mid_x-1,mid_y,m//2,ox,mid_y)
        tiler(grid, mid_x, mid_y-1, m//2, mid_x, oy)
        tiler(grid,mid_x,mid_y,m//2,mid_x,mid_y)
    elif q==2:
        tiler(grid,mid_x-1,mid_y-1,m//2,ox,oy)
        tiler(grid,a,b,m//2,ox,mid_y)
        tiler(grid, mid_x, mid_y-1, m//2, mid_x, oy)
        tiler(grid,mid_x,mid_y,m//2,mid_x,mid_y)
    elif q==3:
        tiler(grid,mid_x-1,mid_y-1,m//2,ox,oy)
        tiler(grid,mid_x-1,mid_y,m//2,ox,mid_y)
        tiler(grid, a, b, m//2, mid_x, oy)
        tiler(grid,mid_x,mid_y,m//2,mid_x,mid_y)
    else:
        tiler(grid,mid_x-1,mid_y-1,m//2,ox,oy)
        tiler(grid,mid_x-1,mid_y,m//2,ox,mid_y)
        tiler(grid, mid_x, mid_y-1, m//2, mid_x, oy)
        tiler(grid,a,b,m//2,mid_x,mid_y)



def putTile(x1,y1,x2,y2,a,b,grid):
    # print('In put tile',x1,y1,x2,y2,a,b,tileNo)
    global tileNo 
    tileNo +=1
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            if i == a and j==b:
                continue
            else:
                grid[i][j]=tileNo

if __name__ == "__main__":
    tileMarker(3,4,4)