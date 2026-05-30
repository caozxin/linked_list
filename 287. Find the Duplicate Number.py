class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        

        fast, slow = nums[0], nums[0] # we initiate both pointers to 1 now

        while True:
            fast = nums[nums[fast]] # we use the fact that indx and val are between [1, n] to move 2 steps for fast and 1 step for slow
            slow = nums[slow]

            # print("fast, slow", fast, slow)

            if fast == slow:
                break

        slow = nums[0] # we reset slow at the beginnging and keep fast at last meeting place

        while fast != slow: # move fast and slow 1 step at one time when them meet
            slow = nums[slow]
            fast = nums[fast]

        return slow # then wherever they met is the dups
