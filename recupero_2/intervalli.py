def merge_intervals(intervals:list[list]):
    i=0
    while i < len(intervals) :
        if intervals[i]==intervals[0]:
            i+=1
            continue
        if intervals[i][0]<=intervals[i-1][1]:
            intervals[i-1][1]=intervals[i][1]
            del intervals[i]
            i+=1
        else:
            i+=1

    return intervals




intervals = [[1, 3], [2, 6], [8, 10], [15, 18],[16, 45]]
print(merge_intervals(intervals)) # restituisce [[1, 6], [8, 10], [15,18]]
intervals = [[1, 4], [4, 5]]
print(merge_intervals(intervals)) # restituisce [[1, 5]]