class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = defaultdict(list)
        for s in strs:
            t = str(sorted(s))
            final[t].append(s)
        return(list(final.values()))
        