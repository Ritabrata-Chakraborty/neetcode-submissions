class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums) - 2):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            ind1 = i + 1
            ind2 = len(nums) - 1

            while ind1 < ind2:
                s = nums[i] + nums[ind1] + nums[ind2]

                if s < 0:
                    ind1 += 1
                elif s > 0:
                    ind2 -= 1
                else:
                    res.append([nums[i], nums[ind1], nums[ind2]])

                    ind1 += 1
                    ind2 -= 1

                    while ind1 < ind2 and nums[ind1] == nums[ind1 - 1]:
                        ind1 += 1

                    while ind1 < ind2 and nums[ind2] == nums[ind2 + 1]:
                        ind2 -= 1

        return res