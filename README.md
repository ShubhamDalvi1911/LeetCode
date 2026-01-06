# LeetCode ✅
LeetCode solutions repository containing optimized code and essential problem-solving insights.

---

## Solved Problems 🧩

| Problem | Path | Status | Notes |
|---|---|---:|---|
| Two Sum (LeetCode #1) | `NumberProblems/two_sum.py` | **Solved** ✅ | Returns indices of two numbers that add up to the target (example usage included) |
| Add Two Numbers (LeetCode #2) | `NumberProblems/add_two_numbers.py` | **Solved** ✅ | Adds two numbers represented as linked lists; example result `[7, 0, 8]` |
| Longest Substring (LeetCode #3) | `StringProblems/longest_substring.py` | **Solved** ✅ | `length_of_longest_substring(s)` returns the length; e.g., `"pwwkew"` -> `3` |
| Median of Two Sorted Arrays (LeetCode #4) | `ArrayProblems/median_of_two_sorted_arrays.py` | **Solved** ✅ | Efficient O(log(min(m,n))) algorithm to find the median of two sorted arrays |
| Longest Palindromic Substring (LeetCode #5) | `StringProblems/longest_palindromic_substring.py` | **Solved** ✅ | `longest_palindrome(s)` returns the longest palindromic substring; e.g., `"babad"` -> `"bab"` |

---

## How to run 🔧

To run the example for Two Sum:

```
python NumberProblems/two_sum.py
```

To run the example for Add Two Numbers:

```
python NumberProblems/add_two_numbers.py
```

To run the example for Longest Substring:

```
python StringProblems/longest_substring.py
```

To run the example for Longest Palindromic Substring:

```
python StringProblems/longest_palindromic_substring.py
```

To run the example for Median of Two Sorted Arrays:

```
python ArrayProblems/median_of_two_sorted_arrays.py
```

---

## Run all examples ⚙️

Run all Python example files from the repository (PowerShell):

```
Get-ChildItem -Recurse -Filter "*.py" | ForEach-Object { python $_.FullName }
```

(Or use a simple shell loop on macOS/Linux: `for f in $(find . -name "*.py"); do python "$f"; done`)

---

## Repository structure 📁

- `ArrayProblems/` — array-related problems
- `NumberProblems/` — number and linked-list problems
- `StringProblems/` — string-related problems

---

## Contributing 💡

Add a new file in a descriptive folder (for example `ArrayProblems/`) with the problem implementation and then update this README by adding a new row to the "Solved Problems" table. Please include a short note in the table describing the function(s) and an example if useful.
