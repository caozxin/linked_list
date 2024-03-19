from typing import (
    List,
)
from lintcode import (
    Interval,
)

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        # Write your code here

        if not intervals:
            return True
        if len(intervals) <= 1:
            return True

        # pre-sort by start time
        def start_time(each_interval: Interval):
            return each_interval.start

        intervals.sort(key=start_time)

        prev_interval_list = []

        for each in intervals:
            print(each.start, each.end)

            if not prev_interval_list:
                prev_interval_list.append(each)
            else:
                prev_meeting = prev_interval_list.pop() #LIFO
                prev_start = prev_meeting.start
                prev_end = prev_meeting.end
                curr_start = each.start
                curr_end = each.end

                # check if overlap exists:
                if prev_end > curr_start:
                    return False
        return True
