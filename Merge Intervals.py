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
    @param intervals: interval list.
    @return: A new interval list.
    """
    def merge(self, intervals: List[Interval]) -> List[Interval]:
        # write your code here

        if not intervals:
            return intervals

        if len(intervals) <= 1: # return if there is only one interval in the list
            return intervals

        # we need to first pre-process input list of intervals by its start value:
        def interval_start(each_interval: Interval):
            return each_interval.start

        intervals.sort(key=interval_start)
        
        result_list = []

        for each in intervals:
            print(each.start, each.end)
            # check if potential overlap:
            if not result_list:
                result_list.append(each)
                continue
            
            curr_start = each.start
            curr_end = each.end
            prev_interval = result_list.pop() # we pop the last one into the result_list
            prev_start = prev_interval.start
            prev_end = prev_interval.end

            if curr_start <= prev_end:
                print("find overlap!")
                new_start = min(prev_start, curr_start)
                new_end = max(prev_end, curr_end)
                new_interval = Interval(new_start, new_end)
                result_list.append(new_interval)
            else:
                result_list.append(prev_interval)
                result_list.append(each)

            # print("result_list", result_list[0])

            
        return result_list
