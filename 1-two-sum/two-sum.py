class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #nums example [2,7,11,15] target = 9
        seen = {}
        #empty dict

        for i in range(len(nums)): # 1st run [0 - 2] | 2nd run [1 - 7]
            needed = target - nums[i] # target(9) - nums[i](index 0 - num = 2) = 7 | do same for index 1 (7) target - nums[i] = 2 
            if needed in seen: #1st run nothing in dict so goes to else | 2nd run needed = 2 we have it in seen 
                return seen[needed], i #needed of 2 is in seen dict stored at [0 - 2] we return indicies [0, 1] (2, 7)
            else:
                seen[nums[i]] = i #1st run store [0 - 2] as nothign was in seen

