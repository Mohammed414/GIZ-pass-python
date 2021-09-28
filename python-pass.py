

class Solution:

    @staticmethod
    def longest_palindromic(s: str) -> str:
        # an empty list to store all possible palindromic substrings
        arr = []
        n = len(s)
        # Looping through string to get all combinations of substrings but only store the palindromic ones
        for i in range(n):
            for j in range(i, n):
                # get a sub string
                sub_string = s[i:j + 1]
                # check whether it is palindromic
                if sub_string == sub_string[::-1]:
                    arr.append(sub_string)

        # get the longest palindromic substring from the list
        longest_palindromic_substring = max(arr, key=len)

        # prints the result
        print(longest_palindromic_substring)


Solution.longest_palindromic("babad")
# outputs: bab

Solution.longest_palindromic("cbbd")
#outputs: bb
