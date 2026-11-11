class Solution(object):
    def minimumCost(self, cost1, cost2, costBoth, need1, need2):

        cost_separate = (need1 * cost1) + (need2 * cost2)

        cost_both = max(need1, need2) * costBoth

        common = min(need1, need2)

        cost_mixed = (common * costBoth) + \
                     ((need1 - common) * cost1) + \
                     ((need2 - common) * cost2)

        return min(cost_separate, cost_both, cost_mixed)
        