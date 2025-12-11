class Solution(object):
    def countCoveredBuildings(self, n, buildings):
        max_row = [0] * (n+1)
        min_row = [n+1] * (n+1)

        max_col = [0]* (n+1)
        min_col = [n+10]*(n+1)

        for p in buildings:
            x,y = p[0],p[1]

            #horizontal
            max_row[y] = max(max_row[y],x)
            min_row[y] = min(min_row[y],x)

            #vertical
            max_col[x] = max(max_col[x],y)
            min_col[x] = min(min_col[x],y)

        res = 0
        for p in buildings:
            x,y = p[0],p[1]
            if (
                x > min_row[y] and x <max_row[y] 
                and y > min_col[x] and y < max_col[x]):
                res+=1
        
        return res
        