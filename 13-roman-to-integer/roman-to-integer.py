class Solution:
    def romanToInt(self, s: str) -> int:
        
    #notes for the code
    #create dic for roman numeral and value
    #total = 0
    #loop through each character in string using index i
    #get the value of the current roman numeral
    #if there is a next character (i + 1 is within bounds)
        #get the value of the next roman numeral
        #if the current value is less than the next
            #subtract current value from total (for the ones like IV, IX)
        #else:
            #add current value to total
    #else:
        #add current value to total
    # Return total

        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        total = 0 

        for i in range(len(s)):
            current_roman = s[i]
            current_value = roman[current_roman]
        
            if i + 1 < len(s):
                next_roman = s[i + 1]
                next_value = roman[next_roman]

                if current_value < next_value:
                    total -= current_value 
                else: 
                    total += current_value

            else: 
                total += current_value 
    
        return total