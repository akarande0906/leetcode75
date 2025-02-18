'''
LC 729: My Calendar I
'''
class MyCalendar:

    def __init__(self):
        self.calendar = []

    def book(self, startTime: int, endTime: int) -> bool:
        left, right = 0, len(self.calendar)
        if not right:
            self.calendar.append((startTime, endTime))
            return True
        
        while left < right:
            mid = (left + right) // 2
            if self.calendar[mid][1] <= startTime:
                left = mid + 1 # New Interval is greater than mid interval
            else: # New interval is to the left of the mid interval
                right = mid
            
        if left == len(self.calendar): # This means we have reached the end
            self.calendar.append((startTime, endTime))
            return True
        if self.calendar[left][0] >= endTime: # This means we have no overlap
            self.calendar.insert(left, (startTime, endTime))
            return True
        return False

        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)