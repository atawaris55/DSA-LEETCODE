class Solution(object):
    def decodeString(self, s):
        nums_stk = []
        str_stk = []

        num = 0
        current = ""

        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)

            elif ch == "[":
                nums_stk.append(num)
                str_stk.append(current)

                num = 0
                current = ""

            elif ch == "]":
                repeat = nums_stk.pop()
                previous = str_stk.pop()

                current = previous + current * repeat

            else:
                current += ch

        return current