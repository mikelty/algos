from itertools import combinations


class Solution:
    def numPoints(self, points,r):
        best = 1
        for (x1, y1), (x2, y2) in combinations(points, 2):
            mx, my = (x1 + x2) / 2, (y1 + y2) / 2  # midpoint
            dx, dy = (x1 - x2), (y1 - y2)
            q = (dx ** 2 + dy ** 2) ** 0.5
            if q / 2 < r + 1e-5:
                d = (r ** 2 - q ** 2 / 4) ** 0.5  # distance from midpoint to center
                sx, sy = d * dy / q, d * dx / q  # coordinate distances (up to a negation) from midpoint to center
                c1x, c1y = (mx + sx), (my - sy)
                c2x, c2y = (mx - sx), (my + sy)
                for cx, cy in ((c1x, c1y), (c2x, c2y)):
                    count = 0
                    for x, y in points:
                        if ((cx - x) ** 2 + (cy - y) ** 2) < r ** 2 + 1e-5:
                            count += 1
                    best = max(best, count)
        return best
