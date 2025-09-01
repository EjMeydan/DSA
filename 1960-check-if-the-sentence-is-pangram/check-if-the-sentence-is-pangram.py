class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
        arr = [0]*26

        for char in sentence:
            index = ord(char) - ord('a')
            arr[index] = 1

        for index in arr:
            if index == 0:
                return False
        return True
