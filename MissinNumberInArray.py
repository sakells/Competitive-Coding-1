class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        low = 0
        high = len(nums) - 1
        while high - low >= 2:
            mid = low + (high - low) // 2
            if nums[low] - low == nums[mid] - mid:
                low = mid
            else:
                high = mid
        return (nums[low] + nums[high]) // 2
