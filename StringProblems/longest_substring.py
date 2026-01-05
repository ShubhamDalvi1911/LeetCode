'''Given a string s, find the length of the longest substring without duplicate characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.'''

def longestsubstrings(s: str) -> list:
    parts = []
    current = ""
    for ch in s:
        if ch not in current:
            current += ch
        else:
            # Found duplicate - append current and slide the window
            parts.append(current)
            idx = current.index(ch)
            current = current[idx + 1:] + ch
    if current:
        parts.append(current)
    return parts

def main():
    s = "pwwkew"
    parts = longestsubstrings(s)
    # print("Unique substrings without duplicate characters are:", parts)
    print("Length of longest substring without duplicate characters is:", max(len(part) for part in parts)) 

if __name__ == "__main__":
    main()