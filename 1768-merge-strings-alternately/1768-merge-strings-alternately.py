class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m = len(word1)
        n = len(word2)

        merge =[]
        i,j=0,0
        if(m==n):
            for i in range(m):
                merge.append(word1[i])
                merge.append(word2[j])
                i+=1
                j+=1

        elif(m<n):
            while (i<m):
                merge.append(word1[i])
                merge.append(word2[j])
                i+=1
                j+=1
            while(j<n):
                merge.append(word2[j])
                j+=1 
        else :
            while(j<n):
                merge.append(word1[i])
                merge.append(word2[j])
                i+=1
                j+=1
            while(i<m):
                merge.append(word1[i])
                i+=1    

        return "".join(merge)