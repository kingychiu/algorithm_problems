"""
    https://leetcode.com/problems/maximum-number-of-visible-points/
"""
from typing import List

import math


class Solution:
    # pylint: disable=too-few-public-methods
    """
    Solution
    """

    def visible_points(
        self, points: List[List[int]], angle: int, location: List[int]
    ) -> int:
        # pylint: disable=no-self-use
        """
        Return the max number of points the agent can see at the given location
        and with the given wide angle
        """
        num_points = len(points)
        num_always_visible = 0

        point_angles = []
        for i in range(num_points):
            # Make the agent location be the origin
            new_x = points[i][0] - location[0]
            new_y = points[i][1] - location[1]

            if new_x == 0 and new_y == 0:
                # It is always visible to the agent.
                num_always_visible += 1
                continue

            # Convert all points to angles from the positive x-axis counter-clockwise
            radian = math.atan2(new_y, new_x)
            if radian < 0:
                radian = 2 * math.pi + radian

            point_angle = math.degrees(radian)
            point_angles.append(point_angle)
            # For circular loop
            point_angles.append(360 + point_angle)

        # Sort the points by their angle
        point_angles.sort()

        start = 0
        max_visible = 0

        for end in range(0, len(point_angles)):
            if point_angles[start] >= 360:
                break
            if point_angles[end] - point_angles[start] > angle:
                start += 1

            # record
            max_visible = max(max_visible, end - start + 1)

        return max_visible + num_always_visible
