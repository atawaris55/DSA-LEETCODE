class Solution(object):
    def checkOverlap(self, radius, xCenter, yCenter, x1, y1, x2, y2):
        xcloset=max(x1,min(xCenter,x2))
        ycloset=max(y1,min(yCenter,y2))
        dx=xCenter-xcloset
        dy=yCenter-ycloset
       
        return (dx*dx+dy*dy)<=radius*radius