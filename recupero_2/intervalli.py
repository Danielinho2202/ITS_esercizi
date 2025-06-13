def merge_intervals(intervals:list[list]):
    i=0
    while i < len(intervals) :
        if intervals[i]==intervals[0]:
            continue
        if intervals[i][0]<=intervals[i-1][1]:
            intervals[i-1][1]=intervals[i][0]
            del intervals[i]

    return intervals




intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge_intervals(intervals)) # restituisce [[1, 6], [8, 10], [15,18]]
intervals = [[1, 4], [4, 5]]
print(merge_intervals(intervals)) # restituisce [[1, 5]]