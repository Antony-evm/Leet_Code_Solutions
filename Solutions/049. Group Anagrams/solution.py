# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}
        for s in strs:
            k = "".join(sorted(s))
            if k not in dictionary:
                dictionary[k] = [s]
            else:
                dictionary[k].append(s)
        return list(dictionary.values())
