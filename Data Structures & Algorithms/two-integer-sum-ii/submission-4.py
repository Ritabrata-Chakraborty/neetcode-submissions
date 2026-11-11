class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ind1 = 0
        ind2 = len(numbers) - 1
        s = 0
        res = []

        while ind1 < ind2:
            s = numbers[ind1] + numbers[ind2]
            if s < target:
                ind1 += 1
            elif s > target:
                ind2 -= 1
            else:
                res.extend([ind1 + 1, ind2 + 1])
                return res

