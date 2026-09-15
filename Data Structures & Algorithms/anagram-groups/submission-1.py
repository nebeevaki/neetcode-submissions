class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_dict = dict()
        for word in strs:
            word_dict[str(sorted(word))] = word_dict.get(str(sorted(word)), [])
            word_dict[str(sorted(word))].append(word)
        return list(word_dict.values())