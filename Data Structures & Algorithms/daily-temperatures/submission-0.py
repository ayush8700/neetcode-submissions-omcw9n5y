class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans= [0]*len(temperatures)
        stack = []
        for pos, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                index = stack.pop()
                ans[index] = pos - index
            stack.append(pos)
        return ans