# 題目 給定任一數字列，數字可正可負
# 若數字列長度大於等於3，則取第三大的數字，數字重複視為同樣數字
# 若數字列小於3，則直接取最大數字

class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        #將nums中重複的元素剃除
        nums = list(set(nums))
        #將數字由大到小排列
        nums.sort(reverse=True)
        if len(nums) >= 3:
            #長度大於等於三，取第二位
            return nums[2]
        else:
            #長度小於3，取最大
            return nums[0]
