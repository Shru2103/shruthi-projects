class Solution:
    def longestPalindrome(self, s):
        if not s:
            return ""
        
        def expand_around_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        longest_palindrome = ""
        for i in range(len(s)):
            # Odd length palindrome
            palindrome1 = expand_around_center(i, i)
            # Even length palindrome
            palindrome2 = expand_around_center(i, i + 1)
            
            # Update the longest palindrome
            if len(palindrome1) > len(longest_palindrome):
                longest_palindrome = palindrome1
            if len(palindrome2) > len(longest_palindrome):
                longest_palindrome = palindrome2
        
        return longest_palindrome

        