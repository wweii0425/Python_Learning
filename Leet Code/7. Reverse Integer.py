# 題目 給定任一數字，數字可正可負
# 將他反轉如 12345 >> 54321, -12345 >> -54321

class solution:
    def reverseInteger(self, input: int):
        # 思考方式，先判斷正負數
        # 將數字轉成字串 str()
        # 將字串反轉[::-1]
        # 將反轉字串轉為數字
        # print(len(input))

        if input < 0:
            result = -1 * int(str(-input)[::-1])
        else:
            result = 1 * int(str(input)[::-1])

        if result > 2**31 or result < -2**31:
            result = 0
        return result


solutionInit = solution()
print(solutionInit.reverseInteger(-12345))
