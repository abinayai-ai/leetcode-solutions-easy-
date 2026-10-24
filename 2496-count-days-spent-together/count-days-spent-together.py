
class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        def convert(date):
            month, day = map(int, date.split("-"))
            days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            return sum(days[:month - 1]) + day

        start = max(convert(arriveAlice), convert(arriveBob))
        end = min(convert(leaveAlice), convert(leaveBob))

        return max(0, end - start + 1)

        