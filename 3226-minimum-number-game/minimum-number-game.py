class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        
        result = []

        sorted_list = sorted(nums)

        for i in range(0, len(sorted_list), 2):
            alice = sorted_list[i]
            bob = sorted_list[i+1]

            result.append(bob)
            result.append(alice)
        
        return result