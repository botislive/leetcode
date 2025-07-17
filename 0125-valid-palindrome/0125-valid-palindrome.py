class Solution:
    def isPalindrome(self, s: str) -> bool:
        stri=""
        for ch in s:
            if ch.isalpha() or ch.isdigit():
                stri+=ch.lower()
        return stri==stri[::-1]

        