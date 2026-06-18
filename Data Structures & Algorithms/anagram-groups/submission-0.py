class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        for s in strs:
            initial_s = sorted(s)
            sorted_s=''.join(initial_s)
            print(initial_s)
            if sorted_s not in hash_map:
                hash_map[sorted_s]=[s]
            else:
                hash_map[sorted_s].append(s)
        return list(hash_map.values())