class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers and numbers ending with 0 (except 0) are not palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0

        # Reverse only half of the number
        while x > reversed_half:
            digit = x % 10
            reversed_half = reversed_half * 10 + digit
            x //= 10

        # For even length: x == reversed_half
        # For odd length: x == reversed_half // 10 (middle digit removed)
        return x == reversed_half or x == reversed_half // 10

        