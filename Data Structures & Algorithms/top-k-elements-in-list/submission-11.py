class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        freq = [[] for i in range(len(nums) + 1)]
        out = []
        for i in nums:
            hashMap[i] = 1 + hashMap.get(i, 0)

        for num, cnt in hashMap.items():
            freq[cnt].append(num)

        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                out.append(num)
                if len(out) == k:
                    return out
        return out
