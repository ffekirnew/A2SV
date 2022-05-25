class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        
        def distance_from_the_origin(point):
            return point[0] ** 2 + point[1] ** 2

        points_and_distances = []
        closest_points = []

        for point in points:
            points_and_distances.append([distance_from_the_origin(point), point])

        points_and_distances.sort()

        for index in range(k):
            closest_points.append(points_and_distances[index][1])

        return closest_points