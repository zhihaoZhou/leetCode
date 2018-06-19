class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = [0, 0]
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] < 0:
                answer[0] = index + 1
            else:
                nums[index] *= -1
        for i in range(len(nums)):
            if nums[i] > 0:
                answer[1] = i + 1
        return answer