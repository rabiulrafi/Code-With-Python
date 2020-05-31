class Solution(object):
    def dayOfTheWeek(self, day, month, year):

        DAYS = ["Sunday", "Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday"]

        if month < 3:
            month += 12
            year -= 1
        c, y = divmod(year, 100)
        w = (c//4 - 2*c + y + y//4 + 13*(month+1)//5 + day - 1) % 7
        return DAYS[w]

a = Solution()
print(a.dayOfTheWeek(31,8,2019))