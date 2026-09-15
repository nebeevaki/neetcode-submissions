class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_dict = dict()
        for word in strs:
            word_dict[str(sorted(word))] = word_dict.get(str(sorted(word)), [])
            word_dict[str(sorted(word))].append(word)
        ans = []
        for word in word_dict:
            ans.append(word_dict[word])
        return ans