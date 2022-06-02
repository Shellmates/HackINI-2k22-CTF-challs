# chess.INI

## Write-up

```py
def solver(a,start,end):
    m=[]
    def make_step(k):
        for i in range(len(m)):
            for j in range(len(m[i])):
                if m[i][j] == k:
                    if i>0 and m[i-1][j] == 0 and a[i-1][j] == 0:
                        m[i-1][j] = k + 1
                    if j>0 and m[i][j-1] == 0 and a[i][j-1] == 0:
                        m[i][j-1] = k + 1
                    if i<len(m)-1 and m[i+1][j] == 0 and a[i+1][j] == 0:
                        m[i+1][j] = k + 1
                    if j<len(m[i])-1 and m[i][j+1] == 0 and a[i][j+1] == 0:
                        m[i][j+1] = k + 1

                    if i>0 and j>0 and m[i-1][j-1] == 0 and a[i-1][j-1] == 0:
                        m[i-1][j-1] = k + 1
                    if i<len(m)-1 and j<len(m[i])-1 and m[i+1][j+1] == 0 and a[i+1][j+1] == 0:
                        m[i+1][j+1] = k + 1
                    if i<len(m)-1 and j>0 and m[i+1][j-1] == 0 and a[i+1][j-1] == 0:
                        m[i+1][j-1] = k + 1
                    if j<len(m[i])-1 and i>0 and m[i-1][j+1] == 0 and a[i-1][j+1] == 0:
                        m[i-1][j+1] = k + 1


    for i in range(len(a)):
        m.append([])
        for j in range(len(a[i])):
            m[-1].append(0)
    i,j = start
    m[i][j] = 1

    k = 0
    while m[end[0]][end[1]] == 0:
        k += 1
        make_step(k)

    i, j = end
    k = m[i][j]
    the_path = [(i,j)]
    while k > 1:
        if i > 0 and m[i - 1][j] == k-1:
            i, j = i-1, j
            the_path.append((i, j))
            k-=1
        elif j > 0 and m[i][j - 1] == k-1:
            i, j = i, j-1
            the_path.append((i, j))
            k-=1
        elif i < len(m) - 1 and m[i + 1][j] == k-1:
            i, j = i+1, j
            the_path.append((i, j))
            k-=1
        elif j < len(m[i]) - 1 and m[i][j + 1] == k-1:
            i, j = i, j+1
            the_path.append((i, j))
            k -= 1
            

        elif i>0 and j>0 and m[i - 1][j-1] == k-1:
            i, j = i-1, j-1
            the_path.append((i, j))
            k-=1

        elif i<len(m)-1 and j<len(m[i])-1 and m[i+1][j+1] == k-1:
            i, j = i+1, j+1
            the_path.append((i, j))
            k-=1

        elif  i<len(m)-1 and j>0 and m[i+1][j-1] == 0 and  m[i + 1][j] == k-1:
            i, j = i+1, j-1
            the_path.append((i, j))
            k-=1
        elif j<len(m[i])-1 and i>0 and m[i-1][j + 1] == k-1:
            i, j = i-1, j+1
            the_path.append((i, j))
            k -= 1
    return the_path
```
## Flag

`shellmates{ch355_M4k35_M3n_w153r_4nd_CL34R-519H73D}`
