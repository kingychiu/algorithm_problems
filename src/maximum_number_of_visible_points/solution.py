"""
    https://leetcode.com/problems/maximum-number-of-visible-points/
"""
from typing import List, Tuple, Optional

import math
from src.data_structures.leetcode.tree import Node


class Solution:
    # pylint: disable=too-few-public-methods
    """
        Solution
    """

    @staticmethod
    def _get_angle(x: int, y: int) -> float:
        """
            Return the angle from the positive x-axis counter-clockwise
        """
        radian = math.atan2(y, x)
        if radian < 0:
            radian = 2 * math.pi + radian
        return math.degrees(radian)

    def visible_points(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        # pylint: disable=no-self-use
        """
            Return the max number of points the agent can see at the given location and with the given wide angle
        """
        num_points = len(points)
        num_always_visible = 0

        if num_points == 0:
            return 0

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
            point_angle = self._get_angle(new_x, new_y)
            point_angles.append(point_angle)
            # For circular loop
            point_angles.append(360 + point_angle)

        # Sort the points by their angle
        point_angles = sorted(point_angles)

        if len(point_angles) == 0:
            return num_always_visible

        from_idx = 0
        to_idx = 0

        num_visible = 0
        max_visible = num_visible

        while True:
            # record
            num_visible = to_idx - from_idx + 1
            max_visible = max(max_visible, num_visible)

            if point_angles[from_idx] >= 360:
                break

            # check next
            next_angle = point_angles[to_idx + 1] - point_angles[from_idx]
            if next_angle > angle:
                # not valid
                from_idx += 1
            else:
                # valid
                to_idx += 1

        return max_visible + num_always_visible
