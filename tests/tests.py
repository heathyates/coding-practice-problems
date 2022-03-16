from coding_problems.two_sum import twoSum 

def test_twoSum():
    nums1 = [2, 7, 11, 15] # target = 9
    nums2 = [3,2, 4] #target = 6
    nums3 = [2,3,4] #target = 6
    nums4 = [3,3] #target = 6

    assert twoSum(nums1, 9) == [0,1]