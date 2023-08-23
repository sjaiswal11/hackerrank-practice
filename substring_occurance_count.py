# In this challenge, the user enters a string and a substring. 
# You have to print the number of times that the substring occurs in the given string. 
# String traversal will take place from left to right, not from right to left.
# NOTE: String letters are case-sensitive.
# Input Format
# The first line of input contains the original string. 
# The next line contains the substring.
# Constraints
# Each character in the string is an ascii character.
# Output Format
# Output the integer number indicating the total number of occurrences of the substring in the original string.

class SubstringCount:
    def __init__(self, string, sub_string):
        self.string = string
        self.sub_string = sub_string
        self.count = 0
        
    def sub_string_count(self):
        for i in range(0, len(self.string)):
            if self.string[i:i+len(self.sub_string)] == self.sub_string:
                self.count += 1
        return self.count
if __name__ == '__main__':
    sc = SubstringCount('ABCDCDC', 'CDC')
    count = sc.sub_string_count()
    print(count)