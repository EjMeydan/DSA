class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        
        nums.sort()

        output = []

        for i in range(0, len(nums), 2):
            first_num = nums[i]
            second_num = nums[i+1]
            output.append(second_num)
            output.append(first_num)
        
        return output

