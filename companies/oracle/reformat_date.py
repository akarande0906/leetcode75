'''
LC 1507: Reformat Date
'''
class Solution:
    def reformatDate(self, date: str) -> str:
        # map months 
        months = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 
            'May': '05', 'Jun': '06', 'Jul': '07', 'Aug': '08', 
            'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'}
        date, month, year = date.split(' ')
        ret_arr = []
        ret_arr.append(year)
        ret_arr.append(months[month])
        date_num = int(date[0])
        if date[1] >= '0' and date[1] <= '9':
            date_num = date_num * 10 + int(date[1])
            date_str = str(date_num)
        else:
            date_str = '0' + str(date_num)
        ret_arr.append(date_str)
        return '-'.join(ret_arr)
# Time: O(1)
# Space: O(1)

reformat_date = Solution().reformatDate
assert reformat_date("20th Oct 2052") == "2052-10-20"
assert reformat_date("6th Jun 1933") == "1933-06-06"
assert reformat_date("26th May 1960") == "1960-05-26"
assert reformat_date("6th Jun 1933") == "1933-06-06"