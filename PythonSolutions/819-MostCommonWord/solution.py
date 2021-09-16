# https://leetcode.com/problems/most-common-word/


# The first challenge is to iterate over the paragraph word by word
# If you use a usual loop, it would iterate char by char not word by word
# If we use string.split(), it would split by space and punctuation is appended to words
# e.g. "I am Bond, James Bond" would have one entry of "Bond," with the comma

# One approach is to clean the string to only contain alphanumeric and spaces
# We can clean using regex
# For cleanliness and readability we first define a pattern for non-alpha r'[^a-zA-Z]'
# Then we use re.sub() to find all non-alpha substrings and replace them with space
# We also lower the whole string
# Now we can loop with a split function

import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        freq = {}
        
        pattern = re.compile(r'[^a-zA-Z]')
        para = re.sub(pattern, ' ', paragraph)
        para = para.lower()

        
        for word in para.split():
            if word.isalpha():
                if word not in freq:
                    freq[word] = 1
                else:
                    freq[word] += 1
        
        # Remove banned word from freq table, could have also skipped in the above loop itself and not saved it in the first place
        for word in banned:
            if word in freq:
                freq.pop(word)
                
        # Find the key with the max value in the freq table and save it to word
        
        word = max(freq, key= lambda x: freq[x])
        
        return word
            
        
        
