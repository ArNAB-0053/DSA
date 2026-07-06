class Solution:
    # Intuition

    # Step 1
    # Sort intervals by:
    # - start in ascending order
    # - if starts are equal, end in descending order
    #
    # Example:
    # [[1,2], [1,5], [2,6], [2,1], [3,4]]
    # ->
    # [[1,5], [1,2], [2,6], [2,1], [3,4]]
    #
    # This ensures that for intervals with the same start,
    # the larger interval appears before the smaller one.

    # Step 2
    # Initialize:
    # - max_end = end of the first interval
    # - covered = 0
    #
    # max_end stores the largest end value seen so far.

    # Step 3
    # Traverse the remaining intervals:
    #
    # If current_end <= max_end:
    #     current interval is covered by a previous interval
    #     covered += 1
    # Else:
    #     max_end = current_end
    #
    # Since intervals are sorted by start, a previous interval
    # with end >= current_end covers the current interval.

    # Answer:
    # total_intervals - covered

    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        # sorting in special order
        # - start in ascending order
        # - if starts are equal, end in descending order

        # Example:
        # [[1,2], [1,5], [2,6], [2,1], [3,4]]
        # ->
        # [[1,5], [1,2], [2,6], [2,1], [3,4]]

        # this ensures that for intervals with the same start, the larger interval appears before the smaller one.
        intervals.sort(key=lambda x:(x[0], -x[1]))

        # keeps tracks of max end and counts the covered element
        max_end, covered = 0, 0
        for i in range(n):
            # current end
            curr_end = intervals[i][1]
            # as already stablished through sorting that start case always will be true
            # so here we are checking only the end part
            # so if the current end <= the max end(till now), means this element is covered
            # so covered count increases by 1
            if curr_end <= max_end:
                covered += 1
            # if not that means we found a new max end
            else:
                max_end = curr_end
        # returning the remaining intervals
        return n-covered