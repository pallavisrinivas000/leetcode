class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        return len((' '.join(s.split(" ")).split())[-1])
        