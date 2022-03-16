from unittest import skip


def twoSum(self, nums = [2,7,11,15], target = 9):
    
    #length_of_nums = len(range(nums))


    for i in range(len(nums)):

        #Set the index 
        j = 1
        while j < i:
            print("wassup")
            total = nums[j] + nums[i]
            if target == total:
                print(j + " and " + i)
                return [j, i]
            j = j + 1 

twoSum([2,])


