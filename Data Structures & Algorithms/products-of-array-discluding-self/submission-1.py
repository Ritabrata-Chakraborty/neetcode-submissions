class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        prefix = [1] * n
        postfix = [1] * n

        for i, num in enumerate(nums):
            if i == 0:
                prefix[i] = num
                postfix[n - i - 1] = nums[n - i -1]
            else:
                prefix[i] = prefix[i-1] * num
                postfix[n - i - 1] = postfix[n - i] * nums[n - i -1]
            
        for i in range(n):
            if i == 0:
                res[i] = postfix[i + 1]
            elif i == (n - 1):
                res[i] = prefix[i - 1]
            else:
                res[i] = postfix[i + 1] * prefix[i - 1]

        return res
             


