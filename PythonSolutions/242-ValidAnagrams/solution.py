# https://leetcode.com/problems/valid-anagram/


# Using a single dictionary:
# Create an array of 26 characters for each letter of alphabet
# For each character in s, increment the character value in counter array
# Then for the same value of t, decrement the counter's value at that element
# Finally check that each element of the array is 0
# If not 0 then return False, they're not anagrams otherwise return True

# Solving using only one hash table

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
       
        counter = [0] * 26
        
        for i in range(0, len(s)):
            # org in python coverts the character to its unicode value. 
            # Since a has the lowest unicode value, on subtracting it,
            # we get value from 0 to 26 for the rest of the elements
            # So we can use the 26 elements array to keep a track of different character's frequencies
            
            # print(ord('a'))               # o/p = 97 
            # print(ord('b'))               # o/p = 98
            # print(ord('b') - ord('a'))    # o/p = 1
            counter[ord(s[i]) - ord('a')] += 1
            counter[ord(t[i]) - ord('a')] -= 1
        
        for i in counter:
            if i != 0:
                return False
        
        return True
            

# Using Counter method from collections to make the hash table code shorter
# The counter has lower times than both hash tables and the sort methods.
# always in 90% of time solution

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freq_s = Counter(s)
        freq_t = Counter(t)
        
        if freq_s == freq_t:
            return True
        else:
            return False

    

# My hash table solution, using two hash tables
# Time: O(n), Space: O(n)
# Can be made shorter with the Counter method from collections to create frequenct tables

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freq = {}
        freq2 = {}
        for char in s:
            if char not in freq:
                freq[char] = 1
            else:
                freq[char] += 1
        
        for char in t:
            if char not in freq2:
                freq2[char] = 1
            else:
                freq2[char] += 1
        
        if freq == freq2:
            return True
        else:
            return False


# TODO Proper function
# Implement it when you've added a sort function for strings and then using it
# With sort, Time: O(nlogn), Space: O(1)



# Python sorted function based solution, can't use in interviews, unless implement own sort function
# O(nlogn) since sorted uses quick sort internally

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            return sorted(list(s)) == sorted(list(t))
        
