'''Given a string s, return the longest palindromic substring in s.
Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"'''

def longestPalindrome(s):
        res = ""

        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1:r]

        for i in range(len(s)):
            p1 = expand(i, i)
            p2 = expand(i, i + 1)
            res = max(res, p1, p2, key=len)

        return res

def main():
    s = "babad"
    result = longestPalindrome(s)
    print("Longest palindromic substring is:", result)

    s = "cbbd"
    result = longestPalindrome(s)
    print("Longest palindromic substring is:", result)

if __name__ == "__main__":
    main()