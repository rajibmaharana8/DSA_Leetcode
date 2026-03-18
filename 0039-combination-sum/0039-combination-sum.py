class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def solve(idx,total,subset,result):

            if total == target:
                result.append(subset.copy())
                return
            elif total>target:
                return
            if idx >= len(candidates):
                return

            subset.append(candidates[idx])
            summ = total + candidates[idx]
            solve(idx , summ ,subset , result)

            subset.pop()
            solve(idx+1,total,subset,result)

        subset = []
        result = []
        
        solve(0,0,subset,result)

        return result
    