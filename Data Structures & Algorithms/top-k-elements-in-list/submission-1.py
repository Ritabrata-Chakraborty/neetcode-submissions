class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        maxk = len(nums)
        count_hmap = {} # num as index and its count as value
        freq = [[] for i in range(maxk)]

        for num in nums:
            count_hmap[num] = 1 + count_hmap.get(num, 0)

        for num, count in count_hmap.items():
            freq[count - 1].append(num)

        res = []
        for i in range(maxk, 0, -1):
            for f in freq[i-1]:
                res.append(f)
                if len(res) == k:
                    return res

        





        
            
        