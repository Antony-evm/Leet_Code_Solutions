# Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.

# According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        cit = [-i for i in citations]
        heapq.heapify(cit)
        res = 0
        i = 1
        while i <= len(citations):
            val = heapq.heappop(cit)
            if -val < i:
                break
            else:
                res = i
            i += 1
        return res
