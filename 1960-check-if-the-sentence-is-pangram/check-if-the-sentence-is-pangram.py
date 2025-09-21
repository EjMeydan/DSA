class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
        letters = set(sentence)
        if len(letters) == 26:
            return True
        return False