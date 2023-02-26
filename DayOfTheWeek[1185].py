# Given a date, return the corresponding day of the week for that date.

# The input is given as three integers representing the day, month and year respectively.

# Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.

 

# Example 1:

# Input: day = 31, month = 8, year = 2019
# Output: "Saturday"

# Example 2:

# Input: day = 18, month = 7, year = 1999
# Output: "Sunday"

# Example 3:

# Input: day = 15, month = 8, year = 1993
# Output: "Sunday"

 

# Constraints:

#     The given dates are valid dates between the years 1971 and 2100.

# Accepted
# 51.9K
# Submissions
# 90.2K
# Acceptance Rate
# 57.5%


# import datetime
class Solution(object):
    def dayOfTheWeek(self, day, month, year):
        """
        :type day: int
        :type month: int
        :type year: int
        :rtype: str
        """
        # faster Zeller's algoritm
        days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        if month < 3: 
            month += 12
            year -= 1
        k = year % 100
        j = year // 100
        h = (day + 13*(month+1)//5 + k + k//4 + j//4 + 5*j) % 7
        return days[h]

        # date_obj = datetime.datetime(year, month, day)
        # return date_obj.strftime("%A")
    
day = 31,18,15
month = 8,7,8
year = 2019, 1999,1993

for i in range(len(year)):
    Solution.dayOfTheWeek('Success', day[i], month[i], year[i])