# https://leetcode.com/problems/reformat-date/

class Solution:
    def reformatDate(self, date: str) -> str:
        
        day = date.split(" ")
        print(day)
        
        months = {
            "Jan" : 1,
            "Feb" : 2,
            "Mar" : 3,
            "Apr" : 4,
            "May" : 5,
            "Jun" : 6,
            "Jul" : 7,
            "Aug" : 8,
            "Sep" : 9,
            "Oct" : 10,
            "Nov" : 11,
            "Dec" : 12
        }
        d = day[0]
        d = "".join(filter(str.isdigit, d))
        d = d.zfill(2)
        m = str(months[day[1]]).zfill(2)
        y = day[2]
        
        
        
        return y +"-"+ m +"-"+d
