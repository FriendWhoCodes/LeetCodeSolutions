

# Fails for all but one test case


class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        result = [0] * len(shifts)
        i = 0
        while i < len(shifts):
            # # print(ord(s[i]))
            # print(ord(s[i]) + shifts[i])
            j = 0
            while j <= i:
                result[j] = chr(ord(s[j]) + shifts[i])
                # print(result[j])
                j += 1
            i+= 1
        return ''.join(result)
