class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char.lower() for char in s if char.isalnum())
        s1 = s[::-1]

        if s1==s:
            return True
        else:
            print(s)
            return False