'''The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);

Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:
Input: s = "A", numRows = 1
Output: "A"'''

def ZigZagConversion(s , numRows):
    templet = list(range(numRows)) + list(range(numRows - 2, 0, -1))
    rows = [''] * numRows

    for i, char in enumerate(s):
        rows[templet[i%len(templet)]] += char
    return ''.join(rows)

def main():
    numRows = int(input("Enter numbers of rows : "))
    s = "PAYPALISHIRING"
    result = ZigZagConversion(s, numRows)
    print(result)

if __name__ == "__main__":
    main()