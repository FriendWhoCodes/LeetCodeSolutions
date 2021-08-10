# https://leetcode.com/problems/count-items-matching-a-rule/

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        
        rule_index = {
            "type"  : 0,
            "color" : 1,
            "name"  : 2
        }
        
        condition = rule_index[ruleKey]
        
        count = 0
        for rows in items:
            if rows[condition] == ruleValue:
                count += 1

        return count
