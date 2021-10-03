# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        weak_rows = {}
        strength = 0
        
        for index, row in enumerate(mat):
            strength = sum(row)
            if index not in weak_rows:
                weak_rows[index] = strength
                
        # result = []
        # minimum = math.inf
        # while k > 0:
        #     for key,value in weak_rows.items():
        #         minimum = 
        #         result.append()
        
        # Following is copied from StackOverflow:
        # https://stackoverflow.com/questions/61054957/how-to-get-first-k-smallest-number-in-a-dictionary
        # Figure out more intutive way than this:
        
        result = [y[0] for y in sorted(weak_rows.items(), key = lambda x: x[1])[:k]]
        return result

            
            
            
            
        
