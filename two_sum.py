class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        table = {}
        for i in range(len(nums)):
            table[nums[i]] = i

        # contains
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in table and table[diff] != i:
                return [i, table[diff]]

      
def main():
    print(s.twoSum([2,7,11,15], 9))
 

main()
