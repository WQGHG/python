
class Solution:
    # @param {integer} num
    # @return {integer}
    def addDigits(self, num):
        length = len(str(num))
        while num>=10:
            L = []
            for i in reversed(range(length)):
                l = num/10**i
                num = num%(10**i)
                L.append(l)
            num = sum(L)
        return num
