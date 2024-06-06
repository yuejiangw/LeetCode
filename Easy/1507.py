class Solution:
    def reformatDate(self, date: str) -> str:
        month = {"Jan": "01", "Feb": "02", "Mar": "03", 
                 "Apr": "04", "May": "05", "Jun": "06", 
                 "Jul": "07", "Aug": "08", "Sep": "09", 
                 "Oct": "10", "Nov": "11", "Dec": "12"}
        date = date.split()
        
        i = 0
        while i < len(date[0]):
            if date[0][i].isdigit():
                i += 1
            else:
                break
        day = date[0][:i]
        if len(day) < 2:
            day = '0' + day

        res = date[2] + '-' + month[date[1]] + '-' + day
        return res