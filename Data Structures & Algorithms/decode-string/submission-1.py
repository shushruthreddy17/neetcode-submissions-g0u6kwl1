class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur_str = ""
        num = 0

        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch == "[":
                stack.append((cur_str,num))
                cur_str = ""
                num = 0
            elif ch == "]":
                pre_str, count = stack.pop()
                cur_str = pre_str + cur_str * count
            else:
                cur_str += ch
        
        return cur_str