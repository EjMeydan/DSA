class Solution:
    def myAtoi(self, s: str) -> int:
        
       #notes
       #setting the index to 0 
       # skipping all whitespace:
       #     while index < len(s) and s[index] == '':
       #         index += 1 

        #if we reach the end of the string, return 0 

       # set operator = 1
       #     if s[index] == '-'. sign = -1, index += 1
       #     else if s[index] == '+' sign = 1, index += 1

       # initialise number = 0

        #while index < len(s) and s[index] is a digit: 
        #    number = number * 10 + int(s[index])
        #    index += 1 

       # apply sign: number = number * sign

        #clamp to 32-bit range:
        #    if number is < -2^31: return -2^31
        #    if number is > 2^31 -1: return 2^31 - 1 

        #return number

        i = 0
        n = len(s)

        while i < n and s[i] == ' ':
            i += 1

        sign = 1
        if i < n and s[i] == '-':
            sign = -1
            i += 1

        elif i < n and s[i] == '+':
            i += 1

        num = 0 

        while i < n and s[i].isdigit():
            digit = int(s[i])
            num =  num * 10 + digit
            i += 1

        num *= sign

        Min_int =  -2**31
        Max_int = 2**31 - 1

        if num < Min_int:
            return Min_int
        if num > Max_int:
            return Max_int

        return num
