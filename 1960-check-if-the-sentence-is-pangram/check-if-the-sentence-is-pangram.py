class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
        letters = {}

        for char in sentence:
            if char not in letters:
                letters[char] = 1
        
        if len(letters) >= 26:
            return True
        return False