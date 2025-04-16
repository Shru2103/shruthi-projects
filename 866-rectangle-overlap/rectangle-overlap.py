class Solution:
    def isRectangleOverlap(self, rec1, rec2):
        # Check if one rectangle is completely to the left, right, above or below the other
        if rec1[2] <= rec2[0] or rec1[0] >= rec2[2] or rec1[3] <= rec2[1] or rec1[1] >= rec2[3]:
            return False
        return True

        