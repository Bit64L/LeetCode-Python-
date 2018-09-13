class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s is None or len(s) < 2:
            return True
        i, j = 0, len(s) - 1
        while True:
            while i < len(s) and not self.isAlpha(s[i]):
                i += 1
            while j >= 0 and not self.isAlpha(s[j]):
                j -= 1
            if i < j and s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
            if i >= j:
                break
        return True

        
    def isAlpha(self, c):
        if (ord(c) >= ord('a') and ord(c) <= ord('z')) or (ord(c) >= ord('A') and ord(c) <= ord('Z')) or (ord(c) >= ord('0') and ord(c) <= ord('9')):
            return True
        return False


solution = Solution()
print(solution.isPalindrome("0P"))