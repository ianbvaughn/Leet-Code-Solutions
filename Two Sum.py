def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    # nums[int]
    # int target = ind1 + ind2

    # iterate through the array

    for i_idx, i_item in enumerate(nums):
        for j_idx, j_item in enumerate(nums):
            if i_item + j_item == target and i_idx != j_idx:
                return [i_idx, j_idx]
            else:
                continue