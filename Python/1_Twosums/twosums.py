

nums = [2,7,11,15,8]
target = 10


def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        # if nums is None:
        #     return {0}

        for i, key in enumerate(nums):
            if (target - key) in dic:
                return [dic[target - key],i]
            
            dic[key] = i


print(twoSum(nums,target))