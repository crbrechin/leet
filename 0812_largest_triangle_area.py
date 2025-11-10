class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        m = []
        for p,q,r in combinations(points, 3):
            # Use the shoelace theorem to cross multiply and  add
            m.append( 0.5 * abs(
                (p[0] * q[1] +
                q[0] * r[1] +
                r[0] * p[1]) -
                (p[1] * q[0] +
                q[1] * r[0] +
                r[1] * p[0]
                )
            )
            )
        return(max(m))
