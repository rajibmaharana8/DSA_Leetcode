class Solution(object):
    def bestClosingTime(self, customers):
        n = len(customers)
        suffixY = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffixY[i] = suffixY[i + 1] + (1 if customers[i] == 'Y' else 0)
        
        min_penalty = float('inf')
        best_hour = 0
        prefixN = 0
        
        for j in range(n + 1):
            penalty = prefixN + suffixY[j]
            if penalty < min_penalty:
                min_penalty = penalty
                best_hour = j
            if j < n and customers[j] == 'N':
                prefixN += 1
        
        return best_hour