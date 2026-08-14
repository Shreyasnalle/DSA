class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        final_anagrams = {}
        for word in strs :
            key = "".join(sorted(word))
            if key not in final_anagrams : 
                final_anagrams[key] = []
            final_anagrams[key].append(word)
        return list(final_anagrams.values())