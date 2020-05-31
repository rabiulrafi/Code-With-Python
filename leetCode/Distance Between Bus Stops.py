import itertools
class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        if start > destination:
            start, destination = destination, start
        s_to_d = sum(itertools.islice(distance, start, destination))
        d_to_s = sum(itertools.islice(distance, 0, start)) + sum(itertools.islice(distance, destination, len(distance)))
        return min(s_to_d, d_to_s)

a = Solution()
distance = [1,2,3,4]
b= a.distanceBetweenBusStops(distance,1,3)
print(b)