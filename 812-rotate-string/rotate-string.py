class Solution(object):
    def rotateString(self, s, goal):
        if len(s)!=len(goal):
            return False
        return s in goal+goal
