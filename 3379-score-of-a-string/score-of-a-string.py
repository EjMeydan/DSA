class Solution:
    def scoreOfString(self, s: str) -> int:

        score = 0 
        prev = ord(s[0])

        for ch in s[1:]:
            score += abs(prev - ord(ch))
            prev = ord(ch)

        return score
        