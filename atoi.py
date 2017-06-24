import sys
class Solution(object):
    
    def isDigit(self,char):
        if ord(char) >= ord('0') and ord(char) <=ord('9'):
            return True 
        return False
        
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        
        # return zero if unable to convert
        result = 0
        
        # skip white spaces
        i = 0
        l = len(str)
        #empty string
        if l==0:
            return 0
        
        while( i<l and str[i]==" " ):
            i += 1

        if i==l:
            return 0
        # ignore the other characters after integer
        
        # check for sign
        sign = "+"
        signFound = False
        
        if i<l and str[i] == "+":
            signFound = True
            i+=1
        elif i<l and str[i] == "-":
            sign = "-"
            signFound = True
            i+=1
        
        #check first position after sign
        if i<l and self.isDigit(str[i])==False:
            return 0
        else:
            while (i<l and self.isDigit(str[i])==True):
                result = result * 10 + (ord(str[i]) - ord('0'))
                i+= 1 
        # change result if signFound
        
        if signFound==True and sign=="-":
            result = result * - 1
        
        # return max or min if crosses the boundary
        if result > 2147483647:
            result = 2147483647
        if result < -2147483648:
            result = -2147483648
        return result
       

